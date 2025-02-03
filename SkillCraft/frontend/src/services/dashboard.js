import api from './api';

export const dashboardService = {
  getOverview: async () => {
    const response = await api.get('/dashboard/overview');
    return response.data;
  },
  
  getGoals: async () => {
    const response = await api.get('/dashboard/goals');
    return response.data;
  },
  
  createGoal: async (goalData) => {
    const response = await api.post('/dashboard/goals', goalData);
    return response.data;
  }
}; 