import RoleCards from '../../components/RoleCards';

const stats = [
  { title: 'Notes PDFs', value: 18 },
  { title: 'Assignments Due', value: 4 },
  { title: 'Attendance %', value: '87%' },
];

export default function StudentDashboardPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-slate-900">Student Dashboard</h1>
      <RoleCards items={stats} />
      <div className="grid gap-4 md:grid-cols-2">
        <div className="rounded-lg bg-white p-5 shadow">Notes PDF download, video lectures, assignment submit</div>
        <div className="rounded-lg bg-white p-5 shadow">Attendance, progress report, notifications, fee payment</div>
      </div>
    </div>
  );
}
