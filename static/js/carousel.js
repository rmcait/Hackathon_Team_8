document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll(".item");
    const numItems = items.length;
    let angle = 0;
    let currentIndex = 1;

    function updateCarousel() {
        const radius = 120;
        const angleIncrement = 360 / numItems;

        items.forEach((item, index) => {
            const theta = (angle + index * angleIncrement) * (Math.PI / 180);
            const x = Math.cos(theta) * radius;
            const y = Math.sin(theta) * radius;

            gsap.to(item, {
                x: x,
                y: y,
                duration: 0.5,
                scale: index === currentIndex ? 1.5 : 1, // 一番前のアイテムを拡大
                zIndex: index === currentIndex ? 10 : 1,
            });
        });
    }

    document.getElementById("next").addEventListener("click", function() {
        angle -= 360 / numItems;
        currentIndex = (currentIndex + 1) % numItems;
        updateCarousel();
    });

    updateCarousel();
});