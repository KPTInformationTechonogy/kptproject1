"use client";

import { createContext, useContext, useState, ReactNode } from 'react';
import axios from 'axios';
import { useRouter } from 'next/navigation';

// Type definition for User and Context
type User = {
access_token: string;
};

type AuthContextType = {
user: User | null;
login: (email: string, password: string) => Promise<void>;
logout: () => void;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
const [user, setUser] = useState<User | null>(null);
const router = useRouter();

const login = async (email: string, password: string) => {
try {
    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);
    formData.append('grant_type', 'password');

    const response = await axios.post('http://localhost:8000/auth/token', formData, {
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    });

    const token = response.data.access_token;

    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    localStorage.setItem('token', token);
    setUser({ access_token: token });
    router.push('/products');
} catch (error) {
    console.error('Login error:', error);
}
};

const logout = () => {
setUser(null);
delete axios.defaults.headers.common['Authorization'];
localStorage.removeItem('token');
router.push('/login');
};

return (
<AuthContext.Provider value={{ user, login, logout }}>
    {children}
</AuthContext.Provider>
);
};

export const useAuth = (): AuthContextType => {
const context = useContext(AuthContext);
if (!context) {
throw new Error("useAuth must be used within an AuthProvider");
}
return context;
};
export default AuthContext;