import { BrowserRouter, Routes, Route } from "react-router-dom";
import styled from "styled-components";
import { PrivateRoute } from "./components/PrivateRoute";
import { Dashboard } from "./pages/Dashboard";
import { Invoice } from "./pages/Invoice";
import { SignIn } from "./pages/SignIn";
import { SignUp } from "./pages/SignUp";
import { Welcome } from "./pages/Welcome";
import { DASHBOARD_PATH, INVOICE_PATH, ROOT_PATH, SIGN_IN_PATH, SIGN_UP_PATH } from "./constants";

function App() {
  return (
    <Wrapper>
      <BrowserRouter>
        <Routes>
          <Route path={ROOT_PATH} element={<PrivateRoute />}>
            <Route index element={<Welcome />} />
            <Route path={DASHBOARD_PATH} element={<Dashboard />} />
            <Route path={INVOICE_PATH} element={<Invoice />} />
          </Route>
          <Route path={SIGN_IN_PATH} element={<SignIn />} />
          <Route path={SIGN_UP_PATH} element={<SignUp />} />
        </Routes>
      </BrowserRouter>
    </Wrapper>
  );
}

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  gap: 20px;
`;

export default App;
