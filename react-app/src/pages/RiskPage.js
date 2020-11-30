import React from 'react';
import { Grid, ButtonGroup, Select, MenuItem, FormControl, InputLabel, makeStyles, TextField} from '@material-ui/core';
import Button from '@material-ui/core/Button';



class RiskPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            analysisData: this.emptyData
        };
    }

    emptyData = {
        contactFrequencyAvoidanceInherent: '',
        contactFrequencyAvoidanceControls: '',
        probabilityOfActionDeterrenceInherent: '',
        probabilityOfActionDeterrenceControls: '',
        threatCapability: '',
        resistanceStrengthVulnerabilityInherent: '',
        resistanceStrengthVulnerabilityControls: '',
        primaryLossMagnitudeResponsiveInherent: '',
        primaryLossMagnitudeResponsiveControls: '',
        secondaryLossMagnitudeResponsiveInherent: '',
        secondaryLossMagnitudeResponsiveControls: '',
        secondaryLossProbability: ''
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

    setInput(name, value) {
        let data = Object.assign({},this.state.analysisData);
        data[name] = value;
        this.setState({analysisData: data});
        console.log(data)
    }

    reset = () => {
        this.setState({
            analysisData: this.emptyData
        })
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
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.contactFrequencyAvoidanceInherent}
                                    onChange = {(e) => this.setInput("contactFrequencyAvoidanceInherent", e.target.value)}
                                >
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.contactFrequencyAvoidanceControls}
                                    onChange = {(e) => this.setInput("contactFrequencyAvoidanceControls", e.target.value)}
                                >
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
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.probabilityOfActionDeterrenceInherent}
                                    onChange = {(e) => this.setInput("probabilityOfActionDeterrenceInherent", e.target.value)}
                                >
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.probabilityOfActionDeterrenceControls}
                                    onChange = {(e) => this.setInput("ProbabilityOfActionDeterrenceControls", e.target.value)}
                                >
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
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.threatCapability}
                                    onChange = {(e) => this.setInput("threatCapability", e.target.value)}
                                >
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl></Grid>
                        <Grid item xs = {6}><FormControl>
                                    <InputLabel>Inherent</InputLabel>
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.resistanceStrengthVulnerabilityInherent}
                                    onChange = {(e) => this.setInput("resistanceStrengthVulnerabilityInherent", e.target.value)}
                                >
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.resistanceStrengthVulnerabilityControls}
                                    onChange = {(e) => this.setInput("resistanceStrengthVulnerabilityControls", e.target.value)}
                                >
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
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.primaryLossMagnitudeResponsiveInherent}
                                    onChange = {(e) => this.setInput("primaryLossMagnitudeResponsiveInherent", e.target.value)}
                                >
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.primaryLossMagnitudeResponsiveControls}
                                    onChange = {(e) => this.setInput("primaryLossMagnitudeResponsiveControls", e.target.value)}
                                >
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
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.secondaryLossMagnitudeResponsiveInherent}
                                    onChange = {(e) => this.setInput("secondaryLossMagnitudeResponsiveInherent", e.target.value)}
                                >
                                <MenuItem value = {1}>one</MenuItem>
                                <MenuItem value = {2}>two</MenuItem>
                                <MenuItem value = {3}>three</MenuItem>
                                <MenuItem value = {4}>four</MenuItem>
                                <MenuItem value = {5}>five</MenuItem>
                                </Select>
                                </FormControl>
                                <FormControl>
                                <InputLabel>Controls</InputLabel>
                                <Select variant = "outlined"
                                    value = {this.state.analysisData.secondaryLossMagnitudeResponsiveControls}
                                    onChange = {(e) => this.setInput("secondaryLossMagnitudeResponsiveControls", e.target.value)}
                                >
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
                        <Grid item xs = {6}>
                            <TextField id="outlined-basic" variant="outlined"
                                label="Percent %"
                                type="number"
                                value={this.state.analysisData.secondaryLossProbability}
                                onChange = {(e) => this.setInput("secondaryLossProbability", Math.min(Math.max(0,e.target.value),100))}
                            />
                        </Grid>
                        <Grid item xs = {3}><Button variant="contained" onClick={this.reset}>Reset</Button></Grid>
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
