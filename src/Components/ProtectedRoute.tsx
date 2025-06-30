// app/components/ProtectedRoute.tsx
'use client'

import { useAuth } from '@/app/context/AuthContext'
import { useRouter } from 'next/navigation'
import { useEffect } from 'react'

export default function ProtectedRoute({ children, requiredRole }: { children: React.ReactNode, requiredRole?: string }) {
const { user, isAuthenticated, loading } = useAuth()
const router = useRouter()

useEffect(() => {
    if (!loading && !isAuthenticated) {
    router.push('/login')
    }

    if (!loading && isAuthenticated && requiredRole && user?.role !== requiredRole) {
    router.push('/unauthorized')
    }
}, [loading, isAuthenticated, user, router, requiredRole])

if (loading || !isAuthenticated || (requiredRole && user?.role !== requiredRole)) {
    return <div>Loading...</div>
}

return <>{children}</>
}