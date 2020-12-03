import React from 'react';
import './ColorText.css'

function ColorText(props) {
	let valueNames = ["1 - Very Low", "2 - Low", "3 - Medium", "4 - High", "5 - Very High"];
	let text = valueNames[props.value - 1];
	let colorClass = "ColorText color" + props.value;
	return <span className={colorClass}>{text}</span>;
}

export default ColorText;