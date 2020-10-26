import React from 'react';
import { Button, TextField, Paper, TableContainer, Table, TableHead, TableBody, TableRow, TableCell } from '@material-ui/core';

class OutcomePage extends React.Component {
  constructor(props) {
    super(props);
		this.state = {

		};
  }
  render() {
		return (<div>
			<h1>Outcome</h1>
      <TableContainer component={Paper}>
				<Table>
					<TableHead>
						<TableRow>
							<TableCell>Customer</TableCell>
							<TableCell>Date of Request</TableCell>
							<TableCell>Overall Residual Risk</TableCell>
              <TableCell>Potential Loss Magnitude</TableCell>
						</TableRow>
					</TableHead>
					<TableBody>
						<TableRow>
							<TableCell>Ada Lovelace</TableCell>
							<TableCell>04-21-2019</TableCell>
							<TableCell>Very High</TableCell>
              <TableCell>4</TableCell>
						</TableRow>
						<TableRow>
							<TableCell>Ada Lovelace</TableCell>
							<TableCell>04-21-2019</TableCell>
							<TableCell>Very High</TableCell>
              <TableCell>4</TableCell>
						</TableRow>
					</TableBody>
				</Table>
			</TableContainer>
      <Button variant="contained" color="primary">Cancel</Button>
      <Button variant="contained" color="primary">Save</Button>
      <img src="tree.png" className="App-header" alt="logo" />

    </div>);
  }
}

export default OutcomePage