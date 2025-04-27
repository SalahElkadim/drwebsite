
let menu_1 = document.querySelector(".nav-menu")
let nav_list = document.querySelector(".nav-list");


menu_1.onclick = function() {
menu_1.classList.toggle("move")
nav_list.classList.toggle("move_1");
}


// إظهار/إخفاء محادثة واتساب
const whatsappBtn = document.getElementById('whatsappBtn');
const whatsappChat = document.getElementById('whatsappChat');

whatsappBtn.addEventListener("click", function () {
  whatsappChat.style.display = whatsappChat.style.display === "block" ? "none" : "block";
});

// عند الضغط على زر الاستشارة
document.getElementById("consultBtn").addEventListener("click", function () {
  alert("سيتم توجيهك إلى نموذج طلب الاستشارة");
  window.open("#contact", "_self");
});

// إنشاء تأثير دوائر متحركة
setInterval(() => {
  const circle = document.createElement("div");
  circle.className = "pulse-circle";
  circle.style.width = "100%";
  circle.style.height = "100%";
  circle.style.top = "0";
  circle.style.left = "0";
  circle.style.animationDelay = "0s";
  document.querySelector(".consultation-cta").appendChild(circle);

  // إزالة الدوائر القديمة لمنع التراكم
  setTimeout(() => {
    circle.remove();
  }, 3000);
}, 1500);

// إضافة نص محسن لفتح نافذة الدردشة عند الضغط على زر الاتصال (استشارة)
document.getElementById('consultBtn').addEventListener('click', function() {
  // هنا يمكنك:
  // 1. فتح نموذج الاستشارة
  // 2. التمرير إلى قسم الاستشارة في الصفحة
  // 3. فتح رابط خارجي
  window.location.href = '#consultation';
});

// إضافة الكود الجديد الخاص بـ CSRF والـ WhatsApp
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // هل الكوكي يبدأ بالاسم اللي نبحث عنه؟
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// عند النقر على زر واتساب
document.getElementById('whatsapp-btn').addEventListener('click', function() {
    fetch('/api/whatsapp-link/', {
        method: 'GET',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // استخدام الـ CSRF Token هنا
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.link) {
            window.open(data.link, '_blank');  // فتح الرابط في نافذة جديدة
        } else {
            alert('Failed to get WhatsApp link.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


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
    train: "التدريب والتطوير",
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
    con: "تواصل معنا",
    req1: "حجز ندوة للمؤسسات الحكومية والخاصة",
    imp: "روابط قد تهمك",

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

