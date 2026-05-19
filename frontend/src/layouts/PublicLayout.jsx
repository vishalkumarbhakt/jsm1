import { Outlet } from 'react-router-dom';
import TopNav from '../components/TopNav';

export default function PublicLayout() {
  return (
    <div className="min-h-screen bg-slate-50">
      <TopNav />
      <main className="mx-auto max-w-6xl p-6">
        <Outlet />
      </main>
    </div>
  );
}
