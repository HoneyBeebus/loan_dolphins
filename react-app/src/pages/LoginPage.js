import React from 'react';
import { Button, TextField } from '@material-ui/core';
import Lgrid from '../components/Lgrid';
import Grid from '@material-ui/core/Grid';
import Divider from '@material-ui/core/Divider';
import Backdrop from '../components/Backdrop';

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
		return (
		<div>
			<Backdrop />
			<Lgrid>
				<Grid item xs={4}>
					<h1>Login</h1>
					<Divider />
					<TextField label="username" onChange={e => this.setState({username: e.target.value})}/>
					<TextField type="password" label="password" onChange={e => this.setState({password: e.target.value})}/>
					<Button variant="contained" color="primary" onClick={this.login}>Login</Button>
				</Grid>
			</Lgrid>
		</div>);
	}
}

export default LoginPage;