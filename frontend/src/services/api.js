import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const loginUser = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}/login`, credentials);
    return response;
  } catch (error) {
    throw error;
  }
};

export const fetchChatResponse = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/chat`, { message });
    console.log('Response from API:', response);  // Log the API response
    return response;
  } catch (error) {
    console.error('Error during API call:', error);
    throw error;
  }
};
