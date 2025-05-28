document.addEventListener("DOMContentLoaded", function () {
  // تحسينات عامة للواجهة

  // إضافة تأثيرات للبطاقات
  const cards = document.querySelectorAll(".card");
  cards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.boxShadow = "0 8px 15px rgba(0, 0, 0, 0.15)";
    });

    card.addEventListener("mouseleave", function () {
      this.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)";
    });
  });

  // تحسين النماذج
  const forms = document.querySelectorAll("form");
  forms.forEach((form) => {
    const inputs = form.querySelectorAll("input, textarea, select");

    inputs.forEach((input) => {
      // إضافة تأثير عند التركيز على الحقول
      input.addEventListener("focus", function () {
        this.style.borderColor = "#3498db";
        this.style.boxShadow = "0 0 0 3px rgba(52, 152, 219, 0.3)";
      });

      input.addEventListener("blur", function () {
        this.style.borderColor = "#ddd";
        this.style.boxShadow = "none";
      });
    });
  });

  // رسالة تأكيد عند تقديم النموذج
  const submitButtons = document.querySelectorAll(
    'input[type="submit"], button'
  );
  submitButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      if (this.form && !this.form.checkValidity()) {
        // إذا كان النموذج غير صالح، عرض رسالة
        alert("الرجاء ملء جميع الحقول المطلوبة بشكل صحيح");
      }
    });
  });

  // تأثيرات للروابط
  const links = document.querySelectorAll("a");
  links.forEach((link) => {
    link.addEventListener("mouseenter", function () {
      this.style.opacity = "0.8";
    });

    link.addEventListener("mouseleave", function () {
      this.style.opacity = "1";
    });
  });
});
