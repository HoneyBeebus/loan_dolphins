import React from 'react';
import Cookies from 'js-cookie';
import LoginPage from '../pages/LoginPage';


class BasicLoginWrapper extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			loggedIn: false
		};
	}

	componentDidMount() {
		// this login system is super basic, needs to be
		// eventually replaced with real authentication tokens, etc.
	
		const username = Cookies.get("username");
		const password = Cookies.get("password");
	
		if (username !== undefined && password !== undefined) {
			this.checkLogin(username, password);
		}
	}

	checkLogin(username, password) {
		fetch("/login", {
			method: "POST",
			headers: {"Content-Type": "application/json"},
			body: JSON.stringify({
				username: username,
				password: password
			})
		})
		.then(response => response.json()).then(data => {
			if (data.success == true) {
				this.setState({
					loggedIn: true
				});
				Cookies.set("username", username, {expires: 1});
				Cookies.set("password", password, {expires: 1});
				Cookies.set("uid", data.uid, {expires: 1});
				Cookies.set("role", data.role, {expires: 1});
			}
			else alert("Incorrect login!");
		});
	}

	render() {
		if (this.state.loggedIn) return (<>{this.props.children}</>);
		else return <LoginPage onSubmit={(user,pass) => this.checkLogin(user,pass)}/>;
	}
}

export default BasicLoginWrapper;