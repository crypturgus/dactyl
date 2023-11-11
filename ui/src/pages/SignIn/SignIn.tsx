import * as React from "react";
import { useNavigate } from "react-router";
import { useMutation } from "@apollo/client";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CircularProgress from "@mui/material/CircularProgress";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { LOGIN } from "./queries";
import { signIn } from "../../authHandlers";
import { SIGN_UP_PATH } from "../../constants";

export const SignIn = () => {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [validationError, setValidationError] = React.useState({ email: "", password: "" });

  const navigate = useNavigate();

  const [login, { loading, error }] = useMutation(LOGIN, {
    onCompleted: (data) => {
      signIn(data.loginUser.token, navigate);
    },
    onError: (error) => {
      console.log("Error: ", error);
    },
  });

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newEmail = e.target.value;
    setEmail(newEmail);
    validateForm(newEmail, password);
  };

  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newPassword = e.target.value;
    setPassword(newPassword);
    validateForm(email, newPassword);
  };

  const validateForm = (currEmail: string, currPassword: string) => {
    let isValid = true;
    const errors = { email: "", password: "" };

    if (!!currEmail.length && !/\S+@\S+\.\S+/.test(currEmail)) {
      errors.email = "Invalid email format";
      isValid = false;
    }

    if (!!currPassword.length && currPassword.length < 6) {
      errors.password = "Password must be at least 6 characters";
      isValid = false;
    }

    setValidationError(errors);
    return isValid;
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!validateForm(email, password)) {
      return;
    }
    login({ variables: { email, password } });
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate mb={3}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
            value={email}
            onChange={handleEmailChange}
            error={!!error || !!validationError.email}
            helperText={validationError.email}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            value={password}
            onChange={handlePasswordChange}
            error={!!error || !!validationError.password}
            helperText={validationError.password}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            disabled={!email || !password}
            sx={{
              mt: 3,
              mb: 2,
              "&.Mui-disabled": {
                bgcolor: "lightblue",
                color: "white",
              },
            }}
          >
            Sign In
          </Button>
          <Link href={SIGN_UP_PATH} variant="body2">
            {"Don't have an account? Sign Up"}
          </Link>
        </Box>
        {loading && <CircularProgress />}
      </Box>
    </Container>
  );
};
