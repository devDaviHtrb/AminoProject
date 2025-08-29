from flask import Blueprint, render_template, request, redirect, url_for, jsonify

NarutoWiki = Blueprint("NarutoWiki", __name__)
page={"page":"""<body class="min-h-screen flex flex-col bg-gradient-to-br from-orange-400 via-yellow-500 to-red-600 text-white">
  <!-- Navigation -->
  <nav class="anime-gradient py-4 px-6 shadow-lg">
    <div class="container mx-auto flex justify-between items-center">
      <a href="/" class="flex items-center space-x-2">
        <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-lg">
          <span class="text-2xl font-bold text-purple-600">A</span>
        </div>
        <span class="logo-text text-2xl font-bold">AnimoApp</span>
      </a>
    </div>
  </nav>

  <!-- Banner -->
  <header class="relative h-72 md:h-96 overflow-hidden">
    <img src="https://i.pinimg.com/originals/55/4f/13/554f13f8f80a6df3d7d60470f6e8d98f.jpg" 
         alt="Naruto banner" 
         class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <h1 class="text-4xl md:text-6xl font-bold drop-shadow-lg">Naruto Universe</h1>
    </div>
  </header>

  <!-- Content -->
  <main class="container mx-auto px-6 py-12 flex-grow">
    <div class="bg-white text-gray-800 rounded-2xl shadow-xl p-8 max-w-4xl mx-auto">
      <h2 class="text-2xl font-bold text-orange-600 mb-4">About Naruto</h2>
      <p class="mb-6 leading-relaxed">
        <b>Naruto</b>, created by Masashi Kishimoto, follows the journey of Naruto Uzumaki, 
        a young ninja who dreams of becoming Hokage and earning the respect of his village. 
        Along his path, he battles powerful enemies, forges deep friendships, and learns 
        the true meaning of strength.
      </p>

      <!-- Images -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <img src="https://i.pinimg.com/564x/8c/f7/38/8cf738f48db7dded05b7b7c3c2c4d476.jpg" 
             alt="Naruto and Sasuke" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/2b/2b/65/2b2b65e682e06698c649f42e8a2a97b0.jpg" 
             alt="Team 7" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/66/02/c2/6602c24e14a72e1e858b51a0a1e2f8d8.jpg" 
             alt="Naruto Kurama Mode" class="rounded-lg shadow-md">
      </div>
    </div>
  </main>
  <!-- Footer -->
  <footer class="bg-gray-900 text-white py-6 text-center">
    <p class="text-gray-400">© 2025 AnimoApp - Naruto Community</p>
  </footer>
</body>"""}
@NarutoWiki.route("/NarutoWiki")
def narutoWiki():
     return  jsonify(page)