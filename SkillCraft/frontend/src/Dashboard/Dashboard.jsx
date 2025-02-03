// Dashboard.jsx
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, Tooltip, Legend } from 'chart.js';
import { ArcElement } from "chart.js";



import { motion } from "framer-motion";

// Register Chart.js components
ChartJS.register(ArcElement, Tooltip, Legend);

export default function Dashboard() {
  const data = {
    labels: ["Completed", "In Progress", "Pending"],
    datasets: [
      {
        data: [60, 30, 10],
        backgroundColor: ["#4CAF50", "#FFC107", "#F44336"],
      },
    ],
  };

  return (
    <div className="p-6 grid gap-6">
      <motion.h1 className="text-2xl font-bold" animate={{ scale: 1.1 }}>
        Dashboard
      </motion.h1>
      <div className="bg-white p-4 shadow-lg rounded-xl">
        <h2 className="text-xl font-semibold">Personalized Goals</h2>
        <Pie data={data} />
      </div>
      <div className="bg-white p-4 shadow-lg rounded-xl">
        <h2 className="text-xl font-semibold">Learning Progress</h2>
        <p>Track your learning journey effectively.</p>
      </div>
      <div className="bg-white p-4 shadow-lg rounded-xl">
        <h2 className="text-xl font-semibold">AI Recommendations</h2>
        <p>Personalized suggestions based on your learning pattern.</p>
      </div>
      <div className="bg-white p-4 shadow-lg rounded-xl">
        <h2 className="text-xl font-semibold">Skill Gap Analysis</h2>
        <p>Identify the skills you need to improve.</p>
      </div>
      <div className="bg-white p-4 shadow-lg rounded-xl">
        <h2 className="text-xl font-semibold">Next Step Suggestions</h2>
        <p>Recommended actions to reach your learning goals.</p>
      </div>
    </div>
  );
}
