import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from '@/context/AuthContext';
import { useAuth } from '@/hooks/useAuth';
import Navbar from '@/components/common/Navbar';
import Login from '@/components/Auth/Login';
import Register from '@/components/Auth/Register';
import DashboardOverview from '@/components/Dashboard/Overview';
import PathView from '@/components/LearningPath/PathView';
import ChatInterface from '@/components/Chat/ChatInterface';

const PrivateRoute = ({ children }) => {
  const { user, loading } = useAuth();
  
  if (loading) return <div>Loading...</div>;
  if (!user) return <Navigate to="/login" />;
  
  return children;
};

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <div className="min-h-screen bg-gray-100">
          <Navbar />
          <main className="container mx-auto px-4 py-8">
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/" element={
                <PrivateRoute>
                  <DashboardOverview />
                </PrivateRoute>
              } />
              <Route path="/learning-path" element={
                <PrivateRoute>
                  <PathView />
                </PrivateRoute>
              } />
              <Route path="/chat" element={
                <PrivateRoute>
                  <ChatInterface />
                </PrivateRoute>
              } />
            </Routes>
          </main>
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;



