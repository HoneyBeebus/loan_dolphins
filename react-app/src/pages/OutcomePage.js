import React from 'react';
import ReactDataGrid from 'react-data-grid';
import { Button } from '@material-ui/core';

export default OutcomePage;

//export default function DataGrid() {
  
  const columns = [
    { key: "lossScenario", name: "Loss Scenario" },
    { key: "date", name: "Date" },
    { key: "overallResidualRisk", name: "Overall Residual Risk" },
    { key: "potentialLossMagnitude", name: "Potential Loss Magnitude"}
  ];

  const rows = [
    { lossScenatio: "Ada Lovelace", date: "04-21-2019", overallResidualRisk: "Very High", potentialLossMagnitude: "4" },
  ];

function OutcomePage() {
		return (<div>
			<h1>Outcome</h1>
      // <ReactDataGrid
       // columns={columns}
        //rowGetter={i => rows[i]}
        //rowsCount={3}
      />
      <Button variant="contained" color="primary">Cancel</Button>
      <Button variant="contained" color="primary">Save</Button>
      <img src="tree.png" className="App-header" alt="logo" />

    </div>);
}
