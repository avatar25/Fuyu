// src/App.js

import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import AddData from './pages/AddData';
import SeeData from './pages/SeeData';
import Trends from './pages/Trends';
import Goals from './pages/Goals';

function App() {
  return (
    <div className="app-container">
      <header>
        <h1>Fuyu App</h1>
        <nav>
          <Link className="nav-link" to="/add">Add Expense</Link>
          <Link className="nav-link" to="/view">See Expenses</Link>
          <Link className="nav-link" to="/trends">Trends</Link>
          <Link className="nav-link" to="/goals">Goals</Link>
        </nav>
      </header>
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
