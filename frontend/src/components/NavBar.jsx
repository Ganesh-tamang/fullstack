// Navbar.jsx
import React from "react";
import { Link, useNavigate,useLocation } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { clearTokens } from "../state/authSlice";

export default function Navbar() {
  const location = useLocation();
  const hideNavbarOn = ["/login", "/register"];

  if (hideNavbarOn.includes(location.pathname)) {
    return null;
  }

  const { access, username } = useSelector((state) => state.auth);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(clearTokens());
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("username");
    navigate("/login"); 
  };

  return (
    <nav className="p-4 bg-black text-white flex gap-6 justify-end font-medium">
      {!access ? (
        <>
          <Link to="/register">Register</Link>
          <Link to="/login">Login</Link>
        </>
      ) : (
        <>
          <span className="mr-auto font-semibold"> Hi, {username}</span>
          <Link to="/">Posts</Link>
          <Link to="/create-post">Create Post</Link>
          <button
            onClick={handleLogout}
            className="bg-red-500 px-3 py-1 rounded hover:bg-red-600 transition"
          >
            Logout
          </button>
        </>
      )}
    </nav>
  );
}
