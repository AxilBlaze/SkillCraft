// AiTutor.jsx
import { useState } from "react";
import { motion } from "framer-motion";

const AITutor = () => {
  const [activeTab, setActiveTab] = useState("Chat");

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-black text-white">
      {/* Glassmorphism Header */}
      <div className="backdrop-blur-lg bg-white/10 p-6 border-b border-white/20">
        <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-pink-600 bg-clip-text text-transparent">
          AI Tutor
        </h1>
      </div>

      {/* Main Content */}
      <div className="container mx-auto p-6">
        {/* Navigation Tabs */}
        <div className="flex gap-4 mb-8">
          {[
            "Chat",
            "History",
            "Feedback"
          ].map((tab) => (
            <motion.button 
              key={tab}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className={`px-6 py-3 rounded-xl transition-all duration-300 ${
                activeTab === tab 
                  ? "bg-gradient-to-r from-purple-500 to-pink-500 shadow-lg shadow-purple-500/30" 
                  : "bg-white/10 hover:bg-white/20"
              }`}
              onClick={() => setActiveTab(tab)}
            >
              {tab}
            </motion.button>
          ))}
        </div>

        {/* Stats Overview */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="backdrop-blur-lg bg-white/10 p-6 rounded-2xl"
          >
            <h3 className="text-lg text-gray-300">Sessions Completed</h3>
            <p className="text-3xl font-bold">24</p>
          </motion.div>
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="backdrop-blur-lg bg-white/10 p-6 rounded-2xl"
          >
            <h3 className="text-lg text-gray-300">Average Rating</h3>
            <p className="text-3xl font-bold">4.8</p>
          </motion.div>
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="backdrop-blur-lg bg-white/10 p-6 rounded-2xl"
          >
            <h3 className="text-lg text-gray-300">Learning Hours</h3>
            <p className="text-3xl font-bold">48</p>
          </motion.div>
        </div>

        {/* Content Section */}
        <motion.div
          key={activeTab}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          transition={{ duration: 0.3 }}
          className="backdrop-blur-lg bg-white/10 p-6 rounded-2xl"
        >
          {activeTab === "Chat" && <ChatSection />}
          {activeTab === "History" && <HistorySection />}
          {activeTab === "Feedback" && <FeedbackSection />}
        </motion.div>
      </div>
    </div>
  );
};

// ... previous imports and code remain the same ...

const ChatSection = () => {
  const [messages, setMessages] = useState([
    {
      type: 'system',
      content: 'Hi! I\'m your AI learning assistant. Ask me any questions about programming concepts!'
    }
  ]);
  const [inputMessage, setInputMessage] = useState('');

  const handleSendMessage = () => {
    if (!inputMessage.trim()) return;
    
    setMessages(prev => [...prev, {
      type: 'user',
      content: inputMessage
    }]);
    
    // Simulated AI response - in real implementation, this would be connected to your backend
    setTimeout(() => {
      setMessages(prev => [...prev, {
        type: 'assistant',
        content: "I'll help you understand that concept. Let me break it down..."
      }]);
    }, 1000);
    
    setInputMessage('');
  };

  return (
    <div className="space-y-4">
      <div className="flex flex-col h-[600px]">
        {/* Chat Messages Area */}
        <div className="flex-1 overflow-y-auto space-y-4 mb-4 p-4">
          {messages.map((message, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div className={`
                p-4 rounded-xl max-w-[80%] 
                ${message.type === 'user' 
                  ? 'bg-gradient-to-r from-purple-500 to-pink-500' 
                  : 'bg-white/10'
                }
              `}>
                <p className="text-white">{message.content}</p>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Quick Questions Suggestions */}
        <div className="flex gap-2 mb-4 overflow-x-auto pb-2">
          {[
            "Explain React Hooks",
            "What is state management?",
            "How does async/await work?",
            "Explain REST APIs"
          ].map((question) => (
            <motion.button
              key={question}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-4 py-2 bg-white/10 rounded-full text-sm whitespace-nowrap hover:bg-white/20"
              onClick={() => setInputMessage(question)}
            >
              {question}
            </motion.button>
          ))}
        </div>

        {/* Input Area */}
        <div className="flex gap-2 bg-white/5 p-4 rounded-xl">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            className="flex-1 bg-white/10 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-500"
            placeholder="Ask any programming concept..."
          />
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleSendMessage}
            className="px-6 py-2 bg-gradient-to-r from-purple-500 to-pink-500 rounded-xl font-medium"
          >
            Send
          </motion.button>
        </div>
      </div>

      {/* Features Section */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
        <div className="bg-white/5 p-4 rounded-xl">
          <h3 className="font-medium mb-2 text-purple-300">Concept Explanations</h3>
          <p className="text-sm text-gray-400">
            Get detailed explanations of programming concepts with examples
          </p>
        </div>
        <div className="bg-white/5 p-4 rounded-xl">
          <h3 className="font-medium mb-2 text-purple-300">Code Reviews</h3>
          <p className="text-sm text-gray-400">
            Share your code to get instant feedback and suggestions
          </p>
        </div>
        <div className="bg-white/5 p-4 rounded-xl">
          <h3 className="font-medium mb-2 text-purple-300">Practice Problems</h3>
          <p className="text-sm text-gray-400">
            Get personalized coding challenges based on your level
          </p>
        </div>
      </div>
    </div>
  );
};

// ... rest of the components remain the same ...

const FeedbackSection = () => (
  <div className="space-y-4">
    <h2 className="text-2xl font-semibold mb-4">Session Feedback</h2>
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      {[
        { topic: 'React Fundamentals', rating: '5/5', feedback: 'Excellent explanation of concepts' },
        { topic: 'JavaScript ES6', rating: '4.5/5', feedback: 'Very helpful examples' },
        { topic: 'API Design', rating: '4.8/5', feedback: 'Clear and concise teaching' },
      ].map((feedback) => (
        <motion.div
          key={feedback.topic}
          whileHover={{ scale: 1.02 }}
          className="bg-white/5 p-4 rounded-xl space-y-2"
        >
          <div className="flex justify-between items-center">
            <h3 className="font-medium">{feedback.topic}</h3>
            <span className="text-purple-400">{feedback.rating}</span>
          </div>
          <p className="text-sm text-gray-400">{feedback.feedback}</p>
        </motion.div>
      ))}
    </div>
  </div>
);

export default AITutor;