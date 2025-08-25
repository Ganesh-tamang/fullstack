import React, { useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { refreshAccessToken } from "./state/refreshToken";

import Navbar from "./components/NavBar";
import Register from "./components/Register_page";
import Login from "./components/Login";
import CreatePost from "./components/CreatePost";
import Posts from "./components/Posts";
import PostDetail from "./components/PostDetail";
import ProtectedRoute from "./components/ProtectedRoute";
import NotFound from "./components/NotFound";
function App() {
  const dispatch = useDispatch();
  const { refresh } = useSelector((state) => state.auth);
  useEffect(() => {
    if (!refresh) return;

    const interval = setInterval(() => {
      refreshAccessToken(dispatch, refresh);
    }, 50 * 60 * 1000); // every 50 minutes

    return () => clearInterval(interval);
  }, [refresh, dispatch]);
 
  return (
    <Router>
      <Navbar />
      <div className="p-6">
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/create-post" element={ <ProtectedRoute>
                <CreatePost />
              </ProtectedRoute>} />
          <Route path="/" element={ <ProtectedRoute>
                <Posts />
              </ProtectedRoute>} />
          <Route path="/posts/:id" element={ <ProtectedRoute>
                <PostDetail />
              </ProtectedRoute>} />
        <Route path="*" element={<NotFound />} />
          
        </Routes>
      </div>
    </Router>
  );
}

export default App;
