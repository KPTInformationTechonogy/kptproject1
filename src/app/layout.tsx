import { AuthProvider } from '@/app/context/AuthContext'
import type { Metadata } from "next";
import "./globals.css";
import NavBar from "@/Components/navbar";
import Footer from "@/Components/footer";
;





export const metadata: Metadata = {
  title: "Kano Process Trading Company"};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className="bg-gray-100"
      >
        <NavBar />
        <AuthProvider>
          {children}
        </AuthProvider>
        <Footer />
      </body>
    </html>
  );
}
