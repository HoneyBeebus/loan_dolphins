import React from 'react';
import { Route, Switch, Router } from 'react-router-dom';

// Pages
import LoginPage from './pages/LoginPage';
import ExamplePage from './pages/ExamplePage';
import OutcomePage from './pages/OutcomePage';
import history from './history';


function Routes() {
	return (
		<Switch>
			<Route path="/" exact component={LoginPage}/>
			<Route path="/test" exact component={ExamplePage}/>
			<Route path ="/outcome" exact component={OutcomePage}/>
		</Switch>
	);
}

export default Routes;