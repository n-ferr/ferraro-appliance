import api from './api';

export const incrementClave = async (displayValue) => {
    try {
            const res = await api.post('/tests/', {value: displayValue});
            return res.data.value;
    } catch(error) {
        console.log('try harder');
        throw(error);
    }
}

export const fetchClave = async () => {
    try {
        const res = await api.get('/tests/');
        return res.data;
    } catch(error) {
        console.log('try harder');
        throw(error);
    }
}