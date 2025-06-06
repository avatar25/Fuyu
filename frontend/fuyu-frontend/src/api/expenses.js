// src/api/expenses.js

import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api';

export const getExpenses = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/expenses/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching expenses:", error);
    throw error;
  }
};

export const addExpense = async (expenseData) => {
  try {
    const response = await axios.post(`${BASE_URL}/expenses/`, expenseData);
    return response.data;
  } catch (error) {
    console.error("Error adding expense:", error);
    throw error;
  }
};

export const getMonthlySummary = async () => {
  const res = await axios.get(`${BASE_URL}/expenses/summary/monthly`);
  return res.data;
};

export const getCategorySummary = async () => {
  const res = await axios.get(`${BASE_URL}/expenses/summary/category`);
  return res.data;
};

export const getDailySummary = async () => {
  const res = await axios.get(`${BASE_URL}/expenses/summary/daily`);
  return res.data;
};

