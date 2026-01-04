from django.db import models
from django.conf import settings


class Ticket(models.Model):
    '''service ticket model'''

    STATUSES = [
        ('NEW', 'New'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('WAITING_PARTS', 'Waiting for Parts'),
        ('WAITING_INFO', 'Waiting for info'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]

    ticket_number = models.CharField(max_length=20, unique=True, editable=False)

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer_tickets',
        limit_choices_to={'role': 'CUSTOMER'}
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets',
        limit_choices_to={'role': 'TECH'}
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUSES, default='NEW')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    is_floater = models.BooleanField(default=False)

    appliance_type = models.CharField(max_length=100)  
    appliance_brand = models.CharField(max_length=100, blank=True)
    appliance_model = models.CharField(max_length=100, blank=True)
    model_number = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['ticket_number']),
            models.Index(fields=['status']),
            models.Index(fields=['customer']),
            models.Index(fields=['assigned_to']),
        ]

    def __str__(self):
        return f"{self.ticket_number} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            from datetime import datetime
           
            date_str = datetime.now().strftime('%Y%m%d')
            prefix = f'TKT-{date_str}'

            last_ticket = Ticket.objects.filter(
                ticket_number__startswith=prefix
            ).order_by('ticket_number').last()
            
            if last_ticket:
                last_num = int(last_ticket.ticket_number.split('-')[-1])
                new_num = last_num + 1
            else:
                new_num = 1
            
            self.ticket_number = f'{prefix}-{new_num:04d}'
        
        # Always call parent save
        super().save(*args, **kwargs)