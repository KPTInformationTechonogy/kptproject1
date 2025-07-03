import { NextResponse } from 'next/server';
import { cookies } from 'next/headers';
import axios from 'axios';

export async function GET() {
  const cookieStore = await cookies();
  const token = cookieStore.get('auth_token')?.value;

  if (!token) {
    return NextResponse.json({ error: 'Not authenticated' }, { status: 401 });
  }

  try {
    const response = await axios.get(`${process.env.BACKEND_URL}/auth/me`, {
      headers: { Authorization: `Bearer ${token}` },
    });

    return NextResponse.json(response.data);
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      return NextResponse.json(
        {
          error:
            error.response?.data?.detail ||
            error.response?.data?.message ||
            error.message,
        },
        { status: error.response?.status || 500 }
      );
    }

    return NextResponse.json({ error: 'Unknown error' }, { status: 500 });
  }
}
