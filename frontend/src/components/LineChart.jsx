import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

// Register necessary chart elements
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const LineChart = () => {
  // Data for the line chart with two datasets
  const data = {
    labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'], // Weeks for the x-axis
    datasets: [
      {
        label: 'Learning Progress (%)',
        data: [60, 70, 75, 80],  // Example data for learning progress
        borderColor: 'rgb(244, 63, 94)',  // Line color for progress
        backgroundColor: 'rgba(244, 63, 94, 0.2)',
        fill: true,
        tension: 0.4,
        borderWidth: 2,
      },
      {
        label: 'Understanding Level (%)',
        data: [50, 60, 70, 85],  // Example data for understanding level
        borderColor: 'rgb(53, 162, 235)', // Line color for understanding level
        backgroundColor: 'rgba(53, 162, 235, 0.2)',
        fill: false,
        tension: 0.4,
        borderWidth: 2,
        borderDash: [5, 5], // Dashed line for understanding level
      },
      {
        label: 'Hours Devoted (hrs)',
        data: [5, 6, 7, 8],  // Example data for hours devoted
        borderColor: 'rgb(255, 159, 64)',  // Line color for hours devoted
        backgroundColor: 'rgba(255, 159, 64, 0.2)',
        fill: false,
        tension: 0.4,
        borderWidth: 2,
        borderDash: [10, 5], // Dashed line for hours
      },
    ],
  };

  // Options for customizing the chart
  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Learning Analytics: Progress, Understanding & Hours',
        font: {
          size: 18,
        },
      },
      tooltip: {
        mode: 'index',
        intersect: false,
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Weeks',
        },
      },
      y: {
        title: {
          display: true,
          text: 'Value (%) / Hours',
        },
        min: 0,
        max: 100,
      },
    },
  };

  return (
    <div className="backdrop-blur-lg bg-white/10 p-6 rounded-2xl">
      <h3 className="text-lg text-gray-300 mb-4">Learning Progress, Understanding Level & Hours Devoted</h3>
      <Line data={data} options={options} />
    </div>
  );
};

export default LineChart;
