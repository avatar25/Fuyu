// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AddData from './pages/AddData';
import SeeData from './pages/SeeData';

function App() {
  return (
    <Router>
      <div>
        <h1>Fuyu App</h1>
        <Routes>
          <Route path="/add" element={<AddData />} />
          <Route path="/view" element={<SeeData />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
