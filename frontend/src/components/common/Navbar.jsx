import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';

const Navbar = () => {
  const { user, logout } = useAuth();

  return (
    <nav className="bg-white shadow">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex">
            <Link to="/" className="flex-shrink-0 flex items-center">
              SkillCraft
            </Link>
            {user && (
              <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                <Link to="/" className="px-3 py-2 text-sm font-medium">
                  Dashboard
                </Link>
                <Link to="/learning-path" className="px-3 py-2 text-sm font-medium">
                  Learning Path
                </Link>
                <Link to="/chat" className="px-3 py-2 text-sm font-medium">
                  Chat
                </Link>
              </div>
            )}
          </div>
          <div className="flex items-center">
            {user ? (
              <button
                onClick={logout}
                className="px-3 py-2 text-sm font-medium text-red-600"
              >
                Logout
              </button>
            ) : (
              <Link to="/login" className="px-3 py-2 text-sm font-medium">
                Login
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 