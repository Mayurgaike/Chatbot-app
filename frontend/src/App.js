import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import Login from './components/Login';
import './App.css';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div className="App">
      {isLoggedIn ? <ChatWindow /> : <Login onLogin={() => setIsLoggedIn(true)} />}
    </div>
  );
}

export default App;
