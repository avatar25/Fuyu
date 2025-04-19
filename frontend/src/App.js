import React from 'react';
import { Routes, Route } from 'react-router-dom';

function Home() {
  return <h1>Home</h1>;
}

function Random() {
  return <h1>Random Page</h1>;
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/random" element={<Random />} />
    </Routes>
  );
}

export default App;