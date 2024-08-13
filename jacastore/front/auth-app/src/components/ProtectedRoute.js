import React, { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';
import api from '../api/api'; // Importa a instância do Axios configurada

const ProtectedRoute = ({ component: Component }) => {
    const [authorized, setAuthorized] = useState(null);

    useEffect(() => {
        const checkAuthorization = async () => {
            try {
                await api.get('/protected'); // Testa a rota protegida
                setAuthorized(true);
            } catch (error) {
                setAuthorized(false);
            }
        };

        checkAuthorization();
    }, []);

    if (authorized === null) {
        return <div>Loading...</div>; // Opcional: mostra um carregando enquanto verifica
    }

    return authorized ? <Component /> : <Navigate to="/login" />;
};

export default ProtectedRoute;
