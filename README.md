<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adri's Beauty Galore</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@700&display=swap');
        body {
            background-color: sienna;
        }
        .logo {
            font-family: 'Bodoni Moda', serif;
            font-weight: bold;
        }
    </style>
</head>
<body class="font-sans text-gray-800">
    <!-- Header -->
    <header class="bg-white shadow">
        <div class="container mx-auto flex justify-between items-center p-6">
            <h1 class="text-2xl logo text-sienna">Adri's Beauty Galore</h1>
            <nav>
                <a href="#about" class="text-white hover:text-gray-200 mx-4">About</a>
                <a href="#products" class="text-white hover:text-gray-200 mx-4">Products</a>
                <a href="#contact" class="text-white hover:text-gray-200 mx-4">Contact</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="bg-pink-200 py-20">
        <div class="container mx-auto text-center">
            <h2 class="text-4xl font-bold mb-4 text-pink-800">Welcome to Adri's Beauty Galore</h2>
            <p class="text-lg mb-8 text-pink-700">Your one-stop shop for all things beauty.</p>
            <img src="https://source.unsplash.com/random/800x600?cosmetics" alt="Cosmetic products" class="mx-auto rounded-lg shadow-lg">
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-16">
        <div class="container mx-auto text-center">
            <h3 class="text-3xl font-semibold mb-6 text-white">About Us</h3>
            <p class="text-lg text-white">At Adri's Beauty Galore, we believe in enhancing natural beauty with the finest cosmetic products. Our carefully curated selection ensures that you find the perfect match for your skin.</p>
        </div>
    </section>

    <!-- Products Section -->
    <section id="products" class="bg-white py-16">
        <div class="container mx-auto text-center">
            <h3 class="text-3xl font-semibold mb-6 text-sienna">Featured Products</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="p-6 bg-sienna rounded-lg shadow">
                    <img src="https://source.unsplash.com/random/300x300?lipstick" alt="Lipstick" class="w-full h-48 object-cover rounded">
                    <h4 class="text-xl font-bold mt-4 text-white">Matte Lipstick</h4>
                    <p class="text-white mt-2">$19.99</p>
                </div>
                <div class="p-6 bg-sienna rounded-lg shadow">
                    <img src="https://source.unsplash.com/random/300x300?skincare" alt="Skincare" class="w-full h-48 object-cover rounded">
                    <h4 class="text-xl font-bold mt-4 text-white">Hydrating Serum</h4>
                    <p class="text-white mt-2">$24.99</p>
                </div>
                <div class="p-6 bg-sienna rounded-lg shadow">
                    <img src="https://source.unsplash.com/random/300x300?eyeshadow" alt="Eyeshadow" class="w-full h-48 object-cover rounded">
                    <h4 class="text-xl font-bold mt-4 text-white">Eyeshadow Palette</h4>
                    <p class="text-white mt-2">$29.99</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-16 bg-pink-200">
        <div class="container mx-auto text-center">
            <h3 class="text-3xl font-semibold mb-6 text-sienna">Contact Us</h3>
            <form class="max-w-md mx-auto">
                <input type="text" placeholder="Name" class="w-full p-4 mb-4 border rounded-lg">
                <input type="email" placeholder="Email" class="w-full p-4 mb-4 border rounded-lg">
                <textarea placeholder="Your message" class="w-full p-4 mb-4 border rounded-lg"></textarea>
                <button type="submit" class="w-full bg-sienna text-white py-3 rounded-lg hover:bg-pink-700">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-sienna text-white py-6">
        <div class="container mx-auto text-center">
            <p>© 2024 Adri's Beauty Galore. All rights reserved.</p>
            <div class="flex justify-center space-x-4 mt-4">
                <a href="#" class="hover:text-gray-200">Facebook</a>
                <a href="#" class="hover:text-gray-200">Instagram</a>
                <a href="#" class="hover:text-gray-200">Twitter</a>
            </div>
        </div>
    </footer>
</body>
</html>
