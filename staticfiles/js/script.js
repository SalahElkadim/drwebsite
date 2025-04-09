
let menu_1 = document.querySelector(".nav-menu")
let nav_list = document.querySelector(".nav-list");


menu_1.onclick = function() {
menu_1.classList.toggle("move")
nav_list.classList.toggle("move_1");
}




const whatsappBtn = document.getElementById('whatsappBtn');
        const whatsappChat = document.getElementById('whatsappChat');

        // عند النقر على الزر
        whatsappBtn.addEventListener("click", function () {
          // الطريقة 1: فتح محادثة مباشرة (الأفضل)
        whatsappChat.style.display =
            whatsappChat.style.display === "block" ? "none" : "block";
        });
document.getElementById('consultBtn').addEventListener('click', function() {
            // هنا يمكنك:
            // 1. فتح نموذج الاستشارة
            // document.getElementById('consultationForm').style.display = 'block';
            
            // 2. التمرير إلى قسم الاستشارة في الصفحة
            // document.getElementById('consultation-section').scrollIntoView();
            
            // 3. فتح رابط خارجي
            window.location.href = '#consultation'});


document.getElementById("consultBtn").addEventListener("click", function () {
  // هنا يمكنك:
  // 1. فتح نموذج الاستشارة
  // 2. التمرير إلى قسم الاتصال
  // 3. فتح نافذة دردشة

  // مثال: فتح رابط خارجي
  window.open("#contact", "_self");

  // أو عرض رسالة
  alert("سيتم توجيهك إلى نموذج طلب الاستشارة");
});

// إنشاء دوائر متحركة إضافية
setInterval(() => {
  const circle = document.createElement("div");
  circle.className = "pulse-circle";
  circle.style.width = "100%";
  circle.style.height = "100%";
  circle.style.top = "0";
  circle.style.left = "0";
  circle.style.animationDelay = "0s";
  document.querySelector(".consultation-cta").appendChild(circle);

  // إزالة الدوائر القديمة لمنع تراكمها
  setTimeout(() => {
    circle.remove();
  }, 3000);
}, 1500);


document.addEventListener("DOMContentLoaded", function () {
  // العناصر التي تريد ترجمتها (أضف class="translatable" لها في HTML)
  const elementsToTranslate = document.querySelectorAll(".translatable");

  // النصوص العربية (يمكنك إضافة المزيد)
  const arabicText = {
    home: "الرئيسية",
    about: "من نحن",
    forensic: "الخدمات الجنائية",
    ling: "خدمات الترجمة والتسويق",
    financial: "تحليل الاحتيال المالي",
    book: "احجز استشارة",
    test: "شهادات",
    faq: "الأسئلة الشائعة",
    help: "المساعدة",
    privacy: "سياسة الخصوصية",
    contact: "تواصل معنا",
    req: " اطلب استشارة الآن",
    spe: "استشارات متخصصة في مجال اللغويات الجنائية وتحليل الاحتيال المالي",
    re: "اطلب استشارة",
    cer: "متخصصون معتمدون في علم اللغة الجنائي",
    for: "تحليل لغوي جنائي - اكتشاف عمليات التزوير - التحقيق في جرائم الاحتيال المالي - الخبرة في مجال الأدلة الجنائية",
    con:"تواصل معنا",
    // أضف بقية النصوص هنا...
  };

  

  // زر AR
  document.getElementById("ar-btn").addEventListener("click", function (e) {
    e.preventDefault();
    translateToArabic();
  });

  // زر EN
  document.getElementById("en-btn").addEventListener("click", function (e) {
    location.reload();
  });

  // وظيفة الترجمة للعربية
  function translateToArabic() {
    elementsToTranslate.forEach((el) => {
      const key = el.getAttribute("data-translate");
      if (arabicText[key]) {
        el.textContent = arabicText[key];
      }
    });
    document.querySelector(".dropdown-btn").textContent = "AR";
  }

  
});

