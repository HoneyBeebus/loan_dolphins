import React from 'react';
import {MenuItem} from '@material-ui/core';
import Dropdown from './Dropdown';
import DataKey from "../DataKey.json";

class DropdownItems extends React.Component {
	render() {
		let key = DataKey[this.props.type];
		if (!key) key = {
			"1": "1 - Very Low",
			"2": "2 - Low",
			"3": "3 - Medium",
			"4": "4 - High",
			"5": "5 - Very High"
		}
		return (<Dropdown
			label={this.props.label}
			value={this.props.value}
			onChange={this.props.onChange}
		>
			<MenuItem value={1}>{key["1"]}</MenuItem>
			<MenuItem value={2}>{key["2"]}</MenuItem>
			<MenuItem value={3}>{key["3"]}</MenuItem>
			<MenuItem value={4}>{key["4"]}</MenuItem>
			<MenuItem value={5}>{key["5"]}</MenuItem>
		</Dropdown>);
	}
}

export default DropdownItems;