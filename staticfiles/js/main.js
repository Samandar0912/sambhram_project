document.addEventListener("DOMContentLoaded", (event) => {
    // Hamburger menyusi
    const ul_btn = document.querySelector(".ul_1 button");
    const ul_1 = document.querySelector(".ul_1");
    const gamburger = document.querySelector(".gamburger");
    
    console.log("yoo");
    gamburger.addEventListener("click", () => {
        ul_1.style.display = ul_1.style="display:block;"
    });



    ul_btn.addEventListener("click", () => {
        ul_1.style.display = "none";
    });
    



    // Swiper slider
    const swiper = new Swiper('.swiper', {
        direction: 'horizontal',
        loop: true,
        pagination: {
            el: '.swiper-pagination',
        },
        autoplay: {
            delay: 4000,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        scrollbar: {
            el: '.swiper-scrollbar',
        },
    });

    // Owl Carousel
    const owl = $('.owl-carousel');
    owl.owlCarousel({
        items: 5, // Standart holatda 5 ta element
        loop: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: true,
        responsive: {
            // Ekran o‘lchamiga qarab sozlamalar
            0: {
                items: 2, // 0px dan 576px gacha (mobil)
            },
            576: {
                items: 2, // 576px dan 768px gacha (katta mobil)
            },
            768: {
                items: 3, // 768px dan 992px gacha (planshet)
            },
            992: {
                items: 4, // 992px dan 1200px gacha (katta planshet/kichik desktop)
            },
            1200: {
                items: 5, // 1200px dan yuqori (desktop)
            }
        }
    });

    // Play tugmasi
    $('.play').on('click', function() {
        owl.trigger('play.owl.autoplay', [1000]);
    });

    // Stop tugmasi
    $('.stop').on('click', function() {
        owl.trigger('stop.owl.autoplay');
    });


    // Sticky Navbar (optimallashtirilgan)
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        const navbarHeight = navbar.offsetHeight;
        const toggleNavbar = () => {
            const scrollPosition = window.scrollY;
            if (scrollPosition > 50) {
                navbar.classList.add('navbar-fixed');
                document.body.style.paddingTop = `${navbarHeight}px`;
            } else {
                navbar.classList.remove('navbar-fixed');
                document.body.style.paddingTop = '0';
            }
        };

        // Dastlabki holatni tekshirish
        toggleNavbar();

        // Scroll eventni qo'shish
        window.addEventListener('scroll', toggleNavbar);
    }
});