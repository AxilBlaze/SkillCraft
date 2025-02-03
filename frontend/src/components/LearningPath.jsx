import React from 'react';
import { motion } from 'framer-motion';

const LearningPath = () => {
  const paths = [
    {
      title: "Web Development",
      progress: 65,
      image: "🌐",
      stages: [
        {
          name: "Frontend Fundamentals",
          completed: true,
          skills: ["HTML5", "CSS3", "JavaScript ES6+"]
        },
        {
          name: "React Ecosystem",
          completed: true,
          skills: ["React.js", "Redux", "React Router"]
        },
        {
          name: "Backend Development",
          active: true,
          skills: ["Node.js", "Express", "MongoDB"]
        },
        {
          name: "Advanced Topics",
          skills: ["AWS", "Docker", "CI/CD"]
        }
      ]
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-black text-white p-6">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="max-w-7xl mx-auto"
      >
        {/* Header Section */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-pink-600 bg-clip-text text-transparent mb-4">
            Your Learning Journey
          </h1>
          <p className="text-gray-400">Master modern web development step by step</p>
        </div>

        {/* Main Path Display */}
        {paths.map((path, pathIndex) => (
          <div key={pathIndex} className="mb-16">
            {/* Path Header */}
            <div className="flex items-center justify-between mb-8 bg-white/5 p-6 rounded-2xl backdrop-blur-lg">
              <div className="flex items-center gap-4">
                <span className="text-4xl">{path.image}</span>
                <div>
                  <h2 className="text-2xl font-bold">{path.title}</h2>
                  <p className="text-purple-400">{path.progress}% Complete</p>
                </div>
              </div>
              <div className="w-32 h-32 relative">
                <svg className="transform -rotate-90 w-32 h-32">
                  <circle
                    cx="64"
                    cy="64"
                    r="60"
                    stroke="currentColor"
                    strokeWidth="8"
                    fill="transparent"
                    className="text-white/10"
                  />
                  <circle
                    cx="64"
                    cy="64"
                    r="60"
                    stroke="currentColor"
                    strokeWidth="8"
                    fill="transparent"
                    strokeDasharray={`${2 * Math.PI * 60}`}
                    strokeDashoffset={`${2 * Math.PI * 60 * (1 - path.progress / 100)}`}
                    className="text-purple-500 transition-all duration-1000"
                  />
                </svg>
                <span className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-2xl font-bold">
                  {path.progress}%
                </span>
              </div>
            </div>

            {/* Stages Timeline */}
            <div className="relative">
              <div className="absolute left-8 top-0 bottom-0 w-1 bg-gradient-to-b from-purple-500 to-pink-500 rounded-full" />
              
              {path.stages.map((stage, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.2 }}
                  className="relative pl-20 pb-12 last:pb-0"
                >
                  {/* Stage Marker */}
                  <div className={`absolute left-8 w-4 h-4 rounded-full transform -translate-x-1/2 -translate-y-1/2
                    ${stage.completed ? 'bg-green-500' : 
                      stage.active ? 'bg-purple-500 animate-pulse' : 'bg-white/30'}`}
                  />

                  {/* Stage Content */}
                  <motion.div
                    whileHover={{ scale: 1.02 }}
                    className={`bg-white/5 p-6 rounded-2xl border border-white/10 backdrop-blur-sm
                      ${stage.active ? 'ring-2 ring-purple-500' : ''}`}
                  >
                    <div className="flex justify-between items-center mb-4">
                      <h3 className="text-xl font-semibold">{stage.name}</h3>
                      {stage.completed && (
                        <span className="text-green-500 flex items-center gap-2">
                          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                          </svg>
                          Completed
                        </span>
                      )}
                    </div>

                    <div className="flex flex-wrap gap-2 mb-4">
                      {stage.skills.map((skill, skillIndex) => (
                        <span
                          key={skillIndex}
                          className="px-3 py-1 bg-white/10 rounded-full text-sm font-medium"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>

                    <motion.button
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                      className={`w-full py-2 rounded-xl font-medium transition-all
                        ${stage.completed ? 'bg-green-500/20 text-green-300' :
                          stage.active ? 'bg-gradient-to-r from-purple-500 to-pink-500' :
                          'bg-white/10 text-gray-400'}`}
                    >
                      {stage.completed ? 'Review Materials' :
                       stage.active ? 'Continue Learning' :
                       'Start This Section'}
                    </motion.button>
                  </motion.div>
                </motion.div>
              ))}
            </div>
          </div>
        ))}

        {/* Achievement Badges */}
        <div className="mt-12">
          <h3 className="text-2xl font-bold mb-6 text-center">Your Achievements</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {['🏆', '⭐', '🎯', '🚀'].map((emoji, index) => (
              <motion.div
                key={index}
                whileHover={{ scale: 1.05 }}
                className="bg-white/5 p-6 rounded-2xl text-center backdrop-blur-sm"
              >
                <span className="text-4xl mb-2 block">{emoji}</span>
                <span className="text-sm text-gray-400">Achievement {index + 1}</span>
              </motion.div>
            ))}
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default LearningPath;