import { Link, useNavigate } from "react-router-dom";

function Sidebar() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.removeItem("token");
        localStorage.removeItem("customer");
        localStorage.removeItem("customer_token");

        navigate("/");

    };

    return (

        <div
            className="d-flex flex-column text-white shadow"
            style={{
                width: "260px",
                minHeight: "100vh",
                background: "linear-gradient(180deg, #0d6efd, #0a58ca)"
            }}
        >

            <div className="text-center py-4 border-bottom">

                <h3 className="fw-bold">
                    🛡️ LIC Portal
                </h3>

                <small>Customer Dashboard</small>

            </div>

            <div className="p-3">

                <Link
                    to="/customer-dashboard"
                    className="btn btn-light w-100 mb-3 text-start"
                    style={{ transition: "0.3s" }}
                    onMouseEnter={(e) => {
                        e.currentTarget.style.transform = "translateX(8px)";
                    }}
                    onMouseLeave={(e) => {
                        e.currentTarget.style.transform = "translateX(0px)";
                    }}
                >
                    🏠 Dashboard
                </Link>

                <Link
                    to="/chatbot"
                    className="btn btn-light w-100 mb-3 text-start"
                    style={{ transition: "0.3s" }}
                    onMouseEnter={(e) => {
                        e.currentTarget.style.transform = "translateX(8px)";
                    }}
                    onMouseLeave={(e) => {
                        e.currentTarget.style.transform = "translateX(0px)";
                    }}
                >
                    🤖 AI Assistant
                </Link>

            </div>

            <div className="mt-auto p-3">

                <button
                    className="btn btn-danger w-100"
                    onClick={logout}
                >
                    🚪 Logout
                </button>

            </div>

        </div>

    );

}

export default Sidebar;