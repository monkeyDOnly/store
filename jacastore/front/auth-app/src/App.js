import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import ProtectedRoute from './components/ProtectedRoute';
import Dashboard from './components/Homepage';
import CpfValidator from './components/brada';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/register" element={<Register />} /> {/* Adicione a rota para registro */}
                <Route path="/protected" element={<ProtectedRoute component={() => <div>Protected Page</div>} />} />
                {/* <Route path="/" element={<div>Home Page</div>} /> Página inicial ou qualquer rota pública */}
                <Route path="/Dashboard" element={<ProtectedRoute component={Dashboard} />}/>
                <Route path="/bradaSaldo" element={<ProtectedRoute component={CpfValidator} />}/>
            </Routes>
        </Router>
    );
};

export default App;
