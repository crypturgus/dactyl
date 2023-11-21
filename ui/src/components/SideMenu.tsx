import { FunctionComponent } from "react";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import Toolbar from "@mui/material/Toolbar";
import { mainListItems, secondaryListItems } from "./listItems";

const drawerWidth = 240;

export const SideMenu: FunctionComponent = () => (
  <Drawer
    variant="permanent"
    sx={{
      width: drawerWidth,
      flexShrink: 0,
      "& .MuiDrawer-paper": { width: drawerWidth, boxSizing: "border-box" },
    }}
  >
    <Toolbar />
    <Divider />
    <List>{mainListItems}</List>
    <Divider />
    <List>{secondaryListItems}</List>
  </Drawer>
);
