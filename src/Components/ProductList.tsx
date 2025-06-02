"use client";

import Image from "next/image";
import Link from "next/link";
import Hinges from "@/images/Hinges - Copy.png";
import Drywall from "@/images/Drywall.png";
import furniture from "@/images/furniture.png";

const products = [
  {
    id: 1,
    name: "Door Hinges",
    price: "₦1,500",
    description: "High-quality steel hinges for all door types",
    primaryImage: Hinges,
    secondaryImage: Drywall,
  },
  {
    id: 2,
    name: "Drywall Sheets",
    price: "₦8,500",
    description: "Premium drywall sheets for smooth finishes",
    primaryImage: Drywall,
    secondaryImage: furniture,
  },
  {
    id: 3,
    name: "Wooden Furniture",
    price: "₦25,000",
    description: "Handcrafted wooden furniture pieces",
    primaryImage: furniture,
    secondaryImage: Hinges,
  },
  {
    id: 4,
    name: "Premium Hinges",
    price: "₦3,000",
    description: "Luxury hinges with extended durability",
    primaryImage: Hinges,
    secondaryImage: Drywall,
  },
  {
    id: 5,
    name: "Drywall Panels",
    price: "₦12,000",
    description: "Industrial-grade drywall panels",
    primaryImage: Drywall,
    secondaryImage: furniture,
  },
  {
    id: 6,
    name: "Drywall Panels",
    price: "₦12,000",
    description: "Industrial-grade drywall panels",
    primaryImage: Drywall,
    secondaryImage: furniture,
  },
  {
    id: 7,
    name: "Drywall Panels",
    price: "₦12,000",
    description: "Industrial-grade drywall panels",
    primaryImage: Drywall,
    secondaryImage: furniture,
  },
  {
    id: 8,
    name: "Premium Hinges",
    price: "₦3,000",
    description: "Luxury hinges with extended durability",
    primaryImage: Hinges,
    secondaryImage: Drywall,
  },
];

const ProductList = () => {
  return (
    <section className="w-full bg-white py-12 px-4 shadow-md rounded-md mt-12">
      <div className="text-center mb-10">
        <h2 className="text-2xl md:text-3xl font-semibold text-gray-900 tracking-wide">
          Featured Products
        </h2>
        <p className="text-gray-500 mt-2">
          Discover high-quality materials and premium fittings for your next project
        </p>
      </div>

      <div className="grid gap-8 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {products.map((product) => (
          <Link
            href={`/products/${product.id}`}
            key={product.id}
            className="flex flex-col shadow-md hover:shadow-lg transition-shadow duration-300 bg-white rounded-md p-4 hover:-translate-y-1 transition-transform"
          >
            <div className="relative w-full h-64 rounded-md overflow-hidden">
              <Image
                src={product.primaryImage}
                alt={product.name}
                fill
                className="absolute object-cover z-10 hover:opacity-0 transition-opacity duration-500"
                sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
                priority={product.id <= 2}
              />
              <Image
                src={product.secondaryImage}
                alt={`${product.name} Alternate`}
                fill
                className="object-cover"
                sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
              />
            </div>

            <div className="flex justify-between items-center mt-4 px-2">
              <h3 className="font-medium text-lg text-gray-800">{product.name}</h3>
              <span className="font-bold text-yellow-700">{product.price}</span>
            </div>

            <p className="text-sm text-gray-500 mt-1 px-2 min-h-[40px]">{product.description}</p>

            <button
              className="mt-auto mx-2 rounded-2xl ring-1 ring-yellow-700 text-yellow-700 py-2 px-4 w-max hover:bg-yellow-700 hover:text-white transition-colors duration-300"
              onClick={(e) => e.preventDefault()}
            >
              Add to Cart
            </button>
          </Link>
        ))}
      </div>

      <div className="text-center mt-10">
        <Link href="/products">
          <button className="px-6 py-2 bg-yellow-500 text-white rounded-md hover:bg-yellow-600 transition-colors duration-300">
            Explore More Products
          </button>
        </Link>
      </div>
    </section>
  );
};

export default ProductList;
