import React, { useState } from 'react';
import axios from 'axios';
import './form.css'; // Importa o CSS comum
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleRegisterClick = () => {
        navigate('/register');
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post('http://localhost:8000/auth/login', {
                username,
                password,
            });
            console.log(response.text)

            localStorage.setItem('token', response.data.access_token);
            console.log(response.data.access_token)
            navigate('/bradaSaldo');
        } catch (err) {
            console.log(err)
            setError('Falha no login. Verifique suas credenciais.');
        }
    };

    return (
        <div className="form-container">
            <form className="form" onSubmit={handleSubmit}>
                <h2>Login</h2>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder="Username"
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Password"
                        required
                    />
                </div>
                <button type="submit" className="form-button">Log In</button>
                {error && <p>{error}</p>}
            </form>
            <div className="button-group">
                <button className="form-button" onClick={handleRegisterClick}>
                    Cadastrar
                </button>
            </div>
        </div>
    );
};

export default Login;
