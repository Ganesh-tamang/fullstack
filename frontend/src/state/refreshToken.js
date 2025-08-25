import { setTokens, clearTokens } from "../state/authSlice";

export const refreshAccessToken = async (dispatch, refresh) => {
  try {
    const res = await fetch("http://localhost:8000/refresh", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh }),
    });

    if (!res.ok) throw new Error("Failed to refresh");

    const data = await res.json();
    dispatch(setTokens(data)); // {access, refresh}
    return data.access;
  } catch (err) {
    console.error("Token refresh failed:", err);
    dispatch(clearTokens());
    return null;
  }
};
