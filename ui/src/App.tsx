import { useQuery, gql } from "@apollo/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import styled from "styled-components";
import { Dashboard } from "./pages/Dashboard";
import { SignIn } from "./pages/SignIn";
import { SignUp } from "./pages/SignUp";

const GET_USERS = gql`
  query {
    users {
      email
    }
  }
`;

function App() {
  const { loading, error, data } = useQuery(GET_USERS);

  return (
    <Wrapper>
      <BrowserRouter>
        <Routes>
          <Route
            path={"/"}
            element={loading ? <>loading</> : error ? <>error</> : <>Our users are: {JSON.stringify(data.users)}</>}
          />
          <Route path={"/sign-in"} element={<SignIn />} />
          <Route path={"/sign-up"} element={<SignUp />} />
          <Route path={"/dashboard"} element={<Dashboard />} />
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
