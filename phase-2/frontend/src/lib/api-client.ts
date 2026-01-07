import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'https://phase-02-backend-production.up.railway.app/api/v1';

// Define types locally to avoid import issues
type AxiosInstance = any;
type AxiosRequestConfig = any;
type AxiosResponse<T = any> = {
  data: T;
  status: number;
  statusText: string;
  headers: any;
  config: any;
};

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Request interceptor to inject JWT token
    this.client.interceptors.request.use(
      (config: AxiosRequestConfig) => {
        const token = localStorage.getItem('access_token');
        if (token && config.headers) {
          config.headers = {
            ...config.headers,
            Authorization: `Bearer ${token}`,
          };
        }
        return config;
      },
      (error: any) => {
        return Promise.reject(error);
      }
    );

    // Response interceptor to handle token expiration
    this.client.interceptors.response.use(
      (response: AxiosResponse) => {
        return response;
      },
      (error: any) => {
        if (error.response?.status === 401) {
          // Token might be expired, clear it and redirect to login
          localStorage.removeItem('access_token');
          // Optionally redirect to login page
          // window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }

  // Auth API methods
  register = (email: string, password: string, fullName: string) => {
    return this.client.post('/auth/register', { email, password, full_name: fullName });
  };

  login = (email: string, password: string) => {
    return this.client.post('/auth/login', { email, password });
  };

  // Explicitly typed login method for type safety
  loginTyped = async (email: string, password: string): Promise<{ data: { access_token: string; token_type: string } }> => {
    const response = await this.client.post('/auth/login', { email, password });
    return response as { data: { access_token: string; token_type: string } };
  };

  // Explicitly typed register method for type safety
  registerTyped = async (email: string, password: string, fullName: string): Promise<{ data: { access_token: string; token_type: string } }> => {
    const response = await this.client.post('/auth/login', { email, password }); // After registration, login to get token
    return response as { data: { access_token: string; token_type: string } };
  };

  getCurrentUser = () => {
    return this.client.get('/auth/me');
  };

  // Task API methods
  getTasks = () => {
    return this.client.get('/tasks/');
  };

  // --- ADDED STATS ENDPOINT ---
  getStats = () => {
    return this.client.get('/tasks/stats');
  };

  // --- UPDATED TO ACCEPT TAGS ---
  createTask = (taskData: { 
    title: string; 
    description?: string; 
    status?: string; 
    priority?: string; 
    due_date?: string | null; // Fixed: Allow null
    tags?: string | null 
  }) => {
    return this.client.post('/tasks/', taskData);
  };

  updateTask = (id: string, taskData: { 
    title?: string; 
    description?: string; 
    status?: string; 
    priority?: string; 
    due_date?: string | null; // Fixed: Allow null
    tags?: string | null 
  }) => {
    return this.client.put(`/tasks/${id}`, taskData);
  };

  deleteTask = (id: string) => {
    return this.client.delete(`/tasks/${id}`);
  };
}

export const apiClient = new ApiClient();
export default ApiClient;
