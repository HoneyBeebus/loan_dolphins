import React from 'react';
import { Button, TextField, Paper, TableContainer, Table, TableHead, TableBody, TableRow, TableCell } from '@material-ui/core';
import DataTree from '../components/DataTree';

class OutcomePage extends React.Component {
  constructor(props) {
    super(props);
		this.state = {

		};
  }

  submit = () => {
	fetch("/commit", {
		method: "POST",
		headers: {"Content-Type": "application/json"},
		body: JSON.stringify(this.props.location.state.analysisData)
	})
	.then(response => response.json()).then(data => {
		if (data.success) {
			this.props.history.push("/risk");
		}
	});
  }

  cancel = () => {
	  this.props.history.push({
		  "pathname": "/risk",
		  "state": {
			  analysisData: this.props.location.state.analysisData
		  }
	  });
  }


  render() {
	  let data = {}
	  if (this.props.location.state && this.props.location.state.analysisData) {
		  data = this.props.location.state.analysisData
	  }
		return (<div>
			<br></br>
			<br></br>
			<h1>Outcome of Analysis</h1>
			<br></br>
			<hr></hr>
			<DataTree data={data}/>
			<hr></hr>
			<h2>Would you like to save this result?</h2>
			<br></br>
			<Button variant="contained" color="primary" spacing="1" onClick={this.submit}>Yes</Button>
			<br></br>
			<br></br>
		  	<Button variant="outlined" color="primary" spacing="1" onClick={this.cancel}>No</Button>

		</div>
		);
  	}
}

export default OutcomePage