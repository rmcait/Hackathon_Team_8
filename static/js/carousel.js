document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll(".item");
    const numItems = items.length;
    let angle = 0;
    let currentIndex = 1;

    function updateCarousel() {
        const radiusX = 650;
        const radiusY = 200;
        const angleIncrement = 360 / numItems;

        items.forEach((item, index) => {
            const theta = (angle + index * angleIncrement) * (Math.PI / 180);
            const x = Math.cos(theta) * radiusX;
            const y = Math.sin(theta) * radiusY;

            gsap.to(item, {
                x: x,
                y: y,
                duration: 0.5,
                scale: index === currentIndex ? 1.5 : 1, // 一番前のアイテムを拡大
                zIndex: index === currentIndex ? 10 : 1,
                ease: "power1.inOut"
            });

            item.onclick = function() {
                if (index === currentIndex) {
                    rotateToIndex(index);
            }
        };
    });
}


    document.getElementById("next").addEventListener("click", function() {
        angle -= 360 / numItems;
        currentIndex = (currentIndex + 1) % numItems;
        updateCarousel();
    });

    updateCarousel();



    const uploadLink = document.querySelector(".item[href]"); // アップロードページのリンク (1の要素)

    console.log("取得した要素:", uploadLink); // 要素の取得状況を確認

    
});