import React from 'react';
import { Button, TextField, Paper, TableContainer, Table, TableHead, TableBody, TableRow, TableCell } from '@material-ui/core';
import DataTree from '../components/DataTree';

class OutcomePage extends React.Component {
  constructor(props) {
    super(props);
		this.state = {

		};
  }
  render() {
		return (<div>
			<h1>Outcome</h1>
			<br></br>
			<h4>Does the following look correct?</h4>
			<hr></hr>
			<br></br>
			<DataTree/>
			<br></br>
			<Button variant="contained" color="primary" spacing="1">Yes</Button>
			<br></br>
			<br></br>
		  	<Button variant="outlined" color="primary" spacing="1">No</Button>

		</div>
		);
  	}
}

export default OutcomePage