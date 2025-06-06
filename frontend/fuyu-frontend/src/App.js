// src/App.js

import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import AddData from './pages/AddData';
import SeeData from './pages/SeeData';
import Trends from './pages/Trends';
import Goals from './pages/Goals';

function App() {
  return (
    <div>
      <h1>Fuyu App</h1>
      <nav style={{ marginBottom: '20px' }}>
        <Link to="/add" style={{ marginRight: '10px' }}>Add Expense</Link>
        <Link to="/view" style={{ marginRight: '10px' }}>See Expenses</Link>
        <Link to="/trends" style={{ marginRight: '10px' }}>Trends</Link>
        <Link to="/goals">Goals</Link>
      </nav>
      <Routes>
        <Route path="/add" element={<AddData />} />
        <Route path="/view" element={<SeeData />} />
        <Route path="/trends" element={<Trends />} />
        <Route path="/goals" element={<Goals />} />
        <Route path="*" element={<div>Welcome! Choose an option above.</div>} />
      </Routes>
    </div>
  );
}

export default App;
