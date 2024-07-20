// frontend/score_view.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_CONFIG } from '../config';

const ScoreView = () => {
    const [score, setScore] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Fetch user score from the API
        const fetchData = async () => {
            try {
                const scoreResponse = await axios.get(`${API_CONFIG.BASE_URL}/score`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                    }
                });

                setScore(scoreResponse.data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching score: ", error);
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (!score) {
        return <div>Error fetching score.</div>;
    }

    return (
        <div>
            <h1>Your FAST Score</h1>
            <p>Your Friend Advisor Score (FAST) is a measure of your social authenticity based on your online activities.</p>
            <h2>Score: {score}</h2>
            <p>This score is updated in real-time and is secured using blockchain technology.</p>
        </div>
    );
};

export default ScoreView;
