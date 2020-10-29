import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';

import SideNav, { Toggle, Nav, NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';
import '@trendmicro/react-sidenav/dist/react-sidenav.css';
import './Matrix.css';

export default MatrixPage;
const useStyles = makeStyles((theme) => ({
	button: {
		display: 'block',
		marginTop: theme.spacing(2),
	},
	formControl: {
		margin: theme.spacing(1),
		minWidth: 120,
	},
}));

function MatrixPage(){
	
	const classes = useStyles();
	const [age, setAge] = React.useState('');
	const [open, setOpen] = React.useState(false);
		
	const handleChange = (event) => {
		setAge(event.target.value);
	};
		
	const handleClose = () => {
		setOpen(false);
	};
		
	const handleOpen = () => {
		setOpen(true);
	};

	return (
		
	<div>
		<SideNav
    			onSelect={(selected) => {
        				// Add your code here
    			}}
			>
    			<SideNav.Toggle />
    			<SideNav.Nav defaultSelected="home">
        			<NavItem eventKey="home">
            			<NavIcon>
                			<i className="fa fa-fw fa-home" style={{ fontSize: '1.75em' }} />
            			</NavIcon>
            			<NavText>
                			Home
            			</NavText>
        			</NavItem>
        			<NavItem eventKey="charts">
            			<NavIcon>
                			<i className="fa fa-fw fa-line-chart" style={{ fontSize: '1.75em' }} />
            			</NavIcon>
            			<NavText>
                			Charts
            			</NavText>
            		<NavItem eventKey="charts/linechart">
                		<NavText>
                    		Line Chart
                		</NavText>
            		</NavItem>
            		<NavItem eventKey="charts/barchart">
                		<NavText>
                    		Bar Chart
                		</NavText>
            		</NavItem>
        		</NavItem>
    		</SideNav.Nav>
		</SideNav>
		<h1>Documentation</h1>
		<img src="matrix1.png"  />
		<Button className={classes.button} onClick={handleOpen}>
			Select Matrix
		</Button>
		<FormControl className={classes.formControl}>
			<InputLabel id="demo-controlled-open-select-label">Matrix</InputLabel>
			<Select
				labelId="demo-controlled-open-select-label"
				id="demo-controlled-open-select"
				open={open}
				onClose={handleClose}
				onOpen={handleOpen}
				value={age}
				onChange={handleChange}
			>
				<MenuItem value="">
					<em>Overall Risk</em>
				</MenuItem>
				<MenuItem value={10}>Primary Risk</MenuItem>
				<MenuItem value={20}>Secondary Risk</MenuItem>
				<MenuItem value={30}>Loss Event Frequency</MenuItem>
				<MenuItem value={40}>Vulnerabilty</MenuItem>
				<MenuItem value={50}>Secondary Loss Event Frequency</MenuItem>
				<MenuItem value={60}>Overall Risk</MenuItem>
			</Select>
		</FormControl>
	</div>);
}

