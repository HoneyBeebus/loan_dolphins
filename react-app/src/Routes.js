import React from 'react';
import { Route, Switch } from 'react-router-dom';

// Pages
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import ExamplePage from './pages/ExamplePage';
import OutcomePage from './pages/OutcomePage';
import MatrixPage from './pages/MatrixPage';
import RiskPage from './pages/RiskPage';

function Routes() {
	return (
		<Switch>
			<Route path="/" exact component={LoginPage}/>
			<Route path="/dashboard" exact component={DashboardPage}/>
			<Route path="/test" exact component={ExamplePage}/>
			<Route path ="/outcome" exact component={OutcomePage}/>
			<Route path="/matrix" exact component={MatrixPage}/>
			<Route path="/risk" exact component={RiskPage}/>
		</Switch>
	);
}

export default Routes;
