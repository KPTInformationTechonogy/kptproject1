import Link from "next/link";

/**
 * ProductList Component with Background Image
 *
 * Highlights Kano Process Trading Company's core offerings with a styled background,
 * overlay, and responsive layout.
 */
const ProductList = () => {
    return (
        <section
            className="relative w-full py-12 md:py-16 px-4 sm:px-6 lg:px-8 bg-cover bg-center"
            style={{
                backgroundImage: "url('/images/bg-building-materials.jpg')", // Change to your own image path
            }}
            aria-labelledby="product-section-heading"
        >
            {/* Overlay */}
            <div className="absolute inset-0 bg-white backdrop-blur-sm"></div>

            <div className="relative max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10 items-center text-gray-800">
                
                {/* Text Content */}
                <article className="space-y-6">
                    <header>
                        <h2
                            id="product-section-heading"
                            className="text-3xl md:text-4xl font-extrabold leading-tight"
                        >
                            <span className="text-blue-300">Kano Process Trading Company</span> — 
                            Your Trusted Partner for Quality Building Solutions
                        </h2>
                    </header>

                    <div className="text-lg space-y-4 text-justify leading-relaxed">
                        <p>
                            We specialize in premium <strong>furniture materials</strong>, 
                            <strong> plumbing supplies</strong>, and <strong> building materials</strong>, 
                            complemented by expert <strong> home decoration services</strong>.
                        </p>

                        <p className="text-justify">
                            Our value-added services include <strong> precision cutting</strong> and 
                            <strong> professional edging</strong>, offering a complete solution from 
                            procurement to installation.
                        </p>

                        <p className="font-semibold text-justify">
                            With secure payment options and our quality guarantee, 
                            we deliver consistent excellence for your construction and interior design needs.
                        </p>
                    </div>

                    <footer>
                        <Link
                            href="/products"
                            className="inline-block bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-md font-medium transition-colors duration-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-400 focus-visible:ring-offset-2"
                            aria-label="Explore our products and services"
                        >
                            Learn More
                        </Link>
                    </footer>
                </article>

                {/* Embedded Video */}
                <aside className="relative aspect-video rounded-xl overflow-hidden shadow-lg">
                    <iframe
                        src="https://www.youtube.com/embed/xwRq109IO6Y"
                        title="Kano Process Trading Company - Product Showcase"
                        className="absolute inset-0 w-full h-full"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                        loading="lazy"
                    />
                </aside>
            </div>
        </section>
    );
};

export default ProductList;
