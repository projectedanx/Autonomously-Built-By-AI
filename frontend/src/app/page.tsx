"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    router.push("/admin");
  }, [router]);

  return (
    <div className="min-h-screen bg-black flex items-center justify-center text-green-500 font-mono text-sm">
      Routing to administrative workspace...
    </div>
  );
}
