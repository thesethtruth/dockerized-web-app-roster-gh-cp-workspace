import React, { useState } from 'react';
import 'tailwindcss/tailwind.css';
import 'daisyui/dist/full.css';

const App = () => {
  const [roster, setRoster] = useState([
    { name: 'Person 1', comingWeek: '', nextTwoWeeks: '', longTerm: '' },
    { name: 'Person 2', comingWeek: '', nextTwoWeeks: '', longTerm: '' },
    { name: 'Person 3', comingWeek: '', nextTwoWeeks: '', longTerm: '' },
  ]);

  const handleInputChange = (index, field, value) => {
    const newRoster = [...roster];
    newRoster[index][field] = value;
    setRoster(newRoster);
  };

  const addPerson = () => {
    setRoster([...roster, { name: `Person ${roster.length + 1}`, comingWeek: '', nextTwoWeeks: '', longTerm: '' }]);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Roster</h1>
      <table className="table w-full">
        <thead>
          <tr>
            <th>Name</th>
            <th>Coming Week</th>
            <th>Next 2 Weeks</th>
            <th>Long Term</th>
          </tr>
        </thead>
        <tbody>
          {roster.map((person, index) => (
            <tr key={index}>
              <td>{person.name}</td>
              <td>
                <input
                  type="text"
                  value={person.comingWeek}
                  onChange={(e) => handleInputChange(index, 'comingWeek', e.target.value)}
                  className="input input-bordered w-full"
                />
              </td>
              <td>
                <input
                  type="text"
                  value={person.nextTwoWeeks}
                  onChange={(e) => handleInputChange(index, 'nextTwoWeeks', e.target.value)}
                  className="input input-bordered w-full"
                />
              </td>
              <td>
                <input
                  type="text"
                  value={person.longTerm}
                  onChange={(e) => handleInputChange(index, 'longTerm', e.target.value)}
                  className="input input-bordered w-full"
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={addPerson} className="btn btn-primary mt-4">Add Person</button>
    </div>
  );
};

export default App;
