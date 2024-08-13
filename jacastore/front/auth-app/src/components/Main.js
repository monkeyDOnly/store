import React, { useState } from 'react';
import Login from './Login';
import Register from './Register';

const Main = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [showLogin, setShowLogin] = useState(true);

    const handleLogin = () => setIsLoggedIn(true);
    const handleLogout = () => setIsLoggedIn(false);

    return (
        <div className="main-container">
            {isLoggedIn ? (
                <div>
                    <h2>Bem-vindo!</h2>
                    <button className="form-button" onClick={handleLogout}>Logout</button>
                </div>
            ) : (
                <div>
                    {showLogin ? (
                        <Login 
                            onLogin={handleLogin} 
                            onSwitchToRegister={() => setShowLogin(false)} 
                        />
                    ) : (
                        <Register 
                            onSwitchToLogin={() => setShowLogin(true)} 
                        />
                    )}
                </div>
            )}
        </div>
    );
};

export default Main;
