import { ApolloClient } from '@apollo/client';
import { NavigateFunction } from 'react-router-dom';
import { SIGN_IN_PATH, ROOT_PATH } from "./constants";

export const setAuthToken = (authToken: string) => {
  localStorage.setItem("auth-token", authToken);
}

export const getAuthToken = (): string | null => {
  return localStorage.getItem("auth-token");
}

export const signIn = (authToken: string, navigate: NavigateFunction) => {
  setAuthToken(authToken);
  navigate(ROOT_PATH);
}

export const signOut = (apolloClient: ApolloClient<object>, navigate: NavigateFunction) => {
  setAuthToken("");
  apolloClient.clearStore()
  navigate(SIGN_IN_PATH);
}