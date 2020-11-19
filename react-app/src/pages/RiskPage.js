import React from 'react';
import { Grid, ButtonGroup, Select, MenuItem, FormControl, InputLabel, makeStyles, TextField} from '@material-ui/core';
import Button from '@material-ui/core/Button';



class RiskPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            analysisData: {
                contactFrequencyAvoidanceInherent: 1,
                contactFrequencyAvoidanceControls: 1,
                probabilityOfActionDeterrenceInherent: 1,
                probabilityOfActionDeterrenceControls: 1,
                threatCapability: 1,
                resistanceStrengthVulnerabilityInherent: 1,
                resistanceStrengthVulnerabilityControls: 1,
                primaryLossMagnitudeResponsiveInherent: 1,
                primaryLossMagnitudeResponsiveControls: 1,
                secondaryLossMagnitudeResponsiveInherent: 1,
                secondaryLossMagnitudeResponsiveControls: 1,
                secondaryLossProbability: 1
            }
        };
    } 

    runAnalysis = () => {
        // send a POST request to the /runAnalysis endpoint with the analysis data
        fetch("/runAnalysis", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(this.state.analysisData)
        })
        .then(response => response.json()).then(data => {
            // print the response from the server
            console.log(data)
        });
    }

    render() {
          return (
              <Grid container direction = "column">
                  <Grid item>Risk Analysis</Grid>
                  <Grid item container> 
                    <Grid item xs ={2}/>
                    <Grid item xs = {8}>
                        <Grid container>
                             <Grid item xs = {6}>Contact Frequency Avoidance</Grid>
                             <Grid item xs = {6}>Probability of Action Deterrence</Grid>
                            <Grid item xs = {6}><FormControl>
                                    <InputLabel>Inherent</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Residual</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                        </Grid>
                            <Grid item xs = {6}><FormControl>
                                    <InputLabel>Inherent</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Residual</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl></Grid>
                        <Grid item xs = {6}>Threat Capability</Grid>
                        <Grid item xs = {6}>Resistance Strength Vulnerability</Grid>
                        <Grid item xs = {6}><FormControl>
                                <InputLabel>OWASP</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl></Grid>
                        <Grid item xs = {6}><FormControl>
                                    <InputLabel>Inherent</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Residual</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl></Grid>
                        <Grid item xs = {6}>Primary Loss Magnitude Responsive</Grid>
                        <Grid item xs = {6}>Secondary Loss Magnitude Responsive</Grid>
                        <Grid item xs = {6}><FormControl>
                                    <InputLabel>Inherent</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Residual</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl></Grid>
                        <Grid item xs = {6}><FormControl>
                                    <InputLabel>Inherent</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Residual</InputLabel>
                                <Select variant = "outlined">
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl></Grid>
                        <Grid item xs = {6}>Secondary Loss Probability</Grid>
                        <Grid item xs = {6}></Grid>
                        <Grid item xs = {6}><TextField id="outlined-basic" label="Percent %" variant="outlined" /></Grid>
                        <Grid item xs = {3}><Button variant="contained">Reset</Button></Grid>
                        <Grid item xs ={3}><Button variant="contained" onClick={this.runAnalysis}>Run Analysis</Button></Grid>
                        </Grid>
                    </Grid>
                    <Grid item xs ={2}/>
                    </Grid>
              </Grid>
        );
    }
  }
  
  export default RiskPage
