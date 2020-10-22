import React from 'react';
import { Button, TextField } from '@material-ui/core';

class LoginPage extends React.Component {
	render() {
		return (<div>
			<h1>Login</h1>
			<TextField label="username"/>
			<TextField type="password" label="password"/>
			<Button variant="contained" color="primary">Login</Button>
		</div>);
	}
}

export default LoginPage;