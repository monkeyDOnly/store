import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Sidebar from './sidebar/Sidebar'

const Dashboard = () => {
    const [userInfo, setUserInfo] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [menuOpen, setMenuOpen] = useState(false);
    const [miniMenuOpen, setMiniMenuOpen] = useState(false);
    const navigate = useNavigate();

    const [sidebarOpen, setSidebarOpen] = useState(false);
    const openSidebar = () => {
        setSidebarOpen(true);
    }
    const closeSidebar = () => {
        setSidebarOpen(false);
    }

    useEffect(() => {
        const fetchUserInfo = async () => {
            try {
                const response = await axios.get('http://localhost:8000/user/info', {
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
        };

        fetchUserInfo();
    }, []);

    // const handleLogout = () => {
    //     const endSession = async () => {
    //         try {
    //             const response = await axios.get('http://localhost:8000/auth/logout', {
    //                 headers: {
    //                     Authorization: `Bearer ${localStorage.getItem('token')}`
    //                 }
    //             });
    //             setUserInfo(response.data);
    //         } catch (error) {
    //             setError('Failed to fetch user information.');
    //         } finally {
    //             setLoading(false);
    //         }
    //     }
    //     endSession();
    //     localStorage.removeItem('token');
    //     navigate('/login');
    // };

    const handleMiniMenuToggle = () => {
        setMiniMenuOpen(!miniMenuOpen);
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

    return (

        <div className="container">
            <Sidebar sidebarOpen={sidebarOpen} closeSidebar={closeSidebar} />
        </div>

        // <div className="dashboard">
        //     <header className="header">
        //         <div className="header-content">
        //             <div className="menu-toggle" onClick={() => setMenuOpen(!menuOpen)}>
        //                 <span className="menu-icon">☰</span>
        //             </div>
        //             <div className="logo">JACARE CDS</div>
        //             <div className="user-menu">
        //                 <span className="user-icon" onClick={handleMiniMenuToggle}>
        //                     ☰
        //                 </span>
        //                 {miniMenuOpen && (
        //                     <div className="mini-menu">
        //                         <button onClick={() => navigate('/reload-balance')}>Recarregar Saldo</button>
        //                         <button onClick={handleLogout}>Logout</button>
        //                         <button onClick={() => navigate('/my-orders')}>Meus Pedidos</button>
        //                     </div>
        //                 )}
        //             </div>
        //         </div>
        //     </header>
        //     <div className={`main-content ${menuOpen ? 'menu-open' : ''}`}>
        //         <aside className="sidebar">
        //             <nav>
        //                 <ul>
        //                     <li><a href="#home">Home</a></li>
        //                     <li><a href="#about">About</a></li>
        //                     <li><a href="#services">Services</a></li>
        //                     <li><a href="#contact">Contact</a></li>
        //                 </ul>
        //             </nav>
        //         </aside>
        //         <main className="content">
        //             <h2>Welcome to your Dashboard</h2>
        //             {userInfo ? (
        //                 <div>
        //                     <p>Username: {userInfo.username}</p>
        //                     <p>Your balance: R${userInfo.saldo.toFixed(2)}</p>
        //                 </div>
        //             ) : (
        //                 <p>No user information available.</p>
        //             )}
        //         </main>
        //     </div>
        // </div>
    );
};

export default Dashboard;
