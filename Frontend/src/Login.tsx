import React, { useState } from 'react';
import './Login.css';

interface LoginProps {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    onLoginSuccess: (data: any) => void;
}

const Login: React.FC<LoginProps> = ({ onLoginSuccess }) => {
    // false = show sign-in, true = show sign-up (active state)
    const [isActive, setIsActive] = useState(false);

    // State for sign-up form inputs
    const [signupData, setSignupData] = useState({
        name: '',
        email: '',
        password: ''
    });

    // State for sign-in form input (Google login)
    const [signinEmail, setSigninEmail] = useState('');

    const handleRegisterClick = () => setIsActive(true);
    const handleLoginClick = () => setIsActive(false);

    const handleSignupChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setSignupData((prev) => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSignupSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        // Pass the sign-up data as a successful login
        onLoginSuccess({ method: 'signup', data: signupData });
    };

    const handleGoogleLogin = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        // Pass the sign-in (Google) data as a successful login
        onLoginSuccess({ method: 'google', data: { email: signinEmail } });
    };

    return (
        <div className={`container ${isActive ? 'active' : ''}`} id="container">
            {/* Sign Up Form */}
            <div className="form-container sign-up">
                <form onSubmit={handleSignupSubmit}>
                    <h1 style={{ textAlign: 'center' }}>Create Account</h1>
                    <div className="social-icons">
                        {/* Only include Google */}
                        <a href="/Google%20suite.jpg" className="icons">
                            <img
                                src="/Google%20suite.jpg"
                                alt="Google Icon"
                                style={{ width: '24px', height: '24px' }}
                            />
                        </a>
                    </div>
                    <span>Register with E-mail</span>
                    <input
                        type="text"
                        placeholder="Name"
                        name="name"
                        value={signupData.name}
                        onChange={handleSignupChange}
                    />
                    <input
                        type="email"
                        placeholder="Enter E-mail"
                        name="email"
                        value={signupData.email}
                        onChange={handleSignupChange}
                    />
                    <input
                        type="password"
                        placeholder="Enter Password"
                        name="password"
                        value={signupData.password}
                        onChange={handleSignupChange}
                    />
                    <button type="submit">Sign Up</button>
                </form>
            </div>

            {/* Sign In Form (only Google login) */}
            <div className="form-container sign-in">
                <form onSubmit={handleGoogleLogin}>
                    <h1>Sign In</h1>
                    <div className="social-icons">
                        {/* Only include Google */}
                        <a href="/Google%20suite.jpg" className="icons">
                            <img
                                src="/Google%20suite.jpg"
                                alt="Google Icon"
                                style={{ width: '24px', height: '24px' }}
                            />
                        </a>
                    </div>
                    {/* Added an email input so that "anything typed" is passed */}
                    <input
                        type="email"
                        placeholder="Enter E-mail"
                        value={signinEmail}
                        onChange={(e) => setSigninEmail(e.target.value)}
                    />
                    <button type="submit">Sign in</button>
                </form>
            </div>

            {/* Toggle Container for switching forms */}
            <div className="toggle-container">
                <div className="toggle">
                    <div className="toggle-panel toggle-left">
                        <h1>
                            Welcome To <br />Code with Victor
                        </h1>
                        <p>Sign in with your account</p>
                        <button className="hidden" id="login" onClick={handleLoginClick}>
                            Sign In
                        </button>
                    </div>
                    <div className="toggle-panel toggle-right">
                        <h1>Hello There (Tittle)</h1>
                        <p>Sub tittle for logging in</p>
                        <button className="hidden" id="register" onClick={handleRegisterClick}>
                            Sign Up
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
