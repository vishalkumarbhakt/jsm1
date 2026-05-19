import { Link } from 'react-router-dom';

const navLinks = [
  { label: 'Home', to: '/' },
  { label: 'About', to: '/about' },
  { label: 'Courses', to: '/courses' },
  { label: 'Admission', to: '/admission' },
  { label: 'Contact', to: '/contact' },
];

export default function TopNav() {
  return (
    <header className="border-b bg-white/90 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between p-4">
        <Link className="flex items-center gap-2 text-lg font-bold text-slate-900" to="/">
          <img alt="JSM" className="h-10 w-10 rounded-full object-cover" src="/assets/logo.jpeg" />
          JSM LMS
        </Link>
        <nav className="flex gap-4 text-sm">
          {navLinks.map((link) => (
            <Link className="text-slate-600 hover:text-slate-900" key={link.to} to={link.to}>
              {link.label}
            </Link>
          ))}
          <Link className="rounded bg-slate-900 px-3 py-1 text-white" to="/login">
            Login
          </Link>
        </nav>
      </div>
    </header>
  );
}
