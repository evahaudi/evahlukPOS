import React from 'react';
import { useLocation } from 'react-router-dom';
import MyAppBar from '../pages/Theappbar';
import Footer from '../pages/Thefooter';

const Layout = ({ children }) => {
  const location = useLocation();

  // Check if the current path is a sidebar route
  const isSidebarRoute = () => {
    return (
      location.pathname === '/waitersidebar' ||
      location.pathname === '/managersidebar' ||
      location.pathname === '/chefsidebar'
    );
  };

  return (
    <div>
      {!isSidebarRoute() && <MyAppBar />}
      <main className="App">
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;
