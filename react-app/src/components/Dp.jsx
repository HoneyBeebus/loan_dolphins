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

export default function ControlledOpenSelect() {
  const classes = useStyles();
  const [source, setSource] = React.useState('');
  const [open, setOpen] = React.useState(false);

  const handleChange = (event) => {
    setSource(event.target.value);
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
        <InputLabel id="demo-controlled-open-select-label">Matrix</InputLabel>
        <Select
          labelId="demo-controlled-open-select-label"
          id="demo-controlled-open-select"
          open={open}
          onClose={handleClose}
          onOpen={handleOpen}
          value={source}
          onChange={handleChange}
        >
          <MenuItem value={"overall.png"}>
            <em>None</em>
          </MenuItem>
          <MenuItem value={"overall.png"}>Overall Risk</MenuItem>
          <MenuItem value={"primary.png"}>Primary Risk</MenuItem>
          <MenuItem value={"secondary.png"}>Secondary Risk</MenuItem>
          <MenuItem value={"primLoss.png"}>Loss Event Frequency</MenuItem>
          <MenuItem value={"vulnerability.png"}>Vulnerability</MenuItem>
          <MenuItem value={"secLoss.png"}>Secondary Loss Event Frequency</MenuItem>
        </Select>
      </FormControl>
    </div>
  );
}