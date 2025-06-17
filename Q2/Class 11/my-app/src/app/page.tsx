import Link from 'next/link';

async function getUsers() {
  const res = await fetch('https://jsonplaceholder.typicode.com/users');
  return res.json();
}

export default async function Home() {
  const users = await getUsers();

  return (
    <div className="container mx-auto p-6 bg-gray-100 min-h-screen">
      <title>API Data Fetch</title>
      <h1 className="text-3xl font-bold mb-6 text-center text-gray-800">User List</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {users.map((user: { id: number; name: string; email: string; username: string }) => (
          <div key={user.id} className="bg-white p-6 rounded-lg shadow-md border">
            <h2 className="text-xl font-semibold text-gray-900">{user.name}</h2>
            <p className="text-gray-700">Username: {user.username}</p>
            <p className="text-gray-500">Email: {user.email}</p>
            <Link href={`/user/${user.id}`} className="text-blue-600 hover:underline mt-2 inline-block">
              View Profile
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

