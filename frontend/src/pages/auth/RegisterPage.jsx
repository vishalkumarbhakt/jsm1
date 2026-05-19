import { useForm } from 'react-hook-form';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { register as registerUser } from '../../redux/authSlice';

export default function RegisterPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { loading, error } = useSelector((state) => state.auth);
  const { register, handleSubmit } = useForm({ defaultValues: { role: 'student' } });

  const onSubmit = async (data) => {
    const result = await dispatch(registerUser(data));
    if (result.payload) navigate('/student');
  };

  return (
    <form className="mx-auto max-w-md space-y-4 rounded-lg bg-white p-6 shadow" onSubmit={handleSubmit(onSubmit)}>
      <h2 className="text-xl font-semibold">Register</h2>
      <input className="w-full rounded border p-2" placeholder="Username" {...register('username')} />
      <input className="w-full rounded border p-2" placeholder="Email" type="email" {...register('email')} />
      <input className="w-full rounded border p-2" placeholder="Password" type="password" {...register('password')} />
      <select className="w-full rounded border p-2" {...register('role')}>
        <option value="student">Student</option>
        <option value="teacher">Teacher</option>
      </select>
      {error && <p className="text-sm text-red-600">{error}</p>}
      <button className="w-full rounded bg-slate-900 p-2 text-white" disabled={loading} type="submit">
        {loading ? 'Creating account...' : 'Create Account'}
      </button>
    </form>
  );
}
