// src/pages/SeeData.js

import React, { useEffect, useState } from 'react';
import { getExpenses } from '../api/expenses';

function SeeData() {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    const fetchExpenses = async () => {
      try {
        const data = await getExpenses();
        setExpenses(data);
      } catch (error) {
        alert("Error fetching expenses");
      }
    };
    fetchExpenses();
  }, []);

  return (
    <div className="form">
      <h1>Expenses Summary</h1>
      <ul>
        {expenses.map((expense) => (
          <li key={expense.id}>
            {expense.category}: ${expense.amount} - {expense.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SeeData;
