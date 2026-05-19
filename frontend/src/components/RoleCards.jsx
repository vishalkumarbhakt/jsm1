export default function RoleCards({ items }) {
  return (
    <div className="grid gap-4 md:grid-cols-3">
      {items.map((item) => (
        <div key={item.title} className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
          <p className="text-sm text-slate-500">{item.title}</p>
          <p className="mt-2 text-2xl font-semibold text-slate-800">{item.value}</p>
        </div>
      ))}
    </div>
  );
}
