import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { fetchMe, loginUser, registerUser } from '../services/authService';

const initialState = {
  user: null,
  loading: false,
  error: null,
};

export const login = createAsyncThunk('auth/login', async (payload) => {
  const { data } = await loginUser(payload);
  localStorage.setItem('access_token', data.access);
  localStorage.setItem('refresh_token', data.refresh);
  const me = await fetchMe();
  return me.data;
});

export const register = createAsyncThunk('auth/register', async (payload) => {
  const { data } = await registerUser(payload);
  localStorage.setItem('access_token', data.access);
  localStorage.setItem('refresh_token', data.refresh);
  return data.user;
});

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    logout(state) {
      state.user = null;
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    },
    setUser(state, action) {
      state.user = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload;
      })
      .addCase(login.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })
      .addCase(register.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(register.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload;
      })
      .addCase(register.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export const { logout, setUser } = authSlice.actions;
export default authSlice.reducer;
