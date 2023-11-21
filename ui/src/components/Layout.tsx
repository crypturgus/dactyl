import React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import { SideMenu } from "./SideMenu";


interface LayoutProps {
  pageContent: React.ReactNode;
  pageTitle: string;
}

export function Layout({ pageContent, pageTitle }: LayoutProps) {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <AppBar position="absolute" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <Typography component="h1" variant="h6" color="inherit" noWrap sx={{ flexGrow: 1 }}>
            {pageTitle}
          </Typography>
        </Toolbar>
      </AppBar>
      <SideMenu />
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        {pageContent}
      </Box>
    </Box>
  );
}
