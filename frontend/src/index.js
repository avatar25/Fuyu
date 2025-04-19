import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';

// Find the div with id "root" in your HTML file
const container = document.getElementById('root');

// Tell React where to mount your React App
const root = createRoot(container);

// Render your App component inside this root
root.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>
);