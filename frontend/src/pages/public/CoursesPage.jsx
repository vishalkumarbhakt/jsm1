export default function CoursesPage() {
  const courses = ['Mathematics', 'Science', 'English', 'Computer'];
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {courses.map((course) => (
        <div key={course} className="rounded-lg bg-white p-5 shadow">
          <h3 className="font-semibold">{course}</h3>
          <p className="text-sm text-slate-500">Course module with notes, videos, tests, and assignments.</p>
        </div>
      ))}
    </div>
  );
}
