"use client";

import { useState, useEffect } from "react";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../../lib/firebase";
import { useRouter } from "next/navigation";
import { useAuth } from "../../context/AuthContext";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const router = useRouter();
  const { user, loading } = useAuth();

  useEffect(() => {
    if (user && !loading) {
      router.push("/admin");
    }
  }, [user, loading, router]);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setIsSubmitting(true);

    try {
      await signInWithEmailAndPassword(auth, email, password);
      router.push("/admin");
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message || "Failed to login. Please check your credentials.");
      } else {
        setError("Failed to login. Please check your credentials.");
      }
      console.error("Login error:", err);
    } finally {
      setIsSubmitting(false);
    }
  };

  if (loading) {
     return <div className="min-h-screen bg-black flex items-center justify-center text-green-500 font-mono">Checking authentication state...</div>;
  }

  return (
    <div className="min-h-screen bg-black flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-md bg-gray-900 border border-gray-700 p-8 rounded-lg shadow-xl">
        <div className="text-center mb-8">
          <h1 className="text-xl font-bold font-mono tracking-wider text-green-500 uppercase">
            Sovereign Workspace
          </h1>
          <p className="text-xs font-mono text-gray-500 mt-2">v1.0.0-STRICT // AUTHENTICATION_REQUIRED</p>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-900/50 border border-red-700 rounded text-red-400 font-mono text-sm">
            ERROR: {error}
          </div>
        )}

        <form onSubmit={handleLogin} className="space-y-6">
          <div>
            <label className="block text-gray-400 font-mono text-sm mb-2" htmlFor="email">
              OPERATOR_IDENTIFIER (Email)
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full bg-black border border-gray-700 rounded p-3 text-gray-200 font-mono text-sm focus:border-green-500 focus:outline-none transition-colors"
              required
              disabled={isSubmitting}
              placeholder="admin@sovereign.local"
            />
          </div>

          <div>
            <label className="block text-gray-400 font-mono text-sm mb-2" htmlFor="password">
              ACCESS_TOKEN (Password)
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-black border border-gray-700 rounded p-3 text-gray-200 font-mono text-sm focus:border-green-500 focus:outline-none transition-colors"
              required
              disabled={isSubmitting}
              placeholder="••••••••••••"
            />
          </div>

          <button
            type="submit"
            disabled={isSubmitting}
            className="w-full bg-gray-800 hover:bg-gray-700 text-green-500 border border-green-500/30 hover:border-green-500 p-3 rounded font-mono font-bold tracking-widest transition-all uppercase disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isSubmitting ? "Authenticating..." : "Initialize Session"}
          </button>
        </form>
      </div>
    </div>
  );
}
