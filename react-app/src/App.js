import React from 'react';
import './App.css';

import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import OutcomePage from './pages/OutcomePage'
import ExamplePage from './pages/ExamplePage'
import MatrixPage from './pages/MatrixPage'
import RiskPage from './pages/RiskPage'
import {Navigation} from './components/navBar'


import {BrowserRouter, Route, Switch} from 'react-router-dom';



function App() {
  return (
    <BrowserRouter>
    <div className="App">

      <h3 className="m-3 d-flex justify-contnet-center"><img src="../public/oportun_logo_circle.png" width="90" height="53"alt="Logo" />
        Oportun
      </h3>
      <Navigation/>
      
      <Switch>
			  <Route path="/" exact component={LoginPage}/>
			  <Route path="/dashboard" exact component={DashboardPage}/>
			  <Route path="/test" exact component={ExamplePage}/>
			  <Route path ="/outcome" exact component={OutcomePage}/>
			  <Route path="/matrix" exact component={MatrixPage}/>
			  <Route path="/risk" exact component={RiskPage}/>
		</Switch>
      
    </div>
    </BrowserRouter>
  );
}

export default App;
