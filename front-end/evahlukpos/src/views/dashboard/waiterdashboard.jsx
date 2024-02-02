import React, { useState } from "react";
import {
  Box,
  Typography,
  useTheme,
  Drawer,
  List,
  ListItem,
  ListItemText,
  AppBar,
  Toolbar,
  IconButton,
  Menu,
  Button,
  MenuItem,
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import Header from "../../components/Header";
import { tokens } from "../../theme";


const WaiterDashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [isDrawerOpen, setDrawerOpen] = useState(false);
  const [anchorEl, setAnchorEl] = useState(null);

  const toggleDrawer = (open) => (event) => {
    if (
      event.type === "keydown" &&
      (event.key === "Tab" || event.key === "Shift")
    ) {
      return;
    }
    setDrawerOpen(open);
  };

  const handleMenuClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };



  return (
    <Box>
      {/* APP BAR */}
      <AppBar position="static">
        <Toolbar>
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            onClick={toggleDrawer(true)}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" style={{ flex: 1 }}>
            DASHBOARD
          </Typography>
          <IconButton
            color="inherit"
            aria-controls="profile-menu"
            aria-haspopup="true"
            onClick={handleMenuClick}
          >
            {/* Add your profile icon or image here */}
          </IconButton>
          <Menu
            id="profile-menu"
            anchorEl={anchorEl}
            keepMounted
            open={Boolean(anchorEl)}
            onClose={handleMenuClose}
          >
            <MenuItem onClick={handleMenuClose}>Profile</MenuItem>
            <MenuItem onClick={handleMenuClose}>Logout</MenuItem>
          </Menu>
        </Toolbar>
      </AppBar>

      {/* DRAWER */}
      <Drawer anchor="left" open={isDrawerOpen} onClose={toggleDrawer(false)}>
        <List>
          <ListItem Button>
            <ListItemText primary="Drawer Item 1" />
          </ListItem>
          <ListItem Button>
            <ListItemText primary="Drawer Item 2" />
          </ListItem>
          {/* Add more items as needed */}
        </List>
      </Drawer>

      {/* MAIN CONTENT */}
      <Box m="20px">
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Header title="DASHBOARD" subtitle="Welcome to your dashboard" />
        </Box>
        <Box>

        </Box>
      </Box>

      {/* FOOTER */}
      <Box textAlign="center" py={50}>
        <Typography variant="h5" color={colors.grey[100]}>
          @2023KRA Copyrights. All rights reserved.
        </Typography>
      </Box>
    </Box>
  );
};

export default WaiterDashboard;
