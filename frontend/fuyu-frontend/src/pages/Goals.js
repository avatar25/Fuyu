import React, { useEffect, useState } from 'react';
import { getGoals, addGoal } from '../api/goals';

function Goals() {
  const [goals, setGoals] = useState([]);
  const [name, setName] = useState('');
  const [target, setTarget] = useState('');
  const [date, setDate] = useState('');

  useEffect(() => {
    load();
  }, []);

  const load = async () => {
    setGoals(await getGoals());
  };

  const submit = async e => {
    e.preventDefault();
    await addGoal({name, target_amount: parseFloat(target), target_date: date, saved_amount:0});
    setName('');
    setTarget('');
    setDate('');
    load();
  };

  return (
    <div>
      <h2>Savings Goals</h2>
      <form onSubmit={submit}>
        <input placeholder="Name" value={name} onChange={e=>setName(e.target.value)} />
        <input placeholder="Target" type="number" value={target} onChange={e=>setTarget(e.target.value)} />
        <input type="date" value={date} onChange={e=>setDate(e.target.value)} />
        <button type="submit">Add Goal</button>
      </form>
      <ul>
        {goals.map(g => {
          const pct = (g.saved_amount / g.target_amount) * 100;
          return (
            <li key={g.id}>
              {g.name}: {g.saved_amount}/{g.target_amount}
              <div style={{background:'#eee', width:'200px'}}>
                <div style={{width:`${pct}%`, background:'green', color:'white'}}>{pct.toFixed(0)}%</div>
              </div>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default Goals;
