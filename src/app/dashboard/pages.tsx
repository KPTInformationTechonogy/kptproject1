import { useEffect, useState } from 'react'
import { getAccessToken } from '@/lib/auth'
import { useRouter } from 'next/router'

export default function Dashboard() {
const router = useRouter()
const [user, setUser] = useState<any>(null)

useEffect(() => {
    (async () => {
    const token = await getAccessToken()
    if (!token) return router.push("/login")

    const res = await fetch("http://localhost:8000/auth/admin/dashboard", {
        headers: { Authorization: `Bearer ${token}` }
    })

    if (res.ok) {
        const data = await res.json()
        setUser(data.message)
    } else {
        router.push("/login")
    }
    })()
}, [])

return (
    <div>{user ? <h1>{user}</h1> : <p>Loading...</p>}</div>
)
}