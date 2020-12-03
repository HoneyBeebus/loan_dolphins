import React from 'react';
import './App.css';

import DashboardPage from './pages/DashboardPage'
import OutcomePage from './pages/OutcomePage'
import ExamplePage from './pages/ExamplePage'
import MatrixPage from './pages/MatrixPage'
import RiskPage from './pages/RiskPage'
import {Navigation} from './components/navBar'

import {BrowserRouter, Route, Switch} from 'react-router-dom';
import BasicLoginWrapper from './components/BasicLoginWrapper'

import Backdrop from './components/Backdrop';

function App() {
  return (
    <BrowserRouter>
    <div className="App">
			<Backdrop />
      <BasicLoginWrapper>
        <Navigation/>
        <Switch>
          <Route path="/" exact component={RiskPage}/>
          <Route path="/dashboard" exact component={DashboardPage}/>
          <Route path="/test" exact component={ExamplePage}/>
          <Route path ="/outcome" exact component={OutcomePage}/>
          <Route path="/matrix" exact component={MatrixPage}/>
          <Route path="/risk" exact component={RiskPage}/>
        </Switch>
      </BasicLoginWrapper>
    </div>
    </BrowserRouter>
  );
}

export default App;
