document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll(".item");

    items.forEach(item => {
        item.addEventListener("click", function(event) {
            event.preventDefault(); // 直接のページ遷移を防ぐ

            const targetUrl = this.href; // クリックされたリンクのURLを取得

            // アニメーション（フェードアウト）
            gsap.to("body", {
                opacity: 0,
                duration: 1,
                onComplete: function() {
                    window.location.href = targetUrl; // アニメーション後に遷移
                }
            });
        });
    });
});