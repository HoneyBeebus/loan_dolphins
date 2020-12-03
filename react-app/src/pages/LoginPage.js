import React from 'react';
import { Button, TextField } from '@material-ui/core';

class LoginPage extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			username: null,
			password: null
		}
	}

	login = () => {
		if (this.state.username && this.state.password) {
			this.props.onSubmit(this.state.username, this.state.password);
		}
	}

	render() {
		return (<div>
			<h1>Login</h1>
			<TextField label="username" onChange={e => this.setState({username: e.target.value})}/>
			<TextField type="password" label="password" onChange={e => this.setState({password: e.target.value})}/>
			<Button variant="contained" color="primary" onClick={this.login}>Login</Button>
		</div>);
	}
}

export default LoginPage;