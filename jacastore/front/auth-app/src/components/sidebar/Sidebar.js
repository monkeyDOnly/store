import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Sidebar.css';
import logo from '../../assets/jaca.jpg'

const Sidebar = ({SidebarOpen, closeSidebar}) => {

    const [userInfo, setUserInfo] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogout = () => {
        const endSession = async () => {
            try {
                const response = await axios.get('http://localhost:8000/auth/logout', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`
                    }
                });
                setUserInfo(response.data);
            } catch (error) {
                setError('Failed to fetch user information.');
            } finally {
                setLoading(false);
            }
        }
        endSession();
        localStorage.removeItem('token');
        navigate('/login');
    };

    return (
        <div className={SidebarOpen ? "sidebar-responsive": ""} id="sidebar">
            <div className="sidebar__title">
                <div className="sidebar__img">
                    <img src={logo} alt="logo" />
                    <h1>JACARÉ STORE</h1>
                </div>
                
                <i 
                onClick={() => closeSidebar()}
                className="fa fa-times"
                id="sidebarIcon"
                arial-hidden="true"
                ></i>
            </div>
            <div className="sidebar_menu">
                <div className="sidebar__link active_menu_link">
                    <i className="fa fa-minus-square"></i>
                    <a href="#">Home</a>
                </div>
                <h2>ADMIN</h2>
                {/* <div className="sidebar__market">
                    <button onClick={handleLogout}>Market</button>
                </div>
                <div className="sidebar__pedidos">
                    <button onClick={handleLogout}>Pedidos</button>
                </div>
                <div className="sidebar__referencia">
                    <button onClick={handleLogout}>Referencia</button>
                </div>
                <div className="sidebar__logout">
                    <button onClick={handleLogout}>Logout</button>
                </div> */}
            </div>
        </div>
    )
}

export default Sidebar;