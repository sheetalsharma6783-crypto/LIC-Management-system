import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function AgentLogin() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();

    const login = async () => {

        try {

            const response = await api.post("/login", {
                    email,
                    password
                });

            localStorage.setItem(
                "token",
                response.data.access_token
            );

            alert("Login Successful");

            navigate("/agent-dashboard");

        }

        catch {

            alert("Invalid Email or Password");

        }

    };

    return (

        <div className="container mt-5">

            <h2>Agent Login</h2>

            <br />

            <input
                type="email"
                autoComplete="off"
                className="form-control"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />

            <br />
            <input
                type="password"
                autoComplete="new-password"
                className="form-control"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <br />

            <button
                className="btn btn-primary"
                onClick={login}
            >
                Login
            </button>

            <br /><br />

            <p>New User?</p>

            <button
                className="btn btn-success"
                onClick={() => navigate("/register")}
            >
                Register
            </button>

        </div>

    );

}

export default AgentLogin;