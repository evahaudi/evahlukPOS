import React from 'react';
import { useState } from "react";
import { Box, Typography, useTheme } from '@mui/material';
import Header from '../../components/Header';
import ChefSidebar from '../global/ChefSidebar';  // Import the Sidebar component
import Topbar from '../global/Topbar';    // Import the Topbar component
import { tokens } from '../../theme';

const ChefDashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    <Box m="20px">
      {/* SIDEBAR AND TOPBAR */}
      <ChefSidebar isSidebar={isSidebar} />   
      <Topbar setIsSidebar={setIsSidebar} />
      {/* CONTENT */}
      <Box ml={{ sm: '250px' }} p="20px"> {/* Adjust margin based on your design */}
        {/* HEADER */}
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Header title="DASHBOARD" subtitle="Welcome to your chef dashboard" />
        </Box>
        <Box>
          {/* Your dashboard content goes here */}
        </Box>

        {/* FOOTER */}
        <Box textAlign="center" py={2}>
          <Typography variant="h5" color={colors.grey[100]}>
            @2023KRA Copyrights. All rights reserved.
          </Typography>
        </Box>
      </Box>
    </Box>
      
    
  );
};

export default ChefDashboard;
