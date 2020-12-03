import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Divider from '@material-ui/core/Divider';
const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    margin: theme.spacing(5, 10),
  },
  container: {
    display: 'grid',
    gridTemplateColumns: 'repeat(12, 1fr)',
    gridGap: theme.spacing(3),
  },
  
  Divider: {
    margin: theme.spacing(20, 0),
  },
  props: {
    MuiDivider: {
      margin: theme.spacing(200, 20),
    },
    Divider: {
      margin: theme.spacing(200, 200),
    },
  },
  '.MuiGrid-item' : {
    margin: theme.spacing(200, 20),
  }

}));

export default function CenteredGrid(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
      {props.children}
      </Grid>
    </div>
  );
}
