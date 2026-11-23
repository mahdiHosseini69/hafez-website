document.addEventListener("DOMContentLoaded", function () {
    // حرکت نرم برای لینک‌های داخلی
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener("click", function (event) {
            const target = document.querySelector(link.getAttribute("href"));
            if (target) {
                event.preventDefault();
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // جلوگیری از ارسال چندباره فرم هنگام ثبت اطلاعات
    document.querySelectorAll('form').forEach(function (form) {
        form.addEventListener("submit", function () {
            const button = form.querySelector('button[type="submit"]');
            if (button) {
                button.disabled = true;
                button.style.opacity = "0.7";
            }
        });
    });
});
