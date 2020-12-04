import React from 'react';
import { Button, TextField } from '@material-ui/core';
import { DataGrid } from '@material-ui/data-grid';
import './DashboardPage.css';


function ViewButton(props) {
	return (
		<Button
			variant="contained" color="primary"
			onClick={e => props.onClick(props.value)}
		>
			View
		</Button>
	);
}

class DashboardPage extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			entries: []
		};
	}

	header = [
		{field: "lossScenario", headerName: "Loss Scenario", width: 200},
		{field: "analyst", headerName: "Analyst", width: 120},
		{field: "runDate", headerName: "Date", width: 120},
		{field: "link", headerName: "View Tree", width: 120,
		renderCell: params => {
			return <ViewButton value={params.value} onClick={this.viewTree}/>
		}},
		{field: "overallRiskResidual", headerName: "Overall Residual Risk", width: 200},
		{field: "primaryRiskResidual", headerName: "Primary Residual Risk", width: 200},
		{field: "secondaryRiskResidual", headerName: "Secondary Residual Risk", width: 200},
		{field: "potentialLossMagnitude", headerName: "Potential Loss Magnitude", width: 200},
		{field: "primaryLossMagnitudeResponsiveResidual", headerName: "Primary Loss Magnitude", width: 200},
		{field: "secondaryLossMagnitudeResponsiveResidual", headerName: "Secondary Loss Magnitude", width: 220}
	];

	componentDidMount() {
		fetch("/getAllAnalyses").then(res => res.json()).then(data => {
			let analyses = data.analyses.map(row => {
				// For each row, copy the analysis ID to the "id" property
				// Since DataGrid requires each row to have "id"
				row.id = row.AID;
				// Also calculate potential loss magnitude
				row.potentialLossMagnitude = row.primaryLossMagnitudeResponsiveResidual + row.secondaryLossMagnitudeResponsiveResidual;
				// and a value for the link
				row.link = "/view/" + row.AID;
				return row;
			});
			console.log(analyses);
			this.setState({entries: analyses});
		});
	}

	viewTree = (link) => {
		this.props.history.push(link);
	}

	render() {
		return (<div>
			<h1>Dashboard View</h1>
			{/* <span>Recent Entries</span> <TextField type="search" variant="outlined" /> <Button variant="contained">Search</Button> */}
			<div class="Dashboard-grid">
				<DataGrid id="Dashboard-grid" rows={this.state.entries} columns={this.header} />
			</div>
		</div>);
	}
}

export default DashboardPage;