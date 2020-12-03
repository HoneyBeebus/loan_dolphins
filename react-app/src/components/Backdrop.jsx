import React from 'react';
import Backdrop from '@material-ui/core/Backdrop';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import '../App.css'

const useStyles = makeStyles((theme) => ({
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: '#fff',
  },
}));

export default function SimpleBackdrop() {
  const classes = useStyles();
  const [open, setOpen] = React.useState(true);
  const handleToggle = () => {
    setOpen(!open);
  };

  return (
    <div>
      <Backdrop className={classes.backdrop} open={open}>
        <img class='App-logo' src='oportun_logo_circle.png' />
        <Button variant="contained" color="primary" onClick={handleToggle}>
            Welcome
        </Button>
      </Backdrop>
    </div>
  );
}