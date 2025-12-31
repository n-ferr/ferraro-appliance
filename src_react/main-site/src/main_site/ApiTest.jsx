import React from 'react';
import { useState } from 'react';
import { incrementClave, fetchClave } from '../services/generic.js'

export default function ApiTest() {

    const [displayValue, setDisplayValue] = useState(0)

    const apiTestClick = async () => {
        const newDisplayValue = await incrementClave(displayValue);
        console.log('api was called');
        setDisplayValue(newDisplayValue);
    }

    return (
        <div>
            <h1>ApiTest</h1>
            <div>{ displayValue }</div>
            <button onClick={(() => apiTestClick())}>Click It</button>
        </div>
    )
}
