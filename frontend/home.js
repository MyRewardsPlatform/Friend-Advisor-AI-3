// frontend/home.js

import React, { useState } from 'react';
import axios from 'axios';

const Home = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleRegister = async () => {
        try {
            const response = await axios.post('/register', {
                username: username,
                password: password
            });
            setMessage(response.data.msg);
        } catch (error) {
            setMessage(error.response.data);
        }
    };

    const handleLogin = async () => {
        try {
            const response = await axios.post('/login', {
                username: username,
                password: password
            });
            localStorage.setItem('access_token', response.data.access_token);
            setMessage('Logged in successfully');
        } catch (error) {
            setMessage(error.response.data);
        }
    };

    return (
        <div>
            <h1>Welcome to FAST System</h1>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={e => setUsername(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={e => setPassword(e.target.value)}
            />
            <button onClick={handleRegister}>Register</button>
            <button onClick={handleLogin}>Login</button>
            <p>{message}</p>
        </div>
    );
};

export default Home;
