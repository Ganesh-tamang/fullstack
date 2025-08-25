import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Posts() {
  const [posts, setPosts] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://localhost:8000/posts")
      .then((res) => res.json())
      .then((data) => setPosts(data))
      .catch(() => setPosts([]));
  }, []);

  return (
    <div className="min-h-screen bg-black p-8">
      <div className="max-w-4xl mx-auto bg-white shadow-lg rounded-2xl p-6">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold text-gray-800">All Posts</h2>
          <button
            onClick={() => navigate("/create-post")}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition"
          >
            + Create Post
          </button>
        </div>

        {posts.length === 0 ? (
          <p className="text-gray-500 text-center py-6">
            No posts available. Be the first to create one!
          </p>
        ) : (
          <ul className="space-y-4">
            {posts.map((p) => (
              <li
                key={p.id}
                className="p-4 border rounded-lg hover:shadow-md transition bg-gray-50"
              >
                <Link
                  to={`/posts/${p.id}`}
                  className="text-lg font-semibold text-blue-600 hover:underline"
                >
                  {p.title}
                </Link>
                <p className="text-sm text-gray-600">
                  by <span className="font-medium">{p.author}</span>
                </p>
                <p className="text-gray-700 mt-2 line-clamp-2">
                  {p.content.slice(0, 100)}...
                </p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
