let ul_btn = document.querySelector(".ul_1 button");
let ul_1 = document.querySelector(".ul_1");
let gamburger = document.querySelector(".gamburger");

if (gamburger && ul_1) {
    gamburger.addEventListener("click", () => {
        ul_1.style.display = "block";
        console.log("yoo");
    });
}

if (ul_btn) {
    ul_btn.addEventListener("click", () => {
        ul_1.style.display = "none";
    });
}


document.addEventListener("DOMContentLoaded", (event) => {
    const swiper = new Swiper('.swiper', {
        // Optional parameters
        direction: 'horizontal',
        loop: true,
    
        // If we need pagination
        pagination: {
            el: '.swiper-pagination',
        },
        autoplay: {
                delay: 4000,
        },
    
        // Navigation arrows
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    
        // And if we need scrollbar
        scrollbar: {
            el: '.swiper-scrollbar',
        },
        });
    
    
        
    
    var owl = $('.owl-carousel');
        owl.owlCarousel({
            items:5,
            loop:true,
            margin:10,
            autoplay:true,
            autoplayTimeout:4000,
            autoplayHoverPause:true
        });
        $('.play').on('click',function(){
            owl.trigger('play.owl.autoplay',[1000])
        })
        $('.stop').on('click',function(){
            owl.trigger('stop.owl.autoplay')
        })
    
    
        window.addEventListener('scroll', function() {
            const navbar = document.querySelector('.navbar');
            const navbarHeight = navbar.offsetHeight;
            const scrollPosition = window.scrollY;
        
            if (scrollPosition > 50) { /* 50px pastga tushganda */
                navbar.classList.add('navbar-fixed');
                document.body.style.paddingTop = `${navbarHeight}px`;
            } else {
                navbar.classList.remove('navbar-fixed');
                document.body.style.paddingTop = '0';
            }
        });
    



});
    