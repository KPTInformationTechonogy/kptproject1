"use client"
import Image from "next/image";
import Link from "next/link";
import Cart from "@/images/shopping_cart.png";
import Profile from "@/images/account_circle.png";
import Notification from "@/images/notifications.png";
import { useState } from "react";
import { useRouter } from "next/navigation";
import CartModal from "./cartModal";


const NavIcons = () => {
    const [isProfileOpen, setIsProfileOpen] = useState(false);
    const [isCartOpen, setIsCartOpen] = useState(false);
    const router = useRouter();
    const isLoggedIn = false;

    const handleProfile = () =>{
        if (!isLoggedIn){
            router.push("/login");
        }
        setIsProfileOpen((prev) => !prev);
    }


    return (
        <div className="flex items-center gap-4 xl:gap-6 relative">
            <Image src={Profile} alt="cart" width={28} height={28} className="cursor-pointer" onClick={handleProfile} />
            {isProfileOpen && (
                <div className="absolute p-4 rounded-md top-12 left-0 text-sm border-t-0 border-1 border-yellow-800 bg-white text-yellow-700 shadow-md flex flex-col items-center justify-center gap-4 z-20 transition-colors">
                    <Link href="/">Profile</Link>
                    <div className="mt-2 cursor-pointer">Logout</div>
                </div>
            )}
            <Image src={Notification} alt="cart" width={28} height={28} className="cursor-pointer" />
            <div className="relative cursor-pointer">
                <Image src={Cart} alt="cart" width={28} height={28} className="cursor-pointer" onClick={() => setIsCartOpen((prev) => !prev)}/>
                <div className="absolute -top-4 -right-4 w-6 h-6 bg-blue-600 text-white text-sm flex items-start justify-center rounded-full">2</div>
                {isCartOpen && <CartModal />}
            </div>
        </div>
    );
}
export default NavIcons;