import React from 'react';
import { Grid, FormControl, TextField} from '@material-ui/core';
import Button from '@material-ui/core/Button';
import DataDropdown from '../components/DataDropdown';
import Cookies from 'js-cookie';



class RiskPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            analysisData: this.emptyData
        };
    }

    componentDidMount() {
        if (this.props.location.state && this.props.location.state.analysisData) {
            this.setState({
                analysisData: this.props.location.state.analysisData
            })
        }
    }

    emptyData = {
        lossScenario: '',
        notes: '',
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
            data.uid = Cookies.get("uid");
            this.props.history.push({
                "pathname": "/outcome",
                "state": {
                    analysisData: data
                }
            });
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
                  <h1>Risk Analysis</h1>
                  <Grid item container> 
                    <Grid item xs ={2}/>
                    <Grid item xs = {8}>
                        <Grid container>
                            <Grid item xs={6}>
                                <TextField variant = "outlined" nultiline label="Loss Scenario"
                                    value={this.state.analysisData.lossScenario}
                                    onChange={(e) => this.setInput("lossScenario", e.target.value)}
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField variant = "outlined" multiline label = "Notes"
                                    value={this.state.analysisData.notes}
                                    onChange={(e) => this.setInput("notes", e.target.value)}
                                />
                            </Grid>
                        </Grid>
                        <br></br>
                        <Grid container>
                             <Grid item xs = {6}>Contact Frequency Avoidance</Grid>
                             <Grid item xs = {6}>Probability of Action Deterrence</Grid>
                            <Grid item xs = {6}><FormControl>
                                <DataDropdown
                                    type="ContactFrequency"
                                    label="Inherent"
                                    value={this.state.analysisData.contactFrequencyAvoidanceInherent}
                                    onChange={(e) => this.setInput("contactFrequencyAvoidanceInherent", e.target.value)}
                                />
                                </FormControl>
                                <FormControl>
                                <DataDropdown
                                    type="ContactFrequency"
                                    label="Controls"
                                    value={this.state.analysisData.contactFrequencyAvoidanceControls}
                                    onChange={(e) => this.setInput("contactFrequencyAvoidanceControls", e.target.value)}
                                />
                                </FormControl>
                        </Grid>
                            <Grid item xs = {6}><FormControl>
                                <DataDropdown
                                    type="Probability"
                                    label="Inherent"
                                    value={this.state.analysisData.probabilityOfActionDeterrenceInherent}
                                    onChange={(e) => this.setInput("probabilityOfActionDeterrenceInherent", e.target.value)}
                                />
                                </FormControl>
                                <FormControl>
                                <DataDropdown
                                    type="Probability"
                                    label="Controls"
                                    value={this.state.analysisData.probabilityOfActionDeterrenceControls}
                                    onChange={(e) => this.setInput("probabilityOfActionDeterrenceControls", e.target.value)}
                                />
                                </FormControl>
                                </Grid>
                        <Grid item xs = {6}>Threat Capability</Grid>
                        <Grid item xs = {6}>Resistance Strength Vulnerability</Grid>
                        <Grid item xs = {6}><FormControl>
                                <DataDropdown
                                    type="ThreatCapability"
                                    label="OWASP"
                                    value={this.state.analysisData.threatCapability}
                                    onChange={(e) => this.setInput("threatCapability", e.target.value)}
                                />
                                </FormControl></Grid>
                        <Grid item xs = {6}><FormControl>
                                <DataDropdown
                                    type="ResistanceStrength"
                                    label="Inherent"
                                    value={this.state.analysisData.resistanceStrengthVulnerabilityInherent}
                                    onChange={(e) => this.setInput("resistanceStrengthVulnerabilityInherent", e.target.value)}
                                />
                                </FormControl>
                                <FormControl>
                                <DataDropdown
                                    type="ResistanceStrength"
                                    label="Controls"
                                    value={this.state.analysisData.resistanceStrengthVulnerabilityControls}
                                    onChange={(e) => this.setInput("resistanceStrengthVulnerabilityControls", e.target.value)}
                                />
                                </FormControl>
                                </Grid>
                        <Grid item xs = {6}>Primary Loss Magnitude Responsive</Grid>
                        <Grid item xs = {6}>Secondary Loss Magnitude Responsive</Grid>
                        <Grid item xs = {6}><FormControl>
                                <DataDropdown
                                    type="LossMagnitude"
                                    label="Inherent"
                                    value={this.state.analysisData.primaryLossMagnitudeResponsiveInherent}
                                    onChange={(e) => this.setInput("primaryLossMagnitudeResponsiveInherent", e.target.value)}
                                />
                                </FormControl>
                                <FormControl>
                                <DataDropdown
                                    type="LossMagnitude"
                                    label="Controls"
                                    value={this.state.analysisData.primaryLossMagnitudeResponsiveControls}
                                    onChange={(e) => this.setInput("primaryLossMagnitudeResponsiveControls", e.target.value)}
                                />
                                </FormControl>
                                </Grid>
                        <Grid item xs = {6}><FormControl>
                                <DataDropdown
                                    type="LossMagnitude"
                                    label="Inherent"
                                    value={this.state.analysisData.secondaryLossMagnitudeResponsiveInherent}
                                    onChange={(e) => this.setInput("secondaryLossMagnitudeResponsiveInherent", e.target.value)}
                                />
                                </FormControl>
                                <FormControl>
                                <DataDropdown
                                    type="LossMagnitude"
                                    label="Controls"
                                    value={this.state.analysisData.secondaryLossMagnitudeResponsiveControls}
                                    onChange={(e) => this.setInput("secondaryLossMagnitudeResponsiveControls", e.target.value)}
                                />
                                </FormControl>
                                </Grid>
                        <Grid item xs = {6}></Grid>
                        <Grid item xs = {6}>Secondary Loss Probability</Grid>
                         <Grid item xs = {6}></Grid>
                        <Grid item xs = {6}>
                            <DataDropdown
                                type="Probability"
                                label="Percent %"
                                value={this.state.analysisData.secondaryLossProbability}
                                onChange={(e) => this.setInput("secondaryLossProbability", e.target.value)}
                            />
                        </Grid>
                        <Grid><Button disabled></Button></Grid>
                        </Grid>
                    </Grid>
                        <Grid xs = {4}></Grid>
                         <Grid xs = {2}>
                         <Button variant="contained" onClick={this.reset}>Reset</Button>
                         </Grid>
                         <Grid><Button variant="contained" onClick={this.runAnalysis}>Run Analysis</Button></Grid>
                    </Grid>
              </Grid>
        );
    }
  }
  
  export default RiskPage
