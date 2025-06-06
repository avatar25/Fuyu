import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api';

export const getGoals = async () => {
  const res = await axios.get(`${BASE_URL}/goals/`);
  return res.data;
};

export const addGoal = async (goal) => {
  const res = await axios.post(`${BASE_URL}/goals/`, goal);
  return res.data;
};

export const updateGoal = async (id, goal) => {
  const res = await axios.put(`${BASE_URL}/goals/${id}`, goal);
  return res.data;
};
