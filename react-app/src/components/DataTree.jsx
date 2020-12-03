import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import ColorText from './ColorText';

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
          <Paper className={classes.paper}><h3>Overall Risk</h3>Inherent: <ColorText value={props.data.overallRiskInherent} /><br></br>Residual: <ColorText value={props.data.overallRiskResidual} /></Paper>
        </Grid>
        <Grid item xs={12} sm={6} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h4>Primary Risk</h4>Inherent: <ColorText value={props.data.primaryRiskInherent} /><br></br>Residual: <ColorText value={props.data.primaryRiskResidual} /></Paper>
        </Grid>
        <Grid item xs={12} sm={6} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h4>Secondary Risk</h4>Inherent: <ColorText value={props.data.secondaryRiskInherent} /><br></br>Residual: <ColorText value={props.data.secondaryRiskResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Primary Loss Event Frequency</h5>Inherent: <ColorText value={props.data.primaryLossEventFrequencyInherent} /><br></br><br></br>Residual: <ColorText value={props.data.primaryLossEventFrequencyResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Primary Loss Magnitude</h5>Inherent: <ColorText value={props.data.primaryLossMagnitudeResponsiveInherent} /><br></br>Controls: <ColorText value={props.data.primaryLossMagnitudeResponsiveControls} /><br></br>Residual: <ColorText value={props.data.primaryLossMagnitudeResponsiveResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Secondary Loss Magnitude</h5>Inherent: <ColorText value={props.data.secondaryLossMagnitudeResponsiveInherent} /><br></br>Controls: <ColorText value={props.data.secondaryLossMagnitudeResponsiveControls} /><br></br>Residual: <ColorText value={props.data.secondaryLossMagnitudeResponsiveResidual} /></Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h5>Secondary Loss Event Frequency</h5>Inherent: <ColorText value={props.data.secondaryLossEventFrequencyInherent} /><br></br><br></br>Residual: <ColorText value={props.data.secondaryLossEventFrequencyResidual} /></Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Threat Event Frequency</h6>Inherent: <ColorText value={props.data.threatEventFrequencyInherent} /><br></br>Residual: <ColorText value={props.data.threatEventFrequencyResidual} /></Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Vulnerability</h6>Inherent: <ColorText value={props.data.vulnerabilityInherent} /><br></br>Residual: <ColorText value={props.data.vulnerabilityResidual} /></Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Secondary Loss Probability</h6><br></br>% {props.data.secondaryLossProbability}</Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Contact Frequency Avoidance</h6>Inherent: <ColorText value={props.data.contactFrequencyAvoidanceInherent} /><br></br>Controls: <ColorText value={props.data.contactFrequencyAvoidanceControls} /><br></br>Residual: <ColorText value={props.data.contactFrequencyAvoidanceResidual} /></Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Threat Capability</h6><br></br><br></br>OWASP: {props.data.threatCapability}</Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Probability of Action Deterrence</h6>Inherent: <ColorText value={props.data.probabilityOfActionDeterrenceInherent} /><br></br>Controls: <ColorText value={props.data.probabilityOfActionDeterrenceControls} /><br></br>Residual: <ColorText value={props.data.probabilityOfActionDeterrenceResidual} /></Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h6>Resistance Strength Vulnerability</h6>Inherent: <ColorText value={props.data.resistanceStrengthVulnerabilityInherent} /><br></br>Controls: <ColorText value={props.data.resistanceStrengthVulnerabilityControls} /><br></br>Residual: <ColorText value={props.data.resistanceStrengthVulnerabilityResidual} /></Paper>
        </Grid>
        <Grid item xs={12} style={{backgroundColor: '#a6a4a2'}}>
          <Paper className={classes.paper}><h3>Notes</h3><br></br>{props.data.notes}</Paper>
        </Grid>
      </Grid>
    </div>
  );
}