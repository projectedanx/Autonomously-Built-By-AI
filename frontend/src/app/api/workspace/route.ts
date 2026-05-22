import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

const WORKSPACE_DIRS = [
  'context_inbox',
  'delegated_tasks',
  'completed_artifacts',
  'epistemic_escrow',
];

interface FileData {
  name: string;
  size: number;
  lastModified: Date;
}

interface WorkspaceData {
  [directory: string]: FileData[];
}

export async function GET() {
  const rootPath = process.cwd().replace('/frontend', ''); // Go up one level to workspace root
  const data: WorkspaceData = {};

  for (const dir of WORKSPACE_DIRS) {
    const dirPath = path.join(rootPath, dir);
    data[dir] = [];

    if (fs.existsSync(dirPath)) {
      try {
        const files = fs.readdirSync(dirPath);
        for (const file of files) {
          const filePath = path.join(dirPath, file);
          const stats = fs.statSync(filePath);
          if (stats.isFile()) {
            data[dir].push({
              name: file,
              size: stats.size,
              lastModified: stats.mtime,
            });
          }
        }
      } catch (error) {
        console.error(`Error reading directory ${dir}:`, error);
      }
    }
  }

  return NextResponse.json(data);
}
