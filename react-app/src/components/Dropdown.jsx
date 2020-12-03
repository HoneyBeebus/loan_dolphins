import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';

const useStyles = makeStyles((theme) => ({
  button: {
    display: 'block',
    marginTop: theme.spacing(2)
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
    borderRadius: 4,
    color: 'secondary'//theme.palette.background.paper
  },
}));

export default function ControlledOpenSelect(props) {
  const classes = useStyles();
  const [source, setSource] = React.useState('');
  if (props.value !== undefined) setSource(props.value);
  const [open, setOpen] = React.useState(false);

  const handleChange = (event) => {
    setSource(event.target.value);
    if (typeof props.onChange == "function") props.onChange(event);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleOpen = () => {
    setOpen(true);
  };

  return (
    <div>
      <FormControl className={classes.formControl}>
        <InputLabel id="demo-controlled-open-select-label">{props.label}</InputLabel>
        <Select
          labelId="demo-controlled-open-select-label"
          id="demo-controlled-open-select"
          open={open}
          onClose={handleClose}
          onOpen={handleOpen}
          value={source}
          onChange={handleChange}
        >
          {props.children}
        </Select>
      </FormControl>
    </div>
  );
}