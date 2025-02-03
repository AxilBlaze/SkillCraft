import { Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Dashboard from "./components/Dashboard";
import AITutor from "./components/AITutor";
import LearningPath from "./components/LearningPath";
function App() {
  return (
    
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/AITutor" element={<AITutor />} />
        <Route path="/LearningPath" element={<LearningPath />} />
      </Routes>
  
  );
}

export default App;
