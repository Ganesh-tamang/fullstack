import React, { useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

export default function CreatePost() {
  const [form, setForm] = useState({ title: "", content: "" });
  const [error, setError] = useState("");
  const { access, username } = useSelector((state) => state.auth); // ✅ username
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await fetch("http://localhost:8000/posts/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${access}`,
        },
        body: JSON.stringify({
          ...form,
          author: username,
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.detail || "Failed to create post");
        return;
      }

      navigate("/posts");
    } catch (err) {
      setError("Something went wrong. Please try again.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-black p-8 text-black">
      <form
        onSubmit={handleSubmit}
        className="bg-white shadow-lg rounded-xl p-6 w-full max-w-md"
      >
        <h2 className="text-2xl font-bold mb-4 text-gray-800">Create Post</h2>

        {error && (
          <p className="text-red-500 text-sm mb-3 border border-red-300 p-2 rounded">
            {error}
          </p>
        )}

        <label className="block mb-2 text-sm font-medium text-gray-700">
          Title
        </label>
        <input
          name="title"
          placeholder="Enter title"
          onChange={handleChange}
          className="w-full p-2 border rounded-lg mb-4 focus:ring-2 focus:ring-blue-500"
          required
        />

        <label className="block mb-2 text-sm font-medium text-gray-700">
          Content
        </label>
        <textarea
          name="content"
          placeholder="Write your content..."
          onChange={handleChange}
          className="w-full p-2 border rounded-lg mb-4 focus:ring-2 focus:ring-blue-500 h-32"
          required
        />

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition"
        >
          Create Post
        </button>
      </form>
    </div>
  );
}
