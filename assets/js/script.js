// Initialize GSAP ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Navbar Scroll Effect
    const nav = document.getElementById('main-nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    // 2. Hero Section Entrance Animation
    const heroTl = gsap.timeline();

    heroTl.to('#hero-title', {
        opacity: 1,
        y: 0,
        duration: 1,
        ease: 'power4.out'
    })
    .to('#hero-desc', {
        opacity: 1,
        y: 0,
        duration: 0.8,
        ease: 'power3.out'
    }, '-=0.6')
    .to('#hero-btns', {
        opacity: 1,
        y: 0,
        duration: 0.8,
        ease: 'power3.out'
    }, '-=0.6')
    .to('#hero-img', {
        opacity: 1,
        scale: 1,
        duration: 1.2,
        ease: 'elastic.out(1, 0.8)'
    }, '-=1');

    // 3. Scroll Reveal Animations
    const reveals = document.querySelectorAll('.reveal');

    reveals.forEach((el) => {
        gsap.to(el, {
            scrollTrigger: {
                trigger: el,
                start: 'top 85%', // Start when top of element hits 85% of viewport
                toggleActions: 'play none none none', // Play once
            },
            opacity: 1,
            y: 0,
            duration: 1,
            ease: 'power3.out',
            stagger: 0.2
        });
    });

    // 4. Smooth Scroll for Navigation Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 5. Card Hover Micro-interactions (handled by CSS but we can add GSAP)
    const cards = document.querySelectorAll('.service-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card.querySelector('i'), {
                scale: 1.2,
                rotate: 5,
                duration: 0.3,
                ease: 'power2.out'
            });
        });
        card.addEventListener('mouseleave', () => {
            gsap.to(card.querySelector('i'), {
                scale: 1,
                rotate: 0,
                duration: 0.3,
                ease: 'power2.in'
            });
        });
    });
});
