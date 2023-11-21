import { useApolloClient, useQuery, gql } from "@apollo/client";
import { useNavigate } from "react-router";
import Button from "@mui/material/Button";
import { Layout } from "../../components/Layout";
import { signOut } from "../../authHandlers";

const GET_USERS = gql`
  query {
    users {
      email
    }
  }
`;

export function Welcome() {
  const { loading, error, data } = useQuery(GET_USERS);

  const client = useApolloClient();
  const navigate = useNavigate();
  return (
    <Layout
      pageTitle="Welcome"
      pageContent={
        <>
          Hi! you're logged in!{" "}
          {loading ? <>loading</> : error ? <>error</> : <>Our users are: {JSON.stringify(data.users)}</>}
          <Button onClick={() => signOut(client, navigate)}>Log out</Button>
        </>
      }
    />
  );
}
