import React from 'react';
import { Button, TextField } from '@material-ui/core';
import { DataGrid } from '@material-ui/data-grid';
import './DashboardPage.css';

const header = [
	{field: "runDate", headerName: "Date", width: 120},
	{field: "lossScenario", headerName: "Loss Scenario", width: 200},
	{field: "overallResidualRisk", headerName: "Overall Residual Risk", width: 200},
	{field: "potentialLossMagnitude", headerName: "Potential Loss Magnitude", width: 200}
];

// TODO: replace this with data pulled from the database
const testData = [
	{
		id: 0, lossScenario: "abcdefg", runDate: "04-21-2019",
		overallResidualRisk: "Very High",
		potentialLossMagnitude: "$100,000 to $999,999"
	}
];
for (var i = 1; i < 200; i++) {
	testData.push(JSON.parse(JSON.stringify(testData[0])));
	testData[i].id = i;
	testData[i].customer += i;
}

class LoginPage extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			entries: []
		};
	}
	componentDidMount() {
		fetch("/analyses").then(res => res.json()).then(data => {
			let analyses = data.analyses.map(row => {
				row.id = row.AID;
				return row;
			});
			console.log(analyses);
			this.setState({entries: analyses});
		});
	}
	render() {
		return (<div>
			<h1>Dashboard View</h1>
			<span>Recent Entries</span> <TextField type="search" variant="outlined" /> <Button variant="contained">Search</Button>
			<div class="Dashboard-grid">
				<DataGrid id="Dashboard-grid" rows={this.state.entries} columns={header} />
			</div>
		</div>);
	}
}

export default LoginPage;