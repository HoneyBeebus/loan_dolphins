import React from 'react';
import './ColorText.css'

function ColorText(props) {
	let valueNames = ["1 - VL", "2 - L", "3 - M", "4 - H", "5 - VH"];
	let text = valueNames[props.value - 1];
	let colorClass = "ColorText color" + props.value;
	return <span className={colorClass}>{text}</span>;
}

export default ColorText;