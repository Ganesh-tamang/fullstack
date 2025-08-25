import React from "react";
import { useSelector } from "react-redux";
import { Navigate } from "react-router-dom";

export default function ProtectedRoute({ children }) {
  const { access } = useSelector((state) => state.auth);

  if (!access) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
