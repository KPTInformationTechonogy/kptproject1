import { NextResponse } from 'next/server'
import { cookies } from 'next/headers'
import axios from 'axios'

export async function POST() {
  const cookieStore = await cookies()
  const token = cookieStore.get('auth_token')?.value

  if (!token) {
    return NextResponse.json(
      { message: 'Already logged out' },
      { status: 200 }
    )
  }

  try {
    await axios.post(`${process.env.BACKEND_URL}/auth/logout`, null, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    // Clear cookie
    const res = NextResponse.json({ message: 'Logged out' })
    res.cookies.set('auth_token', '', { maxAge: 0 })
    return res
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
      )
    }

    return NextResponse.json({ error: 'Unknown error occurred' }, { status: 500 })
  }
}
