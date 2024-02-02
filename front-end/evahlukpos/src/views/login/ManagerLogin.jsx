import { useRef, useState, useEffect } from 'react';
import Swal from 'sweetalert2'
import useAuth from '../../hooks/useAuth';
import { Link, useNavigate, useLocation } from 'react-router-dom';

import axios from 'axios';
const LOGIN_URL = 'http://localhost:8000/api/login/';

const ManagerLogin = () => {
    
    const { setAuth } = useAuth();

    const navigate = useNavigate();
    const location = useLocation();
    const from = location.state?.from?.pathname || "/";

    const userRef = useRef();
    const errRef = useRef();

    const [username, setUser] = useState('');
    const [password, setPwd] = useState('');
    const [errMsg, setErrMsg] = useState('');
    

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setErrMsg('');
    }, [username, password])

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log("Data to be posted:", { username, password });
        try {
            const response = await axios.post(LOGIN_URL,
                JSON.stringify({ username, password }),
                {
                    headers: { 'Content-Type': 'application/json' },
                }
            );
            console.log(JSON.stringify(response?.data));
            //console.log(JSON.stringify(response));
            const accessToken = response?.data?.token;
            const isManager = response?.data?.is_manager;

            // const role = response?.data?.role;
            console.log("Access Token:", accessToken);
            console.log("Role:", isManager);
            setAuth({ username, password, isManager, accessToken, roles: ['isManager'] });
            setUser('');
            setPwd('');
            Swal.fire({
                icon: 'success',
                title: 'Login Successful!',
                text: 'You wil be directed to your dashboard.',
            }).then(() => {
                if (isManager) {
                    console.log('Redirecting to /dashboard');
                    navigate('/managerdashboard');
                } else {
                    // Redirect to another default page
                    console.log('Redirecting to /login');
                    navigate('/managerLogin');
                }
            })
            
            navigate(from, { replace: true });
        } catch (err) {
            if (!err?.response) {
                setErrMsg('No Server Response');
            } else if (err.response?.status === 400) {
                setErrMsg('Missing Username or Password');
            } else if (err.response?.status === 401) {
                setErrMsg('Unauthorized');
            } else {
                setErrMsg('Login Failed');
            }
            errRef.current.focus();
        }
    }

    return (

        <section>
            <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
            <h1>Sign In</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username:</label>
                <input
                    type="text"
                    id="username"
                    ref={userRef}
                    autoComplete="off"
                    onChange={(e) => setUser(e.target.value)}
                    value={username}
                    required
                />

                <label htmlFor="password">Password:</label>
                <input
                    type="password"
                    id="password"
                    onChange={(e) => setPwd(e.target.value)}
                    value={password}
                    required
                />
                <button>Sign In</button>
            </form>
            <p>
                Need an Account?<br />
                <span className="line">
                    <Link to="/">Sign Up</Link>
                </span>
            </p>
        </section>

    )
}

export default ManagerLogin
