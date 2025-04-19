// src/App.js

import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import AddData from './pages/AddData';
import SeeData from './pages/SeeData';

function App() {
  return (
    <div>
      <h1>Fuyu App</h1>
      <nav style={{ marginBottom: '20px' }}>
        <Link to="/add" style={{ marginRight: '10px' }}>Add Expense</Link>
        <Link to="/view">See Expenses</Link>
      </nav>
      <Routes>
        <Route path="/add" element={<AddData />} />
        <Route path="/view" element={<SeeData />} />
        <Route path="*" element={<div>Welcome! Choose an option above.</div>} />
      </Routes>
    </div>
  );
}

export default App;
