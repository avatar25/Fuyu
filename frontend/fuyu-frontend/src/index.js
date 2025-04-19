import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';

const container = document.getElementById('root');
if (!container) {
  throw new Error("Root container not found. Make sure there is a div with id='root' in your index.html.");
}
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>
);