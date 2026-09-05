import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import AgentLogin from "./pages/AgentLogin";
import AgentRegister from "./pages/AgentRegister";
import AgentDashboard from "./pages/AgentDashboard";
import Customers from "./pages/Customers";
import Policies from "./pages/Policies";
import Analytics from "./pages/Analytics";
import Chatbot from "./pages/Chatbot";
import CustomerLogin from "./pages/CustomerLogin";
import CustomerDashboard from "./pages/CustomerDashboard";
import AdminDashboard from "./pages/AdminDashboard";
import CustomerRegister from "./pages/CustomerRegister";
function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Home/>}/>

        <Route path="/agent-login" element={<AgentLogin />} />

        <Route path="/agent-dashboard" element={<AgentDashboard />} />

        <Route path="/register" element={<AgentRegister />} />

        <Route path="/customers" element={<Customers/>}/>

        <Route path="/policies" element={<Policies/>}/>

        <Route path="/analytics" element={<Analytics/>}/>

        <Route path="/chatbot" element={<Chatbot/>}/>
        <Route path="/customer-login" element={<CustomerLogin />}/>
        <Route path="/customer-register" element={<CustomerRegister />} />
        <Route path="/customer-dashboard" element={<CustomerDashboard />}
        />
        <Route path="/admin-dashboard" element={<AdminDashboard />} 
/>

      </Routes>

    </BrowserRouter>

  );

}

export default App;