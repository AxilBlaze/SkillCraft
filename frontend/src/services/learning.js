import api from './api';

export const learningService = {
  getPath: async () => {
    const response = await api.get('/learning-path/path');
    return response.data;
  },
  
  submitAssessment: async (data) => {
    const response = await api.post('/learning-path/assessment', data);
    return response.data;
  },
  
  updateMilestone: async (milestoneId, data) => {
    const response = await api.put(`/learning-path/milestone/${milestoneId}`, data);
    return response.data;
  }
}; 