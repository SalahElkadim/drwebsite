
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
    req: "اطلب استشارة الآن",
    spe: "استشارات متخصصة في مجال اللغويات الجنائية وتحليل الاحتيال المالي",
    re: "اطلب استشارة",
    cer: "متخصصون معتمدون في علم اللغة الجنائي",
    for: "تحليل لغوي جنائي - اكتشاف عمليات التزوير - التحقيق في جرائم الاحتيال المالي - الخبرة في مجال الأدلة الجنائية",
    con: "تواصل معنا",
    req1: "حجز ندوة للمؤسسات الحكومية والخاصة",
    imp: "روابط قد تهمك",

    forensic_linguistic_services: "خدمات التحليل اللغوي الجنائي",
    forensic_linguistic_analysis:"تحليل لغوي جنائي باللغتين العربية والإنجليزية",
    authorship_identification: "تحديد الهوية اللغوية (البصمة اللغوية)",
    threat_fraud_detection: "كشف الإشارات اللغوية الدالة على التهديد والاحتيال",
    peer_review_content: "مراجعة الأقران للمحتوى القانوني والتجاري",
    legal_language_simplification: "تبسيط اللغة القانونية في العقود",
    legal_translation_services: "خدمات الترجمة القانونية",

    fraud_forgery_detection: "كشف الاحتيال والتزوير",
    verify_contracts: "التحقق من صحة العقود والاتفاقيات المكتوبة",
    validate_email_communications:"التحقق من مصداقية البريد الإلكتروني والاتصالات",
    review_financial_documents: "مراجعة شاملة للوثائق والسجلات المالية",
    user_behavior_analysis: "تحليل سلوك المستخدم",

    forensic_voice_analysis: "التحليل الصوتي الجنائي",
    voiceprint_analysis: "تحليل بصمة الصوت والسياق الصوتي",
    forensic_voice_reports: "إعداد تقارير خبرة جنائية صوتية",
    recording_authenticity_verification:"التحقق من صحة التسجيلات وكشف التلاعب الصوتي",
    confession_analysis: "تحليل الاعترافات المسجلة تحت الضغط",
    voice_comparison_demographics:"مقارنة الأصوات والكشف عن الخصائص الديموغرافية",
    expert_technical_services: "خدمات الخبراء الفنية للجهات القضائية",
    written_expert_reports: "تقديم تقارير خبرة فنية مكتوبة",
    expert_witness_testimony: "الشهادة كخبير أمام المحكمة",
  };

  function translateToArabic() {
    // نعيد اختيار العناصر كل مرة تضغط الزر
    const elementsToTranslate = document.querySelectorAll(".translatable");
    elementsToTranslate.forEach((el) => {
      const key = el.getAttribute("data-translate");
      if (arabicText[key]) {
        el.textContent = arabicText[key];
      }
    });

    const dropdownBtn = document.querySelector(".dropdown-btn");
    if (dropdownBtn) {
      dropdownBtn.textContent = "AR";
    }
  }

  const arBtn = document.getElementById("ar-btn");
  if (arBtn) {
    arBtn.addEventListener("click", function (e) {
      e.preventDefault();
      translateToArabic();
    });
  }

  const enBtn = document.getElementById("en-btn");
  if (enBtn) {
    enBtn.addEventListener("click", function (e) {
      e.preventDefault();
      location.reload();
    });
  }
});



