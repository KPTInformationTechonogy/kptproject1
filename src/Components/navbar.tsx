import Link from "next/link";
import Image from "next/image";
import Logo from "@/images/kpt_logo.jpeg";
import Menu from "./Menu";
import NavIcons from "./NavIcons";
import SearchBar from "./SearchBar";

const NavBar = () => {
    return (
        <header className="sticky top-0 z-50 w-full h-20 bg-yellow-700 px-4 md:px-8 lg:px-16 xl:px-32 shadow-md flex items-center justify-between">
            {/* Logo and Company Name */}
            <div className="flex items-center gap-4">
                <Link href={"/"}>
                    <Image 
                        src={Logo} 
                        alt="Logo" 
                        width={50} 
                        height={50} 
                        className="rounded-full ring-2 ring-white"
                    />
                </Link>
                <h1 className="hidden lg:block text-xl font-bold text-white font-sans tracking-wide">
                    Kano Process Trading Company
                </h1>
            </div>

            {/* Desktop Navigation Links */}
            <nav className="hidden xl:flex items-center gap-8">
                <div className="flex items-center gap-6 text-white font-sans font-semibold text-sm">
                    <Link href="/" className="hover:text-yellow-200 transition-colors">Home</Link>
                    <Link href="/services" className="hover:text-yellow-200 transition-colors">Services</Link>
                    <Link href="/list" className="hover:text-yellow-200 transition-colors">Products</Link>
                    <Link href="/contact" className="hover:text-yellow-200 transition-colors">Contact</Link>
                    <Link href="/about" className="hover:text-yellow-200 transition-colors">About</Link>
                </div>
            </nav>

            {/* Search and Icons (Desktop) */}
            <div className="hidden md:flex items-center gap-6">
                <SearchBar />
                <NavIcons />
            </div>

            {/* Mobile Menu Button */}
            <div className="md:hidden">
                <Menu />
            </div>
        </header>
    );
};

export default NavBar;