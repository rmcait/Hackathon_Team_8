document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll(".item");
    const numItems = items.length;
    let angle = 0;
    let currentIndex = 1; // 初期の前面アイテム

    // ✅ 矢印要素を取得
    const arrowRight = document.querySelector(".blinking-arrow");
    const arrowLeft = document.querySelector(".blinking-arrow-left");

    // ✅ 経験値の星を取得
    const stars = document.querySelectorAll(".exp-star");
    let exp = 0; // 現在の経験値（最大5）

    function rotateToIndex(targetIndex) {
        let diff = targetIndex - currentIndex;

        if (diff === 0) return; // すでに前面なら何もしない

        if (diff < 0) diff += numItems; // 差を正の値に変換

        if (diff <= numItems / 2) {
            // 右回転
            angle -= diff * (360 / numItems);
        } else {
            // 左回転
            angle += (numItems - diff) * (360 / numItems);
        }

        currentIndex = targetIndex;
        updateCarousel();
    }

    function updateCarousel() {
        const radiusX = 570;
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
                scale: index === currentIndex ? 1.5 : 1, // 前面アイテムを拡大
                zIndex: index === currentIndex ? 10 : 1,
                ease: "power1.inOut"
            });

            // ✅ どの item をクリックしても回転するよう修正
            item.onclick = function() {
                rotateToIndex(index);
                increaseExp(); // 経験値を増やす
            };
        });
    }

    // ✅ 右矢印（`.blinking-arrow`）をクリック → 次のアイテムに回転
    if (arrowRight) {
        arrowRight.addEventListener("click", function() {
            rotateToIndex((currentIndex + 1) % numItems);
        });
    }

    // ✅ 左矢印（`blinking-arrow-left`）をクリック → 前のアイテムに回転
    if (arrowLeft) {
        arrowLeft.addEventListener("click", function() {
            rotateToIndex((currentIndex - 1 + numItems) % numItems);
        });
    }

    // ✅ 経験値を増加させる関数
    function increaseExp() {
        if (exp < stars.length) {
            stars[exp].classList.add("active"); // 星を光らせる
            exp++; // 経験値を増加
        }

        if (exp === stars.length) {
            stars.forEach(star => star.classList.add("max")); // 全ての星を輝かせる
        }
    }

    updateCarousel();
});