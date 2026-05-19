import api from './api';

export const loginUser = (payload) => api.post('/auth/login/', payload);
export const registerUser = (payload) => api.post('/auth/register/', payload);
export const refreshToken = (payload) => api.post('/auth/token/refresh/', payload);
export const fetchMe = () => api.get('/auth/me/');
