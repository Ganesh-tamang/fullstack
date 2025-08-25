import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function PostDetail() {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:8000/posts/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setPost(data);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-10 w-10 border-t-4 border-blue-500"></div>
      </div>
    );
  }

  if (!post) return <p className="text-center text-gray-500">Post not found</p>;

  return (
    <div className="max-w-2xl mx-auto bg-white shadow-lg rounded-2xl p-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">{post.title}</h2>
      <p className="text-gray-700 leading-relaxed mb-6">{post.content}</p>

      <div className="border-t pt-4 text-sm text-gray-500">
        <p>
          Author: <span className="font-semibold text-gray-800">{post.author}</span>
        </p>
        <p className="mt-1">
          Created:{" "}
          {new Date(post.created_at).toLocaleString("en-US", {
            dateStyle: "medium",
            timeStyle: "short",
          })}
        </p>
        <p>
          Updated:{" "}
          {new Date(post.updated_at).toLocaleString("en-US", {
            dateStyle: "medium",
            timeStyle: "short",
          })}
        </p>
      </div>
    </div>
  );
}
