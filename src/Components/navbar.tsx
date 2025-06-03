import Link from "next/link";
import Image from "next/image";
import Logo from "@/images/kpt_logo.jpeg";
import Menu from "./Menu";
import NavIcons from "./NavIcons";
import SearchBar from "./SearchBar";

const NavBar = () => {
    return (
        <header className="sticky w-full top-0 z-50 px-4 md:px-8 lg:px-16 xl:px-32 h-20 bg-yellow-700  shadow-md flex items-center justify-between">
            {/* Logo and Company Name */}
            <div className="flex items-center gap-4">
                <Link href={"/"}>
                    <Image 
                        src={Logo} 
                        alt="Logo" 
                        width={50} 
                        height={50} 
                        className="rounded-md ring-2 ring-white"
                    />
                </Link>
                <h1 className="hidden lg:block text-lg font-bold text-white font-sans tracking-wide">
                    Kano Process Trading Company
                </h1>
            </div>

            {/* Desktop Navigation Links */}
            <nav className="hidden lg:flex items-center gap-8">
                <div className="flex items-center gap-6 text-white font-sans font-semibold text-sm">
                    <Link href="/" className="hover:text-yellow-200 transition-colors">Home</Link>
                    <Link href="/services" className="hover:text-yellow-200 transition-colors">Services</Link>
                    <Link href="/list" className="hover:text-yellow-200 transition-colors">Products</Link>
                    <Link href="/contact" className="hover:text-yellow-200 transition-colors">Contact</Link>
                    <Link href="/about" className="hover:text-yellow-200 transition-colors">About</Link>
                </div>
            </nav>

            {/* Search and Icons (Desktop) */}
            <div className="flex items-center gap-6">
                <div className="sm:w-10 md:w-max"><SearchBar  /></div>
                <div className="hidden md:block"><NavIcons /></div>
                
            </div>

            {/* Mobile Menu Button */}
            <div className="md:hidden">
                <Menu />
            </div>
        </header>
    );
};

export default NavBar;