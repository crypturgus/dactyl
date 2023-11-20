import Container from "@mui/material/Container";
import { Layout } from "../../components/Layout";

export function Invoice() {
  return (
    <Layout
      pageTitle="Invoice"
      pageContent={
        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          Invoice
        </Container>
      }
    />
  );
}
