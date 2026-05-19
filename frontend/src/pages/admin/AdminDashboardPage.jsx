import {
  ArcElement,
  Chart as ChartJS,
  Legend,
  Tooltip,
} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';
import RoleCards from '../../components/RoleCards';

ChartJS.register(ArcElement, Tooltip, Legend);

const stats = [
  { title: 'Total Students', value: 540 },
  { title: 'Total Teachers', value: 28 },
  { title: 'Pending Admissions', value: 16 },
];

export default function AdminDashboardPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-slate-900">Admin Dashboard</h1>
      <RoleCards items={stats} />
      <div className="grid gap-4 md:grid-cols-2">
        <div className="rounded-lg bg-white p-5 shadow">
          <h3 className="mb-3 font-semibold">Analytics</h3>
          <Doughnut
            data={{
              labels: ['Paid Fees', 'Pending Fees', 'Overdue'],
              datasets: [
                {
                  data: [70, 20, 10],
                  backgroundColor: ['#16a34a', '#f59e0b', '#ef4444'],
                },
              ],
            }}
          />
        </div>
        <div className="rounded-lg bg-white p-5 shadow">
          Manage students/teachers/courses, admissions, CMS, announcements, and payment tracking.
        </div>
      </div>
    </div>
  );
}
