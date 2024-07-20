// frontend/user_profile.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_CONFIG } from '../config';

const UserProfile = () => {
    const [user, setUser] = useState(null);
    const [score, setScore] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Fetch user data and score from the API
        const fetchData = async () => {
            try {
                const userResponse = await axios.get(`${API_CONFIG.BASE_URL}/user`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token')}`
                    }
                });
                const scoreResponse = await axios.get(`${API_CONFIG.BASE_URL}/score`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token')}`
                    }
                });

                setUser(userResponse.data);
                setScore(scoreResponse.data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching data: ", error);
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (!user || !score) {
        return <div>Error fetching user data or score.</div>;
    }

    return (
        <div>
            <h1>User Profile</h1>
            <h2>{user.username}</h2>
            <p>FAST Score: {score}</p>
        </div>
    );
};

export default UserProfile;
