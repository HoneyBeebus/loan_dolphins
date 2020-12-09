import React from 'react';
import {MenuItem} from '@material-ui/core';
import DataKey from "../DataKey.json";

class Data extends React.Component {
	render() {
		let key = DataKey[this.props.type];
		if (!key) key = {
			"1": "1 - Very Low",
			"2": "2 - Low",
			"3": "3 - Medium",
			"4": "4 - High",
			"5": "5 - Very High"
		}
		let style = {};
		let colors = [null, "green", "lime", "yellow", "orange", "red"];
		if (this.props.color) {
			style.color = colors[this.props.value];
			style.fontWeight = "bold";
		}
		if (this.props.background) {
			style.backgroundColor = colors[this.props.value];
		}
		return (<span style={style}>{key[this.props.value]}</span>)
	}
}

export default Data;