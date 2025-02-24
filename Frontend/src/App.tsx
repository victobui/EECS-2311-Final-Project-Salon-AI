import React, { useState } from 'react';
import Login from './Login';
import Chatbot from './Chatbot';

const App: React.FC = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLoginSuccess = (data: any) => {
    console.log('User logged in:', data);
    setIsAuthenticated(true);
  };

  return (
    <div>
      {isAuthenticated ? (
        <Chatbot />
      ) : (
        <Login onLoginSuccess={handleLoginSuccess} />
      )}
    </div>
  );
};

export default App;