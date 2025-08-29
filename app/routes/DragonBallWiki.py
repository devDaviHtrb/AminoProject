from flask import Blueprint, render_template, request, redirect, url_for, jsonify

DragonBallWiki = Blueprint("DragonBallWiki", __name__)
page = {"page": """<body class="min-h-screen flex flex-col bg-gradient-to-br from-yellow-400 via-orange-500 to-red-700 text-white">
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
    <img src="https://i.pinimg.com/originals/91/55/79/915579ae2fd1cc95d03b25a6e82dbd4b.jpg" 
         alt="Dragon Ball banner" 
         class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <h1 class="text-4xl md:text-6xl font-bold drop-shadow-lg">Dragon Ball Z Warriors</h1>
    </div>
  </header>

  <!-- Content -->
  <main class="container mx-auto px-6 py-12 flex-grow">
    <div class="bg-white text-gray-800 rounded-2xl shadow-xl p-8 max-w-4xl mx-auto">
      <h2 class="text-2xl font-bold text-yellow-600 mb-4">About Dragon Ball Z</h2>
      <p class="mb-6 leading-relaxed">
        <b>Dragon Ball Z</b>, created by Akira Toriyama, follows Goku and his friends 
        as they defend Earth from powerful foes. Known for legendary battles, transformations, 
        and iconic characters, DBZ remains one of the most influential anime worldwide.
      </p>

      <!-- Images -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <img src="https://i.pinimg.com/564x/26/7c/3c/267c3cfedb414e92ab1e2eecbe64388d.jpg" 
             alt="Goku Super Saiyan" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/25/c0/07/25c007b0d20558ee3db27c3a0e2df772.jpg" 
             alt="Vegeta" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/1a/48/c1/1a48c1a57f8f77b58596a463d1a8df61.jpg" 
             alt="Goku vs Frieza" class="rounded-lg shadow-md">
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="bg-gray-900 text-white py-6 text-center">
    <p class="text-gray-400">© 2025 AnimoApp - Dragon Ball Z Community</p>
  </footer>
</body>"""}
@DragonBallWiki.route("/DragonBallWiki")
def dragonBallWiki():
    return  jsonify(page)