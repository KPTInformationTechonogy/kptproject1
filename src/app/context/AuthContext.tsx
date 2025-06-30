"use client"
import { createContext, useContext, useState, ReactNode, Children } from 'react';
import axios from 'axios';
import { useRouter } from 'next/navigation';

const AuthContext = createContext();
export const AuthProvider = ({ Children}) => {
    const [user, setUser] = useState(null);
    const router = useRouter();

    const login = async (email, password) => {
        try {
            const formData = new FormData();
            formData.append('email', email);
            formData.append('password', password);
            const response = await axios.post('http://localhost:8000/auth/token', formData, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
            });
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access_token}`;
            localStorage.setItem('token', response.data.access_token);
            setUser(response.data);
            router.push('/dashboard');
        } catch (error) {
            console.error('Login error:', error);
        }
            
    };
    const logout = () => {
        setUser(null);
        delete axios.defaults.headers.common['Authorization'];
        router.push('/login');
    };

return (
    <AuthContext.Provider value={{ user, login, logout }}>
        {Children}
    </AuthContext.Provider>
);
};
export default AuthContext;