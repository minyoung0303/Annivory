import ReactDOM from "react-dom/client";

import App from "./App.jsx";
import "./index.css";
import { BrowserRouter as Router } from 'react-router-dom';

const entryPoint = document.getElementById("root");
ReactDOM.createRoot(entryPoint).render(
    <Router>
        <App />
    </Router>
);
