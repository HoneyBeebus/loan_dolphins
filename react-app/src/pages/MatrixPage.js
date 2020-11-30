import React from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';
import './Matrix.css';
import Dropdown from '../components/Dropdown';

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

    render() {
	return (
		
	<div>
		<h1>Documentation</h1>
		<img src={this.state.source} />
		<Dropdown label="Matrix" onChange={this.handleChange}>
			<MenuItem value={"overall.png"}>
				<em>Overall Risk</em>
			</MenuItem>
			<MenuItem value={"primary.png"} >Primary Risk</MenuItem>
			<MenuItem value={"secondary.png"}>Secondary Risk</MenuItem>
			<MenuItem value={"primLoss.png"}>Loss Event Frequency</MenuItem>
			<MenuItem value={"vulnerability.png"}>Vulnerability</MenuItem>
			<MenuItem value={"secLoss.png"}>Secondary Loss Event Frequency</MenuItem>
		</Dropdown>
	</div>);
}
}

export default MatrixPage;