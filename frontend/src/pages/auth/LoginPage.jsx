import { useForm } from 'react-hook-form';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { login } from '../../redux/authSlice';

const rolePath = {
  student: '/student',
  teacher: '/teacher',
  admin: '/admin',
};

export default function LoginPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { loading, error } = useSelector((state) => state.auth);
  const { register, handleSubmit } = useForm();

  const onSubmit = async (data) => {
    const result = await dispatch(login(data));
    const role = result.payload?.role;
    navigate(rolePath[role] || '/');
  };

  return (
    <form className="mx-auto max-w-md space-y-4 rounded-lg bg-white p-6 shadow" onSubmit={handleSubmit(onSubmit)}>
      <h2 className="text-xl font-semibold">Login</h2>
      <input className="w-full rounded border p-2" placeholder="Username" {...register('username')} />
      <input className="w-full rounded border p-2" placeholder="Password" type="password" {...register('password')} />
      {error && <p className="text-sm text-red-600">{error}</p>}
      <button className="w-full rounded bg-slate-900 p-2 text-white" disabled={loading} type="submit">
        {loading ? 'Signing in...' : 'Sign In'}
      </button>
    </form>
  );
}
