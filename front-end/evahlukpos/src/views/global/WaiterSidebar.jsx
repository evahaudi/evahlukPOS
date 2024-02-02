import React, { useState } from "react";
import { Box, IconButton, Typography,MenuItem, Drawer, List, useTheme } from "@mui/material";
import { Link } from "react-router-dom";
import { tokens } from "../../theme";
import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";


const Item = ({ title, to, icon, selected, setSelected }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  return (
    <MenuItem
      active={selected === title}
      style={{
        color: colors.white[100],
      }}
      onClick={() => setSelected(title)}
      icon={icon}
    >
      <Typography>{title}</Typography>
      <Link to={to} />
    </MenuItem>
  );
};
const WaiterSidebar = () => {
  const colors = tokens("light"); // Assuming you have a function that returns color tokens

  const [isDrawerOpen, setIsDrawerOpen] = useState(false);
  const [selected, setSelected] = useState("Dashboard");

  const handleDrawerOpen = () => {
    setIsDrawerOpen(true);
  };

  const handleDrawerClose = () => {
    setIsDrawerOpen(false);
  };

  return (
    <Box>
      <IconButton onClick={handleDrawerOpen}>
        <MenuOutlinedIcon />
      </IconButton>

      <Drawer anchor="left" open={isDrawerOpen} onClose={handleDrawerClose}>
        <Box
          sx={{
            background: `${colors.black[100]} !important`,
            height: "100vh",
            padding: "20px",
          }}
        >
          <IconButton onClick={handleDrawerClose} style={{ color: colors.white[100] }}>
            <MenuOutlinedIcon />
          </IconButton>

          <List>
            <Item
              title="Dashboard"
              to="/waiterdashboard"
              icon={<HomeOutlinedIcon style={{ color: colors.white[100] }} />}
              selected={selected}
              setSelected={setSelected}
            />
            {/* Add more items as needed */}
          </List>
        </Box>
      </Drawer>
    </Box>
  );
};

export default WaiterSidebar;
