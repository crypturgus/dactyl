import { gql } from "@apollo/client";

export const LOGIN = gql`
  mutation LoginUser($email: String!, $password: String!) {
    loginUser(input: { email: $email, password: $password }) {
      user {
        email
      }
      token
    }
  }
`;
