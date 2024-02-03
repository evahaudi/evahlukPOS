import { Paper, Typography } from '@mui/material';
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

// import Header from '../../components/Header';
const useStyles = makeStyles((theme) => ({
  root: {
    padding: theme.spacing(3),
    margin: theme.spacing(2),
    minHeight: '100vh', // Ensure full height of the viewport
  },
  paper: {
    padding: theme.spacing(3),
    maxHeight: '900px',
    maxWidth: '1800px', // Set your desired maximum height
    overflowY: 'auto',
    minHeight: '100vh',
    minWidth: '100vh',// Add this property for vertical scrolling if content exceeds maxHeight
  },

}));



const ManageEmployees = () => {
  const classes = useStyles();


  return (
    <div>
      <Paper className={classes.paper} elevation={3}>
        <Typography variant="h4" align="center" gutterBottom>
          Welcome
        </Typography>
      </Paper>
    </div>



  );
};

export default ManageEmployees;
