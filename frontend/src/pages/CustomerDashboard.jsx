import { useEffect, useState } from "react";
import api from "../services/api";
import Sidebar from "../components/Sidebar";
function CustomerDashboard() {

    const [customer, setCustomer] = useState(null);
    const [policies, setPolicies] = useState([]);

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);
    useEffect(() => {

    const storedCustomer = JSON.parse(
        localStorage.getItem("customer")
    );

    if (!storedCustomer) return;

    setCustomer(storedCustomer);

    api.get(`/customers/${storedCustomer.customer_id}/policies`)
        .then((response) => {

            setPolicies(response.data);

        })
        .catch((err) => console.log(err));

}, []);

    if (!customer) {
        return (
            <div className="container mt-5 text-center">
                <h3>Customer Not Logged In</h3>
            </div>
        );
    }
    const askAI = async () => {

    try {

        setLoading(true);

        setAnswer("");

        const customer = JSON.parse(
            localStorage.getItem("customer")
        );

        const response = await api.post(
            "/ask-ai",
            {
                customer_id: customer.customer_id,
                question: question
            }
        );

        setAnswer(response.data.answer);

    }

    catch (error) {

        console.log(error);
    
        if (error.response) {
            console.log(error.response.data);
            alert(JSON.stringify(error.response.data));
        }
        else {
            alert(error.message);
        }

}
    finally {

        setLoading(false);

    }

};
    return (
        <div className="d-flex">

            <Sidebar />

            <div
                className="container-fluid p-4"
                style={{
                    background: "#f5f7fa",
                    minHeight: "100vh"
                }}
            >

                <h2 className="mb-4">
                    Welcome, {customer.name}
                </h2>

                <div className="row mb-4">

                    <div className="col-md-4">
                        <div className="card bg-primary text-white shadow">
                            <div className="card-body">
                                <h5>Customer ID</h5>
                                <h2>{customer.customer_id}</h2>
                            </div>
                            <div className="card shadow mt-4">

                            <div className="card-header bg-dark text-white">
                                <h4>🤖 AI Insurance Assistant</h4>
                            </div>
                        
                            <div className="card-body">
                        
                                <label className="form-label">
                                    Ask anything about your policy
                                </label>
                        
                                <textarea
                                    className="form-control"
                                    rows="4"
                                    placeholder="Example: What is my policy type?"
                                    value={question}
                                    onChange={(e) => setQuestion(e.target.value)}
                                />
                        
                                <br />
                        
                                <button
                                    className="btn btn-primary"
                                    onClick={askAI}
                                    disabled={loading}
                                >
                                    {loading ? "Thinking..." : "Ask AI"}
                                </button>
                        
                                {
                                    answer &&
                                    <div className="alert alert-info mt-4">
                        
                                        <h5>AI Response</h5>
                        
                                        <hr />
                        
                                        <p>{answer}</p>

            </div>
        }

    </div>

</div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card bg-success text-white shadow">
                            <div className="card-body">
                                <h5>Mobile Number</h5>
                                <h5>{customer.mobile_number}</h5>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card bg-warning shadow">
                            <div className="card-body">
                                <h5>Total Policies</h5>
                                <h2>{policies.length}</h2>
                            </div>
                        </div>
                    </div>

                </div>

                <div className="card shadow">

                    <div className="card-header">
                        <h4>Your Policies</h4>
                    </div>

                    <div className="card-body">

                        <table className="table table-hover">

                            <thead className="table-dark">
                                <tr>
                                    <th>Policy No</th>
                                    <th>Policy Type</th>
                                    <th>Premium</th>
                                    <th>Maturity Date</th>
                                </tr>
                            </thead>

                            <tbody>

                                {policies.map((policy) => (
                                    <tr key={policy.policy_number}>
                                        <td>{policy.policy_number}</td>
                                        <td>{policy.policy_type}</td>
                                        <td>₹ {policy.premium_amount}</td>
                                        <td>{policy.date_of_maturity}</td>
                                    </tr>
                                ))}

                            </tbody>

                        </table>

                    </div>

                </div>

            </div>

        </div>
    );
}

export default CustomerDashboard;