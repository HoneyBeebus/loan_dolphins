import React from 'react';
import { Button, TextField, Paper, TableContainer, Table, TableHead, TableBody, TableRow, TableCell } from '@material-ui/core';
import DataTree from '../components/DataTree';

class ViewPage extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			AID: props.match.params.AID,
			data: []
		};
	}

	componentDidMount() {
		fetch("/getAnalysis/" + this.state.AID).then(response => response.json()).then(data => {
			this.setState({
				data: data
			});
		});
	}

	render() {
		return (<div>
			<br></br>
			<br></br>
			<h1>Outcome of Analysis</h1>
			<br></br>
			<hr></hr>
			<DataTree data={this.state.data}/>
		</div>);
	}
}

export default ViewPage;