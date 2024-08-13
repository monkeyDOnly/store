import React, { useState } from 'react';
import axios from 'axios';
import './form.css'; // Importa o CSS comum
import { useNavigate } from 'react-router-dom';

const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLoginClick = () => {
        navigate('/login');
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            await axios.post('http://localhost:8000/auth/register', {
                username,
                password,
            });
            alert('Cadastro realizado com sucesso!');
            setUsername('');
            setPassword('');
            navigate('/login');
        } catch (err) {
            setError('Falha no cadastro. Verifique seus dados.');
        }
    };

    return (
        <div className="form-container">
            <form className="form" onSubmit={handleSubmit}>
                <h2>Cadastro</h2>
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
                <button type="submit" className="form-button">Cadastrar</button>
                {error && <p>{error}</p>}
            </form>
            <div className="button-group">
                <button className="form-button" onClick={handleLoginClick}>
                    Entrar
                </button>
            </div>
        </div>
    );
};

export default Register;
