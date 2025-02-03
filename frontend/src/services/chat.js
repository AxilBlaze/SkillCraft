import api from './api';

export const chatService = {
  sendMessage: async (message) => {
    const response = await api.post('/tutor/chat', { message });
    return response.data;
  },
  
  getHistory: async () => {
    const response = await api.get('/tutor/history');
    return response.data;
  }
}; 