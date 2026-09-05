import { useState, useRef } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import api from "../services/api";

function Register() {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [showPassword, setShowPassword] = useState(false);

    const [errors, setErrors] = useState({});

    const usernameRef = useRef(null);
    const emailRef = useRef(null);
    const passwordRef = useRef(null);
    const registerRef = useRef(null);

    const validate = () => {

        let temp = {};

        if (username.length < 2 || username.length > 10) {
            temp.username = "Username must be between 2 and 10 characters.";
        }
        else if (!/^[A-Za-z0-9]+$/.test(username)) {
            temp.username = "Username can contain only letters and numbers.";
        }

        if (!/\S+@\S+\.\S+/.test(email)) {
            temp.email = "Please enter a valid email.";
        }

        if (password.length < 8) {
            temp.password = "Password must be at least 8 characters.";
        }
        else if (!/[A-Z]/.test(password)) {
            temp.password = "Password must contain one uppercase letter.";
        }
        else if (!/[a-z]/.test(password)) {
            temp.password = "Password must contain one lowercase letter.";
        }
        else if (!/[0-9]/.test(password)) {
            temp.password = "Password must contain one number.";
        }
        else if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
            temp.password = "Password must contain one special character.";
        }

        setErrors(temp);

        return Object.keys(temp).length === 0;
    };

    const register = async () => {

        if (!validate()) return;

        try {
            console.log({
            username,
            email,
            password
        });
            const response = await api.post("/register", {
                username,
                email,
                password
            });

            console.log(response.data);

            alert("Registration Successful!");

            setUsername("");
            setEmail("");
            setPassword("");
            setErrors({});

            usernameRef.current.focus();

        }
        catch (error) {

            console.log("FULL ERROR");
            console.log(error);
        
            if (error.response) {
                console.log("Status:", error.response.status);
                console.log(JSON.stringify(error.response.data, null, 2));
        
                alert(JSON.stringify(error.response.data, null, 2));
            }
        
            else if (error.request) {
                alert("Cannot connect to FastAPI Server.");
            }
        
            else {
                alert(error.message);
            }
        }
    };

    return (

        <div className="container mt-5" style={{ maxWidth: "500px" }}>

            <div className="card shadow p-4">

                <h2 className="text-center mb-4">
                    Register
                </h2>

                <div className="mb-3">

                    <label className="form-label">
                        Username
                    </label>

                    <input
                        ref={usernameRef}
                        className="form-control"
                        placeholder="Enter Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        onKeyDown={(e) => {

                            if (e.key === "Enter") {
                                emailRef.current.focus();
                            }

                        }}
                    />

                    {errors.username &&
                        <p className="text-danger mt-1">
                            {errors.username}
                        </p>
                    }

                    <small className="text-muted">
                        2–10 characters. Letters and numbers only.
                    </small>

                </div>

                <div className="mb-3">

                    <label className="form-label">
                        Email
                    </label>

                    <input
                        ref={emailRef}
                        type="email"
                        className="form-control"
                        placeholder="Enter Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        onKeyDown={(e) => {

                            if (e.key === "Enter") {
                                passwordRef.current.focus();
                            }

                        }}
                    />

                    {errors.email &&
                        <p className="text-danger mt-1">
                            {errors.email}
                        </p>
                    }

                    <small className="text-muted">
                        Example: abc@gmail.com
                    </small>

                </div>

                <div className="mb-3">

                    <label className="form-label">
                        Password
                    </label>

                    <div className="input-group">

                        <input
                            ref={passwordRef}
                            type={showPassword ? "text" : "password"}
                            className="form-control"
                            placeholder="Enter Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            onKeyDown={(e) => {

                                if (e.key === "Enter") {
                                    registerRef.current.focus();
                                }

                            }}
                        />

                        <button
                            type="button"
                            className="btn btn-outline-secondary"
                            onClick={() => setShowPassword(!showPassword)}
                        >

                            {
                                showPassword
                                    ?
                                    <FaEyeSlash />
                                    :
                                    <FaEye />
                            }

                        </button>

                    </div>

                    {errors.password &&
                        <p className="text-danger mt-1">
                            {errors.password}
                        </p>
                    }

                    <small className="text-muted">
                        Password must contain:
                        <br />
                        ✔ Minimum 8 characters
                        <br />
                        ✔ One uppercase letter
                        <br />
                        ✔ One lowercase letter
                        <br />
                        ✔ One number
                        <br />
                        ✔ One special character
                    </small>

                </div>

                <button
                    ref={registerRef}
                    className="btn btn-success w-100"
                    onClick={register}
                >
                    Register
                </button>

            </div>

        </div>

    );
}

export default Register;