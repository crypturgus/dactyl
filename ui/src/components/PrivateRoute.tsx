import { Navigate, Outlet } from "react-router-dom";
import { SIGN_IN_PATH } from "../constants.ts";
import { getAuthToken } from "../authHandlers";

export const PrivateRoute = () => {
  const auth = !!getAuthToken();
  // If authorized, return an outlet that will render child elements
  // If not, return element that will navigate to login page
  return auth ? <Outlet /> : <Navigate to={SIGN_IN_PATH} />;
};
