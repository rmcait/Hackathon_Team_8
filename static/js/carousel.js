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

    if (uploadLink) {
        uploadLink.addEventListener("click", function(event) {
            event.preventDefault(); // 直接のページ遷移を防ぐ

            const targetUrl = this.href; // 遷移先のURL
            console.log("遷移先のURL:", targetUrl); // 遷移先URLを確認

            // `.item` を拡大＆四角にする
            uploadLink.classList.add("expanding");

            // `upload.html` の内容を取得して `.item` の中に埋め込む
            fetch(targetUrl)
                .then(response => response.text())
                .then(html => {
                    uploadLink.innerHTML = html; // `.item` 内に `upload.html` を挿入
                })
                .catch(error => console.error("Error:", error));
        });
    } else {
        console.warn("⚠️ 指定した要素 (.item[href]) が見つかりませんでした！");
    }

});