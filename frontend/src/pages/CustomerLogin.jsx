import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function CustomerLogin() {

    const [mobileNumber, setMobileNumber] = useState("");
    const [password, setPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);

    const navigate = useNavigate();

    const login = async () => {

        if (!mobileNumber || !password) {
            alert("Enter Mobile Number and Password");
            return;
        }
        try {

            const response = await api.post("/customer-login", {
                    mobile_number: mobileNumber,
                    password: password
                });
            
           console.log(response.data);

           localStorage.setItem(
                "customer",
                JSON.stringify(response.data.customer)
            );
            
            localStorage.setItem(
                "customer_token",
                response.data.access_token
            );
            
            alert("Welcome " + response.data.customer.name);
            navigate("/customer-dashboard");

        }

        catch {

            alert("Customer not found");

        }

    };

    return (

        <div className="container mt-5" style={{ maxWidth: "500px" }}>

            <div className="card shadow p-4">

                <h2 className="text-center">
                    Customer Login
                </h2>

                <br />

                <input
                    className="form-control"
                    placeholder="Enter Mobile Number"
                    value={mobileNumber}
                    onChange={(e) => setMobileNumber(e.target.value)}
                />
                <div className="input-group">

                <input
                    type={showPassword ? "text" : "password"}
                    className="form-control"
                    placeholder="Enter Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
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
            <br />

                <button
                    className="btn btn-success"
                    onClick={login}
                >
                    Login
                </button>
                <p className="text-center mt-3">
                        New User?{" "}
                        <span
                            style={{
                                color: "blue",
                                cursor: "pointer",
                                textDecoration: "underline"
                            }}
                            onClick={() => navigate("/customer-register")}
                        >
                            Register Here
                        </span>
                    </p>

            </div>

        </div>

    );

}

export default CustomerLogin;