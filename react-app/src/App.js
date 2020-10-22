import React from 'react';
import './App.css';

import { Router } from 'react-router-dom';
import Routes from './Routes';
import history from './history';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Router history={history}>
          <Routes />
        </Router>
      </header>
    </div>
  );
}

export default App;
