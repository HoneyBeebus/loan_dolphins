import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: "theme.palette.text.secondary",
    backgroundColor: "#a39f9d",
  },
}));

export default function FullWidthGrid() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Overall Risk<br></br>Inherent:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={12} sm={6} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Primary Risk<br></br>Inherent:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={12} sm={6} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Secondary Risk<br></br>Inherent:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Primary Loss Event Frequency <br></br>Inherent:<br></br><br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Primary Loss Magnitude<br></br>Inherent:<br></br>Controls:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Secondary Loss Magnitude<br></br>Inherent:<br></br>Controls:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={6} sm={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Secondary Loss Event Frequency<br></br>Inherent:<br></br><br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Threat Event Frequency<br></br>Inherent:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Vulnerability<br></br>Inherent:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={4} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Secondary Loss Probability<br></br><br></br>%</Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Contact Frequency Avoidance<br></br>Inherent:<br></br>Controls:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Threat Capability<br></br><br></br><br></br>OWASP: </Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Probability of Action Deterrence<br></br>Inherent:<br></br>Controls:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={3} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Resistance Strength Vulnerability<br></br>Inherent:<br></br>Controls:<br></br>Residual:</Paper>
        </Grid>
        <Grid item xs={12} style={{backgroundColor: '#757473'}}>
          <Paper className={classes.paper}>Notes</Paper>
        </Grid>
      </Grid>
    </div>
  );
}