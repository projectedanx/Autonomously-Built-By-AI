"use client";

import { useEffect, useState } from "react";

interface FileData {
  name: string;
  size: number;
  lastModified: string;
}

interface WorkspaceData {
  [directory: string]: FileData[];
}

export default function Home() {
  const [data, setData] = useState<WorkspaceData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
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
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) {
    return <div className="p-8 text-gray-500 font-mono text-sm">Loading workspace states...</div>;
  }

  if (!data) {
    return <div className="p-8 text-red-500 font-mono text-sm">Error: Workspace data unavailable.</div>;
  }

  const renderTable = (directory: string, files: FileData[]) => (
    <div key={directory} className="mb-8">
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
              <tr key={file.name} className="hover:bg-gray-900 border-b border-gray-800">
                <td className="p-2 border-r border-l border-gray-800 text-gray-300">{file.name}</td>
                <td className="p-2 border-r border-gray-800 text-gray-400 text-right">{file.size}</td>
                <td className="p-2 border-r border-gray-800 text-gray-400">{new Date(file.lastModified).toISOString()}</td>
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
        <header className="mb-12">
          <h1 className="text-2xl font-bold font-mono tracking-wider text-green-500">SOVEREIGN_CONTEXT_ENGINEERING_WORKSPACE</h1>
          <p className="text-sm font-mono text-gray-500 mt-2">v1.0.0-STRICT // DASHBOARD_VIEW</p>
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
            <div className="bg-gray-900 border border-gray-700 p-4 font-mono text-sm text-gray-400">
                <ul className="list-disc list-inside space-y-2">
                    <li>CFDI_THRESHOLD_ACTIVE: 0.15</li>
                    <li>SAGA_RECOVERY_MODE: compensating_transaction</li>
                    <li>ADJECTIVAL_BOUND: limiting</li>
                </ul>
            </div>
        </section>
      </div>
    </main>
  );
}
