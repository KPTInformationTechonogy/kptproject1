"use client";

import Image from "next/image";
import Location from "@/Components/Location";
import aliyu from "@/images/aliyu.jpg";
import ismail from "@/images/ismail.jpg";


import {
BuildingOffice2Icon,
LightBulbIcon,
MapPinIcon,
ClockIcon,
UserGroupIcon,
GlobeAltIcon,
DocumentTextIcon,
} from "@heroicons/react/24/outline";

export default function AboutPage() {
const team = [
{ name: "Taha Ali Yahya", role: "Director - Nigeria", img: ismail },
{ name: "Ismail Aliyu Abubakar", role: "General Manager", img: aliyu },
{ name: "Nura Ayuba Bayero", role: "Sales Representative", img: aliyu },
];

const timeline = [
{ year: "2007", event: "Founded in Yiwu City, China" },
{ year: "2013", event: "Expanded to Middle East & North Africa" },
{ year: "2018", event: "Opened branches in Hong Kong & London" },
{ year: "2024", event: "Launch into West Africa, starting with Nigeria" },
];

const navItems = [
{ label: "Overview", id: "overview", icon: DocumentTextIcon },
{ label: "Mission & Vision", id: "mission-vision", icon: LightBulbIcon },
{ label: "Company Background", id: "company-background", icon: BuildingOffice2Icon },
{ label: "Expansion", id: "expansion", icon: MapPinIcon },
{ label: "Our Journey", id: "journey", icon: ClockIcon },
{ label: "Our Team", id: "team", icon: UserGroupIcon },
{ label: "Locations", id: "locations", icon: GlobeAltIcon },
];

return (
<div className="flex min-h-screen bg-white text-gray-900">
    {/* Sidebar Navigation */}
        <aside className="w-1/3 bg-gray-50 border-r border-gray-200 p-6 sticky h-[100vh] hidden lg:block">
    <div className="sticky top-24">
        <h2 className="text-xl font-bold text-yellow-700 mb-8 flex items-center gap-2">
        <BuildingOffice2Icon className="h-6 w-6" />
        About Our Company
        </h2>

        <nav>
        <ul className="space-y-2">
            {navItems.map(({ id, label, icon: Icon }) => (
            <li key={id}>
                <a
                href={`#${id}`}
                className="flex items-center gap-3 py-2 px-3 rounded-md hover:bg-green-50 hover:text-yellow-700 transition-colors text-gray-700"
                >
                <Icon className="h-5 w-5" />
                {label}
                </a>
            </li>
            ))}
        </ul>
        </nav>

        <div className="mt-12 pt-6 border-t border-gray-200">
        <p className="text-sm text-gray-500">
            Driving innovation and quality across Africa&#39;s construction landscape since 2007.
        </p>
        </div>
    </div>
    </aside>

    {/* Main Content */}
    <main className="flex-1 py-16 px-4 h-[100vh] overflow-y-scroll scroll-smooth sm:px-8 lg:px-12 xl:px-24">
    <div className="max-w-4xl mx-auto space-y-16">
        {/* Overview */}
        <section id="overview" className="text-center bg-blue-400 bg-opacity-70 p-8 rounded-xl mb-12">
        <h1 className="text-4xl text-gray-800 font-bold mb-4">About Us</h1>
        <p className="text-lg text-gray-700 max-w-2xl mx-auto">
            Driving innovation and quality across Africa&#39;s construction and home improvement landscape.
        </p>
        </section>

        {/* Mission & Vision */}
        <section id="mission-vision" className="space-y-12">
        <div>
            <h2 className="text-2xl font-semibold text-yellow-700 mb-2">Our Mission</h2>
            <p className="text-gray-700 leading-relaxed text-justify">
            To leverage technology and innovation in delivering high-quality building materials,
            construction supplies, furniture, and home automation products that meet the diverse needs
            of African customers. Our aim is to build trust, provide value, and drive sustainable growth,
            starting in Nigeria, while contributing to local economic and technological advancement across the continent.
            </p>
        </div>

        <div>
            <h2 className="text-2xl font-semibold text-yellow-700 mb-2">Our Vision</h2>
            <p className="text-gray-700 leading-relaxed text-justify">
            To be Africa&#39;s leading provider of high-quality, technology-driven building and home improvement
            solutions, enhancing living and working spaces across the continent through innovation and excellence.
            </p>
        </div>
        </section>

        {/* Company Background */}
        <section id="company-background">
        <h2 className="text-2xl font-semibold text-yellow-700 mb-2">Who We Are</h2>
        <p className="text-gray-700 leading-relaxed text-justify">
            Our company, headquartered in Yiwu City, China, has nearly two decades of experience in the building
            materials trade. With strong relationships with hundreds of factories across China, we have built a
            solid foundation in sourcing and quality control, enabling us to offer a wide range of premium products.
        </p>
        <p className="text-gray-700 leading-relaxed mt-4 text-justify">
            We have successfully exported thousands of containers to the Middle East and North Africa,
            establishing a reputation for reliability and excellence. Our international branches in
            Hong Kong, London, and Fez City, Morocco, extend our global reach.
        </p>
        </section>

        {/* Expansion */}
        <section id="expansion">
        <h2 className="text-2xl font-semibold text-yellow-700 mb-2">Expanding Across Africa</h2>
        <p className="text-gray-700 leading-relaxed text-justify">
            We are expanding across Central and West Africa, beginning with Nigeria. Our initial focus on Kano allows
            us to understand local dynamics, establish a strong foundation, and refine our model for broader regional growth.
        </p>
        <p className="text-gray-700 leading-relaxed mt-4 text-justify">
            With a tech-driven approach, we streamline supply chains and deliver exceptional customer experiences to
            both residential and commercial clients.
        </p>
        </section>

        {/* Timeline */}
        <section id="journey">
        <h2 className="text-2xl font-semibold text-yellow-700 mb-4">Our Journey</h2>
        <ul className="space-y-4">
            {timeline.map(({ year, event }, index) => (
            <li key={index} className="border-l-4 border-yellow-500 pl-4 text-justify">
                <span className="font-bold">{year}:</span> {event}
            </li>
            ))}
        </ul>
        </section>

        {/* Team */}
        <section id="team">
        <h2 className="text-2xl font-semibold text-yellow-700 mb-6">Meet the Team</h2>
        <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-8">
            {team.map(({ name, role, img }, index) => (
            <div key={index} className="text-center">
                <div className="w-32 h-32 mx-auto mb-4 rounded-full overflow-hidden bg-gray-200 border-4 border-yellow-100">
                <Image
                    src={img}
                    alt={name}
                    width={128}
                    height={128}
                    className="object-cover w-full h-full"
                />
                </div>
                <h3 className="font-semibold text-lg">{name}</h3>
                <p className="text-gray-600">{role}</p>
            </div>
            ))}
        </div>
        </section>

        {/* Locations */}
        <section id="locations" className="text-center">
        <h2 className="text-2xl font-semibold text-yellow-700 mb-2">Our Locations</h2>
        <p className="text-gray-600 mb-6">Branches in China, UK, Morocco, and Nigeria</p>
        <div className="w-full h-80 bg-gray-100 rounded-xl flex items-center justify-center text-gray-500">
            <Location />
        </div>
        </section>
    </div>
    </main>
</div>
);
}
