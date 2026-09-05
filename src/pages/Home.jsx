import { Link } from "react-router-dom";

function Home() {
    return (
        <div
            className="container-fluid d-flex align-items-center justify-content-center"
            style={{
                minHeight: "100vh",
                background: "linear-gradient(to right, #eef2f3, #d9e4f5)"
            }}
        >
            <div className="container">

                <div className="text-center mb-5">

                    <h1 className="display-4 fw-bold text-primary">
                        Insurance Management System
                    </h1>

                    <p className="lead text-secondary">
                        AI Powered Insurance Management Portal
                    </p>

                </div>

                <div className="row justify-content-center">

                    {/* Agent Card */}

                    <div className="col-md-5 mb-4">

                        <div
                            className="card shadow-lg border-0 h-100"
                            style={{
                                borderRadius: "18px",
                                transition: "0.35s",
                                cursor: "pointer"
                            }}
                            onMouseEnter={(e) => {
                                e.currentTarget.style.transform =
                                    "translateY(-10px) scale(1.02)";
                                e.currentTarget.style.boxShadow =
                                    "0 18px 35px rgba(0,0,0,0.2)";
                            }}
                            onMouseLeave={(e) => {
                                e.currentTarget.style.transform =
                                    "translateY(0)";
                                e.currentTarget.style.boxShadow =
                                    "0 .5rem 1rem rgba(0,0,0,.15)";
                            }}
                        >

                            <div className="card-body text-center p-5">

                                <i
                                    className="bi bi-person-workspace"
                                    style={{
                                        fontSize: "70px",
                                        color: "#0d6efd"
                                    }}
                                ></i>

                                <h2 className="mt-3">
                                    Agent
                                </h2>

                                <p className="text-muted mt-3">

                                    Manage Customers,
                                    Policies, Analytics
                                    and AI Assistant.

                                </p>

                                <Link
                                    to="/agent-login"
                                    className="btn btn-primary btn-lg mt-3 w-100"
                                >
                                    Continue
                                </Link>

                            </div>

                        </div>

                    </div>

                    {/* Customer Card */}

                    <div className="col-md-5 mb-4">

                        <div
                            className="card shadow-lg border-0 h-100"
                            style={{
                                borderRadius: "18px",
                                transition: "0.35s",
                                cursor: "pointer"
                            }}
                            onMouseEnter={(e) => {
                                e.currentTarget.style.transform =
                                    "translateY(-10px) scale(1.02)";
                                e.currentTarget.style.boxShadow =
                                    "0 18px 35px rgba(0,0,0,0.2)";
                            }}
                            onMouseLeave={(e) => {
                                e.currentTarget.style.transform =
                                    "translateY(0)";
                                e.currentTarget.style.boxShadow =
                                    "0 .5rem 1rem rgba(0,0,0,.15)";
                            }}
                        >

                            <div className="card-body text-center p-5">

                                <i
                                    className="bi bi-person-circle"
                                    style={{
                                        fontSize: "70px",
                                        color: "#198754"
                                    }}
                                ></i>

                                <h2 className="mt-3">
                                    Customer
                                </h2>

                                <p className="text-muted mt-3">

                                    View Policies,
                                    Premium Details,
                                    Claims and AI Support.

                                </p>

                                <Link
                                    to="/customer-login"
                                    className="btn btn-success btn-lg mt-3 w-100"
                                >
                                    Continue
                                </Link>

                            </div>

                        </div>

                    </div>

                </div>

            </div>
        </div>
    );
}

export default Home;