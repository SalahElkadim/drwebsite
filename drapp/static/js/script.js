
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

const consultBtn = document.getElementById("consultBtn");
if (consultBtn) {
  consultBtn.addEventListener("click", function () {
    document
      .getElementById("consultation-section")
      ?.scrollIntoView({ behavior: "smooth" });
  });
}

// إنشاء دوائر متحركة إضافية
setInterval(() => {
  const circle = document.createElement("div");
  circle.className = "pulse-circle";
  circle.style.width = "100%";
  circle.style.height = "100%";
  circle.style.top = "0";
  circle.style.left = "0";
  circle.style.animationDelay = "0s";

  // إزالة الدوائر القديمة لمنع تراكمها
  setTimeout(() => {
    circle.remove();
  }, 3000);
}, 1500);

document.addEventListener("DOMContentLoaded", function () {
  const englishText = {
    home: "Home",
    about: "About Us",
    forensic: "Forensic Services",
    ling: "Translation & Marketing",
    financial: "Financial Fraud Analysis",
    train: "Training & Development",
    book: "Book a Consultation",
    test: "Testimonials",
    faq: "FAQs",
    help: "Help",
    privacy: "Privacy Policy",
    contact: "Contact Us",
    req: "Request Consultation Now",
    spe: "Specialized consultations in forensic linguistics and financial fraud analysis",
    re: "Request a Consultation",
    cer: "Certified Experts in Forensic Linguistics",
    for: "Forensic linguistic analysis – forgery detection – financial fraud investigation – expertise in forensic evidence",
    con: "Contact Us",
    req1: "Book a Seminar for Government or Private Institutions",
    imp: "Important Links",

    forensic_linguistic_services: "Forensic Linguistic Services",
    forensic_linguistic_analysis:"Forensic Linguistic Analysis in Arabic and English",
    authorship_identification:"Authorship Identification (Linguistic Fingerprint)",
    threat_fraud_detection:"Detection of Linguistic Indicators of Threat and Fraud",
    peer_review_content: "Peer Review for Legal and Commercial Content",
    legal_language_simplification: "Legal Language Simplification in Contracts",
    legal_translation_services: "Legal Translation Services",

    fraud_forgery_detection: "Fraud and Forgery Detection",
    verify_contracts: "Verification of Written Contracts and Agreements",
    validate_email_communications:"Email and Communication Credibility Verification",
    review_financial_documents:"Comprehensive Review of Financial Documents and Records",
    user_behavior_analysis: "User Behavior Analysis",

    forensic_voice_analysis: "Forensic Voice Analysis",
    voiceprint_analysis: "Voiceprint and Audio Context Analysis",
    forensic_voice_reports: "Preparation of Forensic Audio Expert Reports",
    recording_authenticity_verification:"Recording Authenticity Verification and Tampering Detection",
    confession_analysis: "Analysis of Recorded Confessions Under Pressure",
    voice_comparison_demographics:"Voice Comparison and Demographic Feature Detection",
    expert_technical_services:"Expert Technical Services for Judicial Authorities",
    written_expert_reports: "Provision of Written Expert Reports",
    expert_witness_testimony: "Expert Witness Testimony in Court",
    fff: "Specialized services in forensic linguistics, fraud detection, authorship analysis, and document validation.",
    hhh: "Our expertise helps clients, legal professionals, and institutions detect deception, uncover forgery, and analyze linguistic evidence.",
    iii: "If you are interested, contact us now",
    trademark_marketing_title: "Trademark and Marketing Solutions",
    trademark_marketing_subtitle:"Comprehensive services for brand protection, registration, strategic development, and digital growth",
    trademark_marketing_intro:"We help individuals and companies protect their commercial identity and grow their market presence through legal and creative strategies",

    trademark_services_title: "Trademark Services",
    linguistic_analysis_trademark:"Linguistic Analysis for Local and International Trademark Disputes",
    develop_brand_strategy: "Brand Strategy Development",
    brand_identity_design: "Visual Identity Design",
    market_competitor_analysis: "Market and Competitor Analysis",
    linguistic_consulting_brand: "Linguistic Consulting for Brand Building",
    legal_consulting_protection: "Legal Consulting and Brand Protection",
    brand_reputation_protection: "Brand Reputation Protection",

    digital_marketing_services_title: "Digital Marketing Services",
    develop_digital_marketing_strategy:"Digital Strategy Development for Online Presence",
    online_reputation_monitoring: "Online Reputation Monitoring & PR",
    seo_service: "Search Engine Optimization (SEO)",
    ppc_campaigns: "Pay-Per-Click Campaign Management",

    brand_protection_growth_cta: "Need help with brand protection or growth?",
    contact_our_team: "Contact Our Team",
    training_title: "Training & Development",
    training_subtitle:"Specialized programs in forensic linguistics, fraud detection, and communication analysis for professionals and institutions",

    training_intro:"We offer expert-led training sessions and workshops to enhance investigative, linguistic, and analytical skills for identifying deception and supporting legal accountability.",

    specialized_training_title: "Specialized Training Sessions",
    session1:"Expert-led sessions focused on linguistic evidence in legal investigations",
    session2:"Interactive workshops on identifying fraudulent linguistic patterns",
    session3:"Training programs to improve skills in analyzing fraudulent documents and messages",

    practical_training_title: "Practical Training Solutions",
    practical1:"Training kits to develop linguistic strategies for fraud detection in interviews",
    practical2: "Webinars on language and financial crime for legal awareness",
    practical3:"Workshops to detect misleading language and fraud in financial documents",

    advanced_training_title:"Advanced Communication & Forensic Analysis Training",
    advanced1:"Practical training in authorship attribution and threat assessment",
    advanced2:"Workshops on analyzing fraud communication in digital platforms",

    cta_title: "Need Training & Development?",
    cta_button: "Contact Us",
  };

  function translateToEnglish() {
    const elementsToTranslate = document.querySelectorAll(".translatable");
    elementsToTranslate.forEach((el) => {
      const key = el.getAttribute("data-translate");
      if (englishText[key]) {
        el.textContent = englishText[key];
      }
    });

    const dropdownBtn = document.querySelector(".dropdown-btn");
    if (dropdownBtn) {
      dropdownBtn.textContent = "EN";
    }
  }

  const enBtn = document.getElementById("en-btn");
  if (enBtn) {
    enBtn.addEventListener("click", function (e) {
      e.preventDefault();
      translateToEnglish();
    });
  }

  const arBtn = document.getElementById("ar-btn");
  if (arBtn) {
    arBtn.addEventListener("click", function (e) {
      e.preventDefault();
      location.reload(); // تُرجع للمحتوى العربي الأساسي
    });
  }
});


