import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import { Input } from '@material-ui/core';
import { InputLabel } from '@material-ui/core';


const useStyles = makeStyles((theme) => ({
  root: {
    padding: theme.spacing(3),
    margin: theme.spacing(2),
    minHeight: '100vh', // Ensure full height of the viewport
  },
  paper: {
    padding: theme.spacing(3),
    maxHeight: '900px',
    maxWidth:'1800px', // Set your desired maximum height
    overflowY: 'auto', 
    minHeight: '100vh',
    minWidth:'100vh',// Add this property for vertical scrolling if content exceeds maxHeight
  },
 
}));

const Profile = () => {
  const classes = useStyles();
  const [userDetails, setUserDetails] = useState({});

  useEffect(() => {
    // Fetch user details from an API
    // Replace this with your actual API call
    fetchUserDetails().then((data) => setUserDetails(data));
  }, []);

  const fetchUserDetails = async () => {
    // Replace this with actual API call
    const response = await fetch('your-api-endpoint');
    const data = await response.json();
    return data;
  };
  
  const handleUpdateDetails = () => {
    // Handle updating user details
    // Add your logic here
  };

  return (
  
    <Paper className={classes.paper} elevation={3}>
      <Typography variant="h4" align="center" gutterBottom>
        Profile Details
      </Typography>
      <Grid container spacing={3} alignItems="center">
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="username">Username</InputLabel>
          <Input
            id="username"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.username}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="email">Email</InputLabel>
          <Input
            id="email"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.email}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="fullName">Full Name</InputLabel>
          <Input
            id="fullName"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.fullName}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="dob">Date of Birth</InputLabel>
          <Input
            id="dob"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.dob}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="location">Location</InputLabel>
          <Input
            id="location"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.location}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="experience">Experience years</InputLabel>
          <Input
            id="experience"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.experience}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="phone">Phone</InputLabel>
          <Input
            id="phone"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.phone}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="department">Department</InputLabel>
          <Input
            id="department"
            placeholder="Type in here…"
            variant="outlined"
            value={userDetails.department}
          />
        </Grid>
        <Grid item xs={8} sm={4}>
          <InputLabel htmlFor="password">Password:</InputLabel>
          <Input
            id="password"
            type="password"
            value={userDetails.password}
          />
        </Grid>
      </Grid>
      <br />
      <br />
      <Button
        variant="contained"
        color="primary"
        onClick={handleUpdateDetails}
      >
        Update Details
      </Button>
    </Paper>
   
  );
};

export default Profile;
