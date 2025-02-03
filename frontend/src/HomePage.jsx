import React from 'react';

const HomePage = () => {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-700 to-black text-white flex flex-col items-center justify-center p-6 relative">
        {/* Navigation Bar */}
        {/* Top Navigation */}
      <nav className="absolute top-5 right-10 flex space-x-6 text-gray-300 text-lg font-bold">
        <a href="#" className="hover:text-white transition" >Dashboard </a>
        <a href="#" className="hover:text-white transition">Chat Interface</a>
        <a href="#" className="hover:text-white transition">Message History</a>
        <a href="#" className="hover:text-white transition">AI-tutor</a>
      </nav>
  
        {/* White Light Effect in the Center */}
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="w-[40rem] h-[40rem] bg-white rounded-full opacity-50 blur-[6rem]"></div>
        </div>
  
        {/* Violet Shading on Right Edge */}
        <div className="absolute right-0 top-0 bottom-0 w-1/4 bg-purple-500 opacity-40 blur-[6rem]"></div>
  
        {/* Content */}
        <div className="max-w-4xl text-center relative z-10 mt-16">
          <h1 className="text-4xl font-bold">Adaptive Learning</h1>
          <h2 className="text-2xl font-semibold mt-2">
            Learn and Grow with AI
          </h2>
          <p className="mt-4 text-gray-300 max-w-lg mx-auto">
            Your personalized AI tutor for all domains
          </p>
          <button className="mt-6 px-6 py-2 bg-black rounded-full text-white font-medium border border-white hover:bg-white hover:text-black transition-all">
            Start Learning
          </button>
        </div>
  
        
  
        {/* Stats Section */}
        
        <div className="flex mt-12 space-x-6 relative z-10">
          <div className="bg-black p-6 rounded-xl text-center">
            <h3 className="text-2xl font-bold text-purple-300">Personalized Goals</h3>
            <p className="text-gray-300"></p>
          </div>
          
          <div className="bg-black p-6 rounded-xl text-center">
            <h3 className="text-2xl font-bold text-purple-300">Know your Learning Progress</h3>
            <p className="text-gray-300"></p>
          </div>
        

        <div className="bg-black p-6 rounded-xl text-center">
            <h3 className="text-2xl font-bold text-purple-300">AI Recommendations</h3>
            <p className="text-gray-300"></p>
          </div>

          <div className="bg-black p-6 rounded-xl text-center">
            <h3 className="text-2xl font-bold text-purple-300">Analyze your Skill Gap</h3>
            <p className="text-gray-300"></p>
          </div>

          <div className="bg-black p-6 rounded-xl text-center">
            <h3 className="text-2xl font-bold text-purple-300">Practice Exercises and feedback</h3>
            <p className="text-gray-300"></p>
          </div>
        </div>

        
        {/* Avatar Icons */}
        <div className="flex mt-6 space-x-4 relative z-10">
          <img src="https://via.placeholder.com/40" alt="avatar" className="rounded-full" />
          <img src="https://via.placeholder.com/40" alt="avatar" className="rounded-full" />
          <img src="https://via.placeholder.com/40" alt="avatar" className="rounded-full" />
        </div>
      </div>
    );
  };
  
  export default HomePage;
