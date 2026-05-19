import RoleCards from '../../components/RoleCards';

const stats = [
  { title: 'Uploaded Notes', value: 32 },
  { title: 'Assignments Created', value: 15 },
  { title: 'Attendance Marked', value: 102 },
];

export default function TeacherDashboardPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-slate-900">Teacher Dashboard</h1>
      <RoleCards items={stats} />
      <div className="rounded-lg bg-white p-5 shadow">
        Upload notes/videos, create quizzes, mark attendance, evaluate submissions, and track student progress.
      </div>
    </div>
  );
}
