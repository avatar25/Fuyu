import React, { useEffect, useState } from 'react';
import { Bar, Pie } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, ArcElement } from 'chart.js';
import { getMonthlySummary, getCategorySummary, getDailySummary } from '../api/expenses';

ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement);

function Trends() {
  const [monthly, setMonthly] = useState({});
  const [category, setCategory] = useState({});
  const [daily, setDaily] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      setMonthly(await getMonthlySummary());
      setCategory(await getCategorySummary());
      setDaily(await getDailySummary());
    };
    fetchData();
  }, []);

  const monthlyData = {
    labels: Object.keys(monthly),
    datasets: [{ label: 'Total', data: Object.values(monthly), backgroundColor: 'rgba(75,192,192,0.4)' }]
  };

  const categoryData = {
    labels: Object.keys(category),
    datasets: [{ data: Object.values(category), backgroundColor: ['#FF6384','#36A2EB','#FFCE56','#4BC0C0'] }]
  };

  return (
    <div>
      <h2>Spending Trends</h2>
      <div style={{ width:'400px', margin:'20px' }}>
        <Bar data={monthlyData} />
      </div>
      <div style={{ width:'400px', margin:'20px' }}>
        <Pie data={categoryData} />
      </div>
      <pre>{JSON.stringify(daily, null, 2)}</pre>
    </div>
  );
}

export default Trends;
