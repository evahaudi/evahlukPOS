import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import { List, ListItem, ListItemText } from '@material-ui/core';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import WaiterDashboard from "../dashboard/waiterdashboard";
import Profile from '../pages/WaiterProfile';
import ManageOrders from '../pages/Manageorders';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';

const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  container: {
    display: 'flex',
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    backgroundColor: 'green',
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
    marginTop: theme.spacing(8),
    marginBottom:theme.spacing(8),

  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  profileIcon: {
    marginLeft: 'auto',
  },
  footer: {
    marginTop: 'auto',
    height:'10px',
    backgroundColor: 'green',
    padding: theme.spacing(2),
    width: '100%',
    color:'white',
    position: 'fixed',
    bottom: 0,
    textAlign: 'center',
    zIndex: theme.zIndex.drawer + 1,
    left: 0,

    [theme.breakpoints.up('sm')]: {
      padding: theme.spacing(3), // Increase padding for small screens and larger
    },

    [theme.breakpoints.up('md')]: {
      fontSize: '1.2rem', // Increase font size for medium screens and larger
    },

    [theme.breakpoints.up('lg')]: {
      padding: theme.spacing(4), // Increase padding for large screens and larger
      fontSize: '1.5rem', // Increase font size for large screens and larger
    },
  },
}));

const WaiterSidebar = () => {
  const classes = useStyles();
  const [open, setOpen] = useState(true);
  const [currentPage, setCurrentPage] = useState('Waiterdashboard');

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  const [anchorEl, setAnchorEl] = useState(null);

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleProfileMenuClose = () => {
    setAnchorEl(null);
  };

  const renderPage = () => {
    switch (currentPage) {
      case 'Waiterdashboard':
        return <WaiterDashboard />;
      case 'Profile':
        return <Profile />;
      case 'Manageorders':
        return <ManageOrders />;
      default:
        return <WaiterDashboard />;
    }
  };

  return (
    <div className={classes.container}>
      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="toggle drawer"
            onClick={open ? handleDrawerClose : handleDrawerOpen}
            edge="start"
          >
            <MenuIcon />
          </IconButton>
          <div className={classes.profileIcon}>
            <IconButton color="inherit" onClick={handleProfileMenuOpen}>
              <AccountCircleIcon />
            </IconButton>
            <Menu
              id="profile-menu"
              anchorEl={anchorEl}
              keepMounted
              open={Boolean(anchorEl)}
              onClose={handleProfileMenuClose}
            >
              <MenuItem onClick={handleProfileMenuClose}>Profile</MenuItem>
              <MenuItem onClick={handleProfileMenuClose}>Settings</MenuItem>
              <MenuItem onClick={handleProfileMenuClose}>Notifications</MenuItem>
            </Menu>
          </div>
        </Toolbar>
      </AppBar>
      <Drawer
        className={classes.drawer}
        variant="temporary"
        anchor="left"
        open={open}
        onClose={handleDrawerClose}
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <List>
          <ListItem button onClick={() => handlePageChange('Waiterdashboard')}>
            <ListItemText primary="Dashboard" />
          </ListItem>
          <ListItem button onClick={() => handlePageChange('Profile')}>
            <ListItemText primary="Profile" />
          </ListItem>
          <ListItem button onClick={() => handlePageChange('Manageorders')}>
            <ListItemText primary="Manage Orders" />
          </ListItem>
        </List>
      </Drawer>
      <main className={classes.content}>
        <Toolbar />
        {renderPage()}
      </main>
      <Box className={classes.footer} >
        <Typography variant="body2" align="center">
          © 2024 evahlukPOS. All rights reserved.
        </Typography>
      </Box>
    </div>
  );
};

export default WaiterSidebar;
