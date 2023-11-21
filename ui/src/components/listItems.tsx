import * as React from "react";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ListSubheader from "@mui/material/ListSubheader";
import DashboardIcon from "@mui/icons-material/Dashboard";
import PeopleIcon from "@mui/icons-material/People";
import LayersIcon from "@mui/icons-material/Layers";
import AssignmentIcon from "@mui/icons-material/Assignment";
import { HeadlessLink } from "./HeadlessLink";
import { DASHBOARD_PATH, INVOICE_PATH, ROOT_PATH, SIGN_IN_PATH, SIGN_UP_PATH } from "../constants";

export const mainListItems = (
  <React.Fragment>
    <HeadlessLink to={ROOT_PATH}>
      <ListItemButton>
        <ListItemIcon>
          <AssignmentIcon />
        </ListItemIcon>
        <ListItemText primary="Welcome" />
      </ListItemButton>
    </HeadlessLink>
    <HeadlessLink to={DASHBOARD_PATH}>
      <ListItemButton>
        <ListItemIcon>
          <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary="Dashboard" />
      </ListItemButton>
    </HeadlessLink>
    <HeadlessLink to={INVOICE_PATH}>
      <ListItemButton>
        <ListItemIcon>
          <LayersIcon />
        </ListItemIcon>
        <ListItemText primary="Invoice" />
      </ListItemButton>
    </HeadlessLink>
  </React.Fragment>
);

export const secondaryListItems = (
  <React.Fragment>
    <ListSubheader component="div" inset>
      Other pages
    </ListSubheader>
    <HeadlessLink to={SIGN_IN_PATH}>
      <ListItemButton>
        <ListItemIcon>
          <PeopleIcon />
        </ListItemIcon>
        <ListItemText primary="Sign-in" />
      </ListItemButton>
    </HeadlessLink>
    <HeadlessLink to={SIGN_UP_PATH}>
      <ListItemButton>
        <ListItemIcon>
          <PeopleIcon />
        </ListItemIcon>
        <ListItemText primary="Sign-up" />
      </ListItemButton>
    </HeadlessLink>
  </React.Fragment>
);
