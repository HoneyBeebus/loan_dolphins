import React from 'react';
import { Button, TextField, Paper, TableContainer, Table, TableHead, TableBody, TableRow, TableCell } from '@material-ui/core';

class LoginPage extends React.Component {
	constructor(props) {
		super(props);
		this.state = {

		};
	}
	render() {
		return (<div>
			<h1>Dashboard View</h1>
			<span>Recent Entries</span> <TextField type="search" variant="outlined" /> <Button variant="contained">Search</Button>
			<TableContainer component={Paper}>
				<Table>
					<TableHead>
						<TableRow>
							<TableCell>Customer</TableCell>
							<TableCell>Date of Request</TableCell>
							<TableCell>Risk</TableCell>
						</TableRow>
					</TableHead>
					<TableBody>
						<TableRow>
							<TableCell>Ada Lovelace</TableCell>
							<TableCell>04-21-2019</TableCell>
							<TableCell>Very High</TableCell>
						</TableRow>
						<TableRow>
							<TableCell>Ada Lovelace</TableCell>
							<TableCell>04-21-2019</TableCell>
							<TableCell>Very High</TableCell>
						</TableRow>
					</TableBody>
				</Table>
			</TableContainer>
		</div>);
	}
}

export default LoginPage;