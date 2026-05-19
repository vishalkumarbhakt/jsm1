import { motion } from 'framer-motion';

export default function HomePage() {
  return (
    <section className="grid items-center gap-6 md:grid-cols-2">
      <div>
        <motion.h1
          animate={{ opacity: 1, y: 0 }}
          className="text-4xl font-bold text-slate-900"
          initial={{ opacity: 0, y: 20 }}
        >
          Full-Stack School Learning Platform
        </motion.h1>
        <p className="mt-3 text-slate-600">
          JSM LMS now includes role-based student, teacher, and admin dashboards with JWT authentication.
        </p>
      </div>
      <img alt="School building" className="rounded-xl shadow" src="/assets/school-building.png" />
    </section>
  );
}
