import './App.css';
import React from 'react';
import CalendarComponent from "./CalendarComponent";

function App() {
  return (
      <div className="App">
        {/* CalendarComponent 호출*/}
        <div style={{width: '60%', height: '500px', margin: '10px auto'}}>
          <CalendarComponent/>
        </div>
      </div>
  );
}

export default App;
