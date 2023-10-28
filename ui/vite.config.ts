import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // Needed so Vite allows communicating with the dockerized app through exposed port in docker-compose
  server: {
    port: 5173,
    host: '0.0.0.0',
  }
})
