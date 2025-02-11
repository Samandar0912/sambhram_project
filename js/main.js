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




    const prev = document.querySelector("#prev");
    const next = document.querySelector("#next");
    
    let carouselVp = document.querySelector("#carousel-vp");
    
    let cCarouselInner = document.querySelector("#cCarousel-inner");
    let carouselInnerWidth = cCarouselInner.getBoundingClientRect().width;
    
    let leftValue = 0;
    
    // Variable used to set the carousel movement value (card's width + gap)
    const totalMovementSize =
      parseFloat(
        document.querySelector(".cCarousel-item").getBoundingClientRect().width,
        10
      ) +
      parseFloat(
        window.getComputedStyle(cCarouselInner).getPropertyValue("gap"),
        10
      );
    
    prev.addEventListener("click", () => {
      if (!leftValue == 0) {
        leftValue -= -totalMovementSize;
        cCarouselInner.style.left = leftValue + "px";
      }
    });
    
    next.addEventListener("click", () => {
      const carouselVpWidth = carouselVp.getBoundingClientRect().width;
      if (carouselInnerWidth - Math.abs(leftValue) > carouselVpWidth) {
        leftValue -= totalMovementSize;
        cCarouselInner.style.left = leftValue + "px";
      }
    });
    
    const mediaQuery510 = window.matchMedia("(max-width: 510px)");
    const mediaQuery770 = window.matchMedia("(max-width: 770px)");
    
    mediaQuery510.addEventListener("change", mediaManagement);
    mediaQuery770.addEventListener("change", mediaManagement);
    
    let oldViewportWidth = window.innerWidth;
    
    function mediaManagement() {
      const newViewportWidth = window.innerWidth;
    
      if (leftValue <= -totalMovementSize && oldViewportWidth < newViewportWidth) {
        leftValue += totalMovementSize;
        cCarouselInner.style.left = leftValue + "px";
        oldViewportWidth = newViewportWidth;
      } else if (
        leftValue <= -totalMovementSize &&
        oldViewportWidth > newViewportWidth
      ) {
        leftValue -= totalMovementSize;
        cCarouselInner.style.left = leftValue + "px";
        oldViewportWidth = newViewportWidth;
      }
    }
    