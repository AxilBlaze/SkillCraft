// AiTutor.jsx
import { useState } from "react";

export default function AiTutor() {
  const [showChat, setShowChat] = useState(false);
  const [showHistory, setShowHistory] = useState(false);
  const [showFeedback, setShowFeedback] = useState(false);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">AI Tutor</h2>
      <div className="flex gap-4 mt-4">
        <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={() => setShowChat(true)}>Chat Interface</button>
        <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={() => setShowHistory(true)}>Message History</button>
        <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={() => setShowFeedback(true)}>Adaptive Feedback</button>
      </div>
      {showChat && (
        <div className="fixed inset-0 bg-white p-4 shadow-lg rounded-xl">
          <h2 className="text-xl font-semibold">Chat Box</h2>
          <button className="bg-red-500 text-white px-4 py-2 rounded" onClick={() => setShowChat(false)}>Close</button>
        </div>
      )}
      {showHistory && (
        <div className="fixed inset-0 bg-white p-4 shadow-lg rounded-xl">
          <h2 className="text-xl font-semibold">Message History</h2>
          <p>All previous messages appear here.</p>
          <button className="bg-red-500 text-white px-4 py-2 rounded" onClick={() => setShowHistory(false)}>Close</button>
        </div>
      )}
      {showFeedback && (
        <div className="fixed inset-0 bg-white p-4 shadow-lg rounded-xl">
          <h2 className="text-xl font-semibold">Adaptive Feedback</h2>
          <p>Feedback based on your learning behavior.</p>
          <button className="bg-red-500 text-white px-4 py-2 rounded" onClick={() => setShowFeedback(false)}>Close</button>
        </div>
      )}
    </div>
  );
}