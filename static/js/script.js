function ExibirPag(anime){
    fetch(`/pages/${anime}`)
    .then(response => {

        if(!response.ok){
            throw new Error("a resposta de rede não foi bem sucedida")
        }
        return response.json()})
    .then(page =>{
        document.querySelector("body").innerHTML = page.page
    }).catch(error=>console.error("erro na busca de pagina", error))
}

document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('ImgCarousel');
    const images = [
        "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/7b6fff63-6d31-46e5-ab2c-c2756a283c74.png",
        "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/c956aa2d-0b85-4426-9446-502cf17e211f.png",
        "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/a22bb9d3-0e5c-44b0-a923-ff6836911f80.png"
    ];
    
    let currentImage = 0;
    
    function updateCarousel() {
        carousel.querySelector('div').style.backgroundImage = `url('${images[currentImage]}')`;
        currentImage = (currentImage + 1) % images.length;
    }
    
    // Change image every 5 seconds
    setInterval(updateCarousel, 5000);
    
    // Mobile menu toggle
    const menuButton = document.querySelector('button');
    const navMenu = document.querySelector('nav ul');
    
    menuButton.addEventListener('click', function() {
        navMenu.classList.toggle('hidden');
        navMenu.classList.toggle('flex');
        navMenu.classList.toggle('flex-col');
        navMenu.classList.toggle('absolute');
        navMenu.classList.toggle('top-full');
        navMenu.classList.toggle('left-0');
        navMenu.classList.toggle('right-0');
        navMenu.classList.toggle('bg-purple-600');
        navMenu.classList.toggle('p-4');
    });
});