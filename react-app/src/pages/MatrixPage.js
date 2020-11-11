import React from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';

import '@trendmicro/react-sidenav/dist/react-sidenav.css';
import './Matrix.css';


class MatrixPage extends React.Component {
    constructor(props) {
        super(props);
		this.state = {
            open: false,
            source: "overall.png"
		};
    }
    handleChange = (event) => {
        this.setState({source: event.target.value});
    }
        
    handleClose = () => {
        this.setState({open: false});
    }
        
    handleOpen = () => {
        this.setState({open: true});
    }

    render() {
	return (
		
	<div>
		<h1>Documentation</h1>
		<img src={this.state.source} /> 
		<Button onClick={this.handleOpen}>
			Select Matrix
		</Button>
		<div class="formControl">
			<div id="demo-controlled-open-select-label">Matrix</div>
			<Select
				labelId="demo-controlled-open-select-label"
				id="demo-controlled-open-select"
				open={this.state.open}
				onClose={this.handleClose}
				onOpen={this.handleOpen}
				value={this.source}
                onChange={this.handleChange}
			>
				<MenuItem value={"overall.png"}>
					<em>Overall Risk</em>
				</MenuItem>
				<MenuItem value={"primary.png"} >Primary Risk</MenuItem>
				<MenuItem value={"secondary.png"}>Secondary Risk</MenuItem>
				<MenuItem value={"primLoss.png"}>Loss Event Frequency</MenuItem>
				<MenuItem value={"vulnerability.png"}>Vulnerability</MenuItem>
				<MenuItem value={"secLoss.png"}>Secondary Loss Event Frequency</MenuItem>
			</Select>
		</div>
	</div>);
}
}

export default MatrixPage;