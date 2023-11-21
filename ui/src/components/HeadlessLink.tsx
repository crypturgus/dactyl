import { FunctionComponent } from "react";
import { Link, LinkProps } from "react-router-dom";

interface HeadlessLinkProps extends LinkProps {
  children: React.ReactNode;
}

export const HeadlessLink: FunctionComponent<HeadlessLinkProps> = ({ children, ...linkProps }) => (
  <Link {...linkProps} style={{ textDecoration: "none", color: "inherit" }}>
    {children}
  </Link>
);
