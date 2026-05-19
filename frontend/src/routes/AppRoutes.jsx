import { Route, Routes } from 'react-router-dom';
import DashboardLayout from '../layouts/DashboardLayout';
import PublicLayout from '../layouts/PublicLayout';
import LoginPage from '../pages/auth/LoginPage';
import RegisterPage from '../pages/auth/RegisterPage';
import AdminDashboardPage from '../pages/admin/AdminDashboardPage';
import AdmissionPage from '../pages/public/AdmissionPage';
import AboutPage from '../pages/public/AboutPage';
import ContactPage from '../pages/public/ContactPage';
import CoursesPage from '../pages/public/CoursesPage';
import HomePage from '../pages/public/HomePage';
import StudentDashboardPage from '../pages/student/StudentDashboardPage';
import TeacherDashboardPage from '../pages/teacher/TeacherDashboardPage';
import ProtectedRoute from './ProtectedRoute';

const studentLinks = [{ to: '/student', label: 'Overview' }];
const teacherLinks = [{ to: '/teacher', label: 'Overview' }];
const adminLinks = [{ to: '/admin', label: 'Overview' }];

export default function AppRoutes() {
  return (
    <Routes>
      <Route element={<PublicLayout />}>
        <Route element={<HomePage />} path="/" />
        <Route element={<AboutPage />} path="/about" />
        <Route element={<CoursesPage />} path="/courses" />
        <Route element={<AdmissionPage />} path="/admission" />
        <Route element={<ContactPage />} path="/contact" />
        <Route element={<LoginPage />} path="/login" />
        <Route element={<RegisterPage />} path="/register" />
      </Route>

      <Route
        element={
          <ProtectedRoute role="student">
            <DashboardLayout links={studentLinks} title="Student Panel" />
          </ProtectedRoute>
        }
      >
        <Route element={<StudentDashboardPage />} path="/student" />
      </Route>

      <Route
        element={
          <ProtectedRoute role="teacher">
            <DashboardLayout links={teacherLinks} title="Teacher Panel" />
          </ProtectedRoute>
        }
      >
        <Route element={<TeacherDashboardPage />} path="/teacher" />
      </Route>

      <Route
        element={
          <ProtectedRoute role="admin">
            <DashboardLayout links={adminLinks} title="Admin Panel" />
          </ProtectedRoute>
        }
      >
        <Route element={<AdminDashboardPage />} path="/admin" />
      </Route>
    </Routes>
  );
}
