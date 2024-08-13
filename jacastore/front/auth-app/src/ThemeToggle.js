import React, { useState, useEffect } from 'react';

const ThemeToggle = () => {
    const [theme, setTheme] = useState(localStorage.getItem('theme') || 'light-mode');

    useEffect(() => {
        document.body.className = theme;
        localStorage.setItem('theme', theme);
    }, [theme]);

    const toggleTheme = () => {
        setTheme((prevTheme) => (prevTheme === 'light-mode' ? 'dark-mode' : 'light-mode'));
    };

    return (
        <button onClick={toggleTheme} className="theme-toggle-button">
            {theme === 'light-mode' ? 'Switch to Dark Mode' : 'Switch to Light Mode'}
        </button>
    );
};

export default ThemeToggle;
