export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="admin-layout min-h-screen bg-black">
      {children}
    </div>
  );
}
