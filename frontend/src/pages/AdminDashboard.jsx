import { useEffect, useState } from "react";
import api from "../services/api";

function AdminDashboard() {

    const [stats, setStats] = useState(null);

    useEffect(() => {

        api.get("/dashboard/stats")
            .then((response) => {
                console.log(response.data);
                setStats(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }, []);


    if (!stats) {
        return <h3>Loading...</h3>;
    }


    return (
        <div className="container mt-5">

            <h2>
                LIC Admin Dashboard
            </h2>


            <div className="row mt-4">

                <div className="col-md-4">
                    <div className="card p-3">
                        <h5>Total Customers</h5>
                        <h2>{stats.total_customers}</h2>
                    </div>
                </div>


                <div className="col-md-4">
                    <div className="card p-3">
                        <h5>Total Policies</h5>
                        <h2>{stats.total_policies}</h2>
                    </div>
                </div>


                <div className="col-md-4">
                    <div className="card p-3">
                        <h5>Average Age</h5>
                        <h2>{stats.average_age}</h2>
                    </div>
                </div>

            </div>

        </div>
    );
}

export default AdminDashboard;