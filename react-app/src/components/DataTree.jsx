import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Data from './Data';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: "white",
    backgroundColor: "#343A40",
  },
}));

export default function FullWidthGrid(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h3>Overall Risk</h3>Inherent: <Data color value={props.data.overallRiskInherent} /><br></br>Residual: <Data color value={props.data.overallRiskResidual} /></Paper>
        </Grid>
        <Grid item xs={12} sm={6} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h4>Primary Risk</h4>Inherent: <Data color value={props.data.primaryRiskInherent} /><br></br>Residual: <Data color value={props.data.primaryRiskResidual} /></Paper>
        </Grid>
        <Grid item xs={12} sm={6} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h4>Secondary Risk</h4>Inherent: <Data color value={props.data.secondaryRiskInherent} /><br></br>Residual: <Data color value={props.data.secondaryRiskResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Primary Loss Event Frequency</h5>Inherent: <Data color value={props.data.primaryLossEventFrequencyInherent} /><br></br><br></br>Residual: <Data color value={props.data.primaryLossEventFrequencyResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Primary Loss Magnitude</h5>Inherent: <Data color type="LossMagnitude" value={props.data.primaryLossMagnitudeResponsiveInherent} /><br></br>Controls: <Data color type="LossMagnitude" value={props.data.primaryLossMagnitudeResponsiveControls} /><br></br>Residual: <Data color type="LossMagnitude" value={props.data.primaryLossMagnitudeResponsiveResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Secondary Loss Magnitude</h5>Inherent: <Data color type="LossMagnitude" value={props.data.secondaryLossMagnitudeResponsiveInherent} /><br></br>Controls: <Data color type="LossMagnitude" value={props.data.secondaryLossMagnitudeResponsiveControls} /><br></br>Residual: <Data color type="LossMagnitude" value={props.data.secondaryLossMagnitudeResponsiveResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Secondary Loss Event Frequency</h5>Inherent: <Data color value={props.data.secondaryLossEventFrequencyInherent} /><br></br><br></br>Residual: <Data color value={props.data.secondaryLossEventFrequencyResidual} /></Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Threat Event Frequency</h6>Inherent: <Data color value={props.data.threatEventFrequencyInherent} /><br></br>Residual: <Data color value={props.data.threatEventFrequencyResidual} /></Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Vulnerability</h6>Inherent: <Data color value={props.data.vulnerabilityInherent} /><br></br>Residual: <Data color value={props.data.vulnerabilityResidual} /></Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Secondary Loss Probability</h6><br></br><Data color type="Probability" value={props.data.secondaryLossProbability} /></Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Contact Frequency Avoidance</h6>Inherent: <Data color type="ContactFrequency" value={props.data.contactFrequencyAvoidanceInherent} /><br></br>Controls: <Data color type="ContactFrequency" value={props.data.contactFrequencyAvoidanceControls} /><br></br>Residual: <Data color type="ContactFrequency" value={props.data.contactFrequencyAvoidanceResidual} /></Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Threat Capability</h6><br></br><br></br>OWASP: <Data color type="ThreatCapability" value={props.data.threatCapability} /></Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Probability of Action Deterrence</h6>Inherent: <Data color type="Probability" value={props.data.probabilityOfActionDeterrenceInherent} /><br></br>Controls: <Data color type="Probability" value={props.data.probabilityOfActionDeterrenceControls} /><br></br>Residual: <Data color type="Probability" value={props.data.probabilityOfActionDeterrenceResidual} /></Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Resistance Strength Vulnerability</h6>Inherent: <Data type="ResistanceStrength" value={props.data.resistanceStrengthVulnerabilityInherent} /><br></br>Controls: <Data type="ResistanceStrength" value={props.data.resistanceStrengthVulnerabilityControls} /><br></br>Residual: <Data type="ResistanceStrength" value={props.data.resistanceStrengthVulnerabilityResidual} /></Paper>
        </Grid>
        <Grid item xs={6} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h3>Loss Scenario</h3><br></br>{props.data.lossScenario}</Paper>
        </Grid>
        <Grid item xs={6} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h3>Notes</h3><br></br>{props.data.notes}</Paper>
        </Grid>
      </Grid>
    </div>
  );
}