from flask import jsonify, Blueprint

pages = {"Dragon Ball":{ "name":"Dragon Ball", "page": """<body class="min-h-screen flex flex-col bg-gradient-to-br from-yellow-400 via-orange-500 to-red-700 text-white">
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
</body>"""},"Bleach":{ "name":"Bleach","page":"""<body class="min-h-screen flex flex-col bg-gradient-to-br from-blue-500 via-indigo-600 to-gray-900 text-white">
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
    <img src="https://i.pinimg.com/originals/9f/f3/cc/9ff3cc727f9f08f5292bb2ab2e1fa532.jpg" 
         alt="Bleach banner" 
         class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <h1 class="text-4xl md:text-6xl font-bold drop-shadow-lg">Bleach Society</h1>
    </div>
  </header>

  <!-- Content -->
  <main class="container mx-auto px-6 py-12 flex-grow">
    <div class="bg-white text-gray-800 rounded-2xl shadow-xl p-8 max-w-4xl mx-auto">
      <h2 class="text-2xl font-bold text-blue-600 mb-4">About Bleach</h2>
      <p class="mb-6 leading-relaxed">
        <b>Bleach</b>, created by Tite Kubo, tells the story of Ichigo Kurosaki, 
        a teenager who gains the powers of a Soul Reaper. With these powers, 
        he must defend humanity from evil spirits and guide departed souls to the afterlife.
      </p>

      <!-- Images -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <img src="https://i.pinimg.com/564x/dc/66/6f/dc666ff409f3e4d5e0de14306d2db342.jpg" 
             alt="Ichigo Bankai" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/77/2b/8f/772b8f99a15fa84f50e93b9b5687cbf3.jpg" 
             alt="Gotei 13" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/64/d0/4a/64d04a61ec6904fbbfe65d3992f20593.jpg" 
             alt="Ichigo Hollow form" class="rounded-lg shadow-md">
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="bg-gray-900 text-white py-6 text-center">
    <p class="text-gray-400">© 2025 AnimoApp - Bleach Community</p>
  </footer>"""},"Naruto":{ "name":"Naruto", "page":"""<body class="min-h-screen flex flex-col bg-gradient-to-br from-orange-400 via-yellow-500 to-red-600 text-white">
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
</body>"""}, "One Piece":{"page":"""<body class="min-h-screen flex flex-col bg-gradient-to-br from-sky-400 via-blue-500 to-indigo-700 text-white">
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
    <img src="https://i.pinimg.com/originals/ed/7f/f1/ed7ff15a22a4f10a8144c7e62e4e32e1.jpg" 
         alt="One Piece banner" 
         class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <h1 class="text-4xl md:text-6xl font-bold drop-shadow-lg">One Piece Crew</h1>
    </div>
  </header>

  <!-- Content -->
  <main class="container mx-auto px-6 py-12 flex-grow">
    <div class="bg-white text-gray-800 rounded-2xl shadow-xl p-8 max-w-4xl mx-auto">
      <h2 class="text-2xl font-bold text-blue-600 mb-4">About One Piece</h2>
      <p class="mb-6 leading-relaxed">
        <b>One Piece</b>, created by Eiichiro Oda, follows Monkey D. Luffy and his crew 
        of pirates as they sail the Grand Line in search of the legendary treasure known 
        as the One Piece. A story of adventure, friendship, and dreams, it is one of the 
        longest-running and most beloved anime series.
      </p>

      <!-- Images -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <img src="https://i.pinimg.com/564x/35/3a/6b/353a6bda34f03ab76394eaa5d4956a68.jpg" 
             alt="Luffy Gear 4" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/30/0a/07/300a07d6e96cb342f986e73da88fbdd8.jpg" 
             alt="Straw Hat Crew" class="rounded-lg shadow-md">
        <img src="https://i.pinimg.com/564x/82/70/1a/82701a7402d4a6181178f2688a9a8cd3.jpg" 
             alt="Luffy vs Kaido" class="rounded-lg shadow-md">
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="bg-gray-900 text-white py-6 text-center">
    <p class="text-gray-400">© 2025 AnimoApp - One Piece Community</p>
  </footer>
</body>"""}}

getPage = Blueprint("get_page", __name__)

@getPage.route("/pages/<anime>")
def get_page(anime):
    animePage = pages.get(anime, {
        "id":"desconhecido",
        "name":"desconhecido",
        "page":"<p>error</p>"
    })
    return jsonify(animePage)