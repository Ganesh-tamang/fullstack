import { createSlice } from "@reduxjs/toolkit";

const accessToken = localStorage.getItem("access") || null;
const refreshToken = localStorage.getItem("refresh") || null;
const username = localStorage.getItem("username") || null;

const authSlice = createSlice({
  name: "auth",
  initialState: {
    access: accessToken,
    refresh: refreshToken,
    isAuthenticated: !!accessToken,
    username: username,
  },
  reducers: {
    setTokens: (state, action) => {
      const { access, refresh, username } = action.payload;
      state.access = access;
      state.refresh = refresh;
      state.isAuthenticated = true;
      state.username = username;
      localStorage.setItem("access", access);
      localStorage.setItem("refresh", refresh);
      localStorage.setItem("username", username);
    },
    clearTokens: (state) => {
      state.access = null;
      state.refresh = null;
      state.isAuthenticated = false;
      state.username = null;
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      localStorage.removeItem("username");
    },
  },
});

export const { setTokens, clearTokens } = authSlice.actions;
export default authSlice.reducer;
