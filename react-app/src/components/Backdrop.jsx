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
  const [open, setOpen] = React.useState(false);
  const handleToggle = () => {
    setOpen(!open);
  };
  React.useEffect(() => {
    setOpen(!open); // this will fire on every change :(
}, []);
  

  return (
    <div>
      <Backdrop className={classes.backdrop} open={open} onLoad={() => {window.setTimeout(handleToggle, 1000);}}>
        <img class='App-logo' src='oportun_logo_circle.png' />
      </Backdrop>
    </div>
  );
}