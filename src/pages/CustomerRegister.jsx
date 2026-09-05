import { FaEye, FaEyeSlash } from "react-icons/fa";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function CustomerRegister() {

    const [mobileNumber, setMobileNumber] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);

    const navigate = useNavigate();

    const register = async () => {

        if (!mobileNumber || !password || !confirmPassword) {
            alert("Please fill all fields");
            return;
        }
    
        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return;
        }
    
        try {
    
            const response = await api.post("/customer-register", {
                mobile_number: mobileNumber,
                password: password
            });
    
            console.log(response.data);
    
            alert("Registration successful");
    
            setMobileNumber("");
            setPassword("");
            setConfirmPassword("");
    
        } catch(error) {

            console.log(error.response?.data);
        
            if(error.response){
        
                if(typeof error.response.data === "object"){
                    alert(
                        JSON.stringify(error.response.data, null, 2)
                    );
                }
                else{
                    alert(error.response.data);
                }
        
            }
            else{
                alert("Server is not responding");
            }
        
        }
    };
    return (

        <div className="container mt-5" style={{ maxWidth: "500px" }}>

            <div className="card shadow p-4">

                <h2 className="text-center mb-4">
                    Customer Register
                </h2>

                <input
                    className="form-control"
                    placeholder="Enter Mobile Number"
                    value={mobileNumber}
                    onChange={(e) => setMobileNumber(e.target.value)}
                />

                <br />

                <div className="input-group">

                        <input
                            type={showPassword ? "text" : "password"}
                            className="form-control"
                            placeholder="Enter Password"
                            value={password}
                            onChange={(e)=>setPassword(e.target.value)}
                        />
                        
                        <button
                            type="button"
                            className="btn btn-outline-secondary"
                            onClick={()=>setShowPassword(!showPassword)}
                        >
                        {
                        showPassword ? <FaEyeSlash/> : <FaEye/>
                        }
                        </button>
                        
                        </div>
                <br />

                <input
                    type="password"
                    className="form-control"
                    placeholder="Confirm Password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />

                <br />

                <button 
                    type="button" 
                    className="btn btn-success w-100"
                    onClick={register}
                >
                    Register
                </button>

                <p className="text-center mt-3 mb-0">
                    Already have an account?{" "}
                    <span
                        style={{
                            cursor: "pointer",
                            color: "blue",
                            textDecoration: "underline"
                        }}
                        onClick={() => navigate("/customer-login")}
                    >
                        Login
                    </span>
                </p>

            </div>

        </div>

    );
}

export default CustomerRegister;