import React from 'react';
import { Routes, Route } from "react-router-dom";
import ChefDashboard from "./views/dashboard/chefdashbboard";
// import WaiterDashboard from "./views/dashboard/waiterdashboard";
import ManagerDashboard from "./views/dashboard/waiterdashboard";
import WaiterLogin from './views/login/WaiterLogin';
import Register from "./views/signup/Register";
import Layout from "./views/global/Layouts";
import RequireAuth from "./context/RequireAuth";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import ManagerLogin from './views/login/ManagerLogin';
import ChefLogin from './views/login/ChefLogin';
import WaiterSidebar from "./views/global/WaiterSidebar"
import ManagerSidebar from './views/global/ManagerSidebar';
import ChefSidebar from './views/global/ChefSidebar';

const ROLES = {
  'isChef': 'isChef',
  'isWaiter': 'isWaiter',
  'Admin': 5150,
  'isManager': 'isManager'
}


function App() {
  const [theme, colorMode] = useMode();
  

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
                 
            <Routes>
              {/* <Route path="/" element={Dashboard}/>
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<Signup />} /> */}
                <Route path="/" element={<Layout />}>
                  {/* public routes */}
                  <Route path="/waiterLogin" element={<WaiterLogin />} />
                  <Route path="/chefLogin" element={<ChefLogin />} />
                  <Route path="/managerLogin" element={<ManagerLogin />} />
                  <Route path="/" element={<Register />} />


                  {/* we want to protect these routes */}
                  {/* <Route element={<RequireAuth allowedRoles={[ROLES.isWaiter]} />}>
                    <Route path="waiterdashboard" element={<WaiterDashboard />} />
                  </Route> */}
                  <Route element={<RequireAuth allowedRoles={[ROLES.isWaiter]} />}>
                    <Route path="waitersidebar" element={<WaiterSidebar />} />
                  </Route>
                  <Route element={<RequireAuth allowedRoles={[ROLES.isManager]} />}>
                    <Route path="managersidebar" element={<ManagerSidebar />} />
                  </Route>
                  <Route element={<RequireAuth allowedRoles={[ROLES.isChef]} />}>
                    <Route path="chefsidebar" element={<ChefSidebar />} />
                  </Route>                  
                  <Route element={<RequireAuth allowedRoles={[ROLES.isManager]} />}>
                    <Route path="managerdashboard" element={<ManagerDashboard />} />
                  </Route>
                  <Route element={<RequireAuth allowedRoles={[ROLES.isChef]} />}>
                    <Route path="chefdashboard" element={<ChefDashboard />} />
                  </Route>
                  
                  </Route>
              </Routes>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;


