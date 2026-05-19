import { Link, Outlet } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { logout } from '../redux/authSlice';

export default function DashboardLayout({ title, links }) {
  const dispatch = useDispatch();

  return (
    <div className="flex min-h-screen bg-slate-100">
      <aside className="w-64 space-y-3 bg-slate-900 p-5 text-white">
        <h2 className="text-lg font-semibold">{title}</h2>
        <nav className="space-y-1 text-sm">
          {links.map((link) => (
            <Link key={link.to} className="block rounded px-3 py-2 hover:bg-slate-700" to={link.to}>
              {link.label}
            </Link>
          ))}
        </nav>
        <button
          className="mt-4 w-full rounded bg-red-500 px-3 py-2 text-sm"
          onClick={() => dispatch(logout())}
          type="button"
        >
          Logout
        </button>
      </aside>
      <div className="flex-1 p-6">
        <Outlet />
      </div>
    </div>
  );
}
