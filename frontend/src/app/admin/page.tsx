"use client";

import { useEffect, useState } from "react";
import { useAuth } from "../../context/AuthContext";
import { useRouter } from "next/navigation";

interface FileData {
  name: string;
  size: number;
  lastModified: string;
}

interface WorkspaceData {
  [directory: string]: FileData[];
}

export default function AdminDashboard() {
  const [data, setData] = useState<WorkspaceData | null>(null);
  const [dataLoading, setDataLoading] = useState(true);
  const { user, loading: authLoading, signOut } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!authLoading && !user) {
      router.push("/login");
    }
  }, [user, authLoading, router]);

  useEffect(() => {
    if (!user) return;

    async function fetchData() {
      try {
        const response = await fetch("/api/workspace");
        if (response.ok) {
          const result = await response.json();
          setData(result);
        } else {
          console.error("Failed to fetch workspace data");
        }
      } catch (error) {
        console.error("Error fetching workspace data:", error);
      } finally {
        setDataLoading(false);
      }
    }

    fetchData();
  }, [user]);

  if (authLoading || (!user && !authLoading)) {
    return <div className="min-h-screen bg-black p-8 text-gray-500 font-mono text-sm">Verifying authorization...</div>;
  }

  if (dataLoading) {
    return <div className="min-h-screen bg-black p-8 text-gray-500 font-mono text-sm">Loading workspace states...</div>;
  }

  if (!data) {
    return <div className="min-h-screen bg-black p-8 text-red-500 font-mono text-sm">Error: Workspace data unavailable.</div>;
  }

  const renderTable = (directory: string, files: FileData[]) => (
    <div key={directory} className="mb-8 bg-gray-900 border border-gray-800 p-4 rounded">
      <h2 className="text-lg font-semibold mb-2 font-mono uppercase border-b border-gray-700 pb-1">{directory}</h2>
      {files.length === 0 ? (
        <p className="text-sm text-gray-500 font-mono italic">No items present.</p>
      ) : (
        <table className="w-full text-left border-collapse font-mono text-sm">
          <thead>
            <tr className="bg-gray-800 text-gray-200">
              <th className="p-2 border border-gray-700 font-medium">Identifier</th>
              <th className="p-2 border border-gray-700 font-medium w-32">Bytes</th>
              <th className="p-2 border border-gray-700 font-medium w-48">Modified</th>
            </tr>
          </thead>
          <tbody>
            {files.map((file) => (
              <tr key={file.name} className="hover:bg-gray-800 border-b border-gray-700">
                <td className="p-2 border-r border-l border-gray-700 text-gray-300">{file.name}</td>
                <td className="p-2 border-r border-gray-700 text-gray-400 text-right">{file.size}</td>
                <td className="p-2 border-r border-gray-700 text-gray-400">{new Date(file.lastModified).toISOString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );

  return (
    <main className="min-h-screen bg-black text-gray-200 p-8">
      <div className="max-w-6xl mx-auto">
        <header className="mb-12 flex justify-between items-end border-b border-gray-800 pb-4">
          <div>
            <h1 className="text-2xl font-bold font-mono tracking-wider text-green-500">SOVEREIGN_CONTEXT_ENGINEERING_WORKSPACE</h1>
            <p className="text-sm font-mono text-gray-500 mt-2">v1.0.0-STRICT // DASHBOARD_VIEW // MULTI_USER_INSTANCE</p>
          </div>
          <div className="text-right">
             <p className="text-sm font-mono text-gray-400 mb-2">OPERATOR: {user?.email}</p>
             <button
                onClick={signOut}
                className="text-xs font-mono bg-red-900/30 text-red-500 border border-red-900 hover:bg-red-900/50 px-3 py-1 rounded transition-colors uppercase tracking-widest"
              >
                Terminate Session
             </button>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8">
          <div className="space-y-8">
            {renderTable('context_inbox', data['context_inbox'] || [])}
            {renderTable('delegated_tasks', data['delegated_tasks'] || [])}
          </div>
          <div className="space-y-8">
            {renderTable('completed_artifacts', data['completed_artifacts'] || [])}
            {renderTable('epistemic_escrow', data['epistemic_escrow'] || [])}
          </div>
        </div>

        <section className="mt-16 pt-8 border-t border-gray-800">
            <h2 className="text-lg font-semibold mb-4 font-mono uppercase text-yellow-500">Symbolic Scars / System Constraints</h2>
            <div className="bg-gray-900 border border-gray-700 p-4 font-mono text-sm text-gray-400 rounded">
                <ul className="list-disc list-inside space-y-2">
                    <li>CFDI_THRESHOLD_ACTIVE: 0.15</li>
                    <li>SAGA_RECOVERY_MODE: compensating_transaction</li>
                    <li>ADJECTIVAL_BOUND: limiting</li>
                    <li className="text-blue-400">ADMIN_MULTI_TENANT_ENABLED: true</li>
                </ul>
            </div>
        </section>
      </div>
    </main>
  );
}
