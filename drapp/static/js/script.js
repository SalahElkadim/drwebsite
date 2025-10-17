        // تأثيرات التمرير والحركة
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // قائمة الهاتف المحمول
        const navMenu = document.getElementById('navMenu');
        const navList = document.getElementById('navList');
        
        navMenu.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navList.classList.toggle('active');
        });

        // إغلاق القائمة عند النقر خارجها
        document.addEventListener('click', function(e) {
            if (!navMenu.contains(e.target) && !navList.contains(e.target)) {
                navMenu.classList.remove('active');
                navList.classList.remove('active');
            }
        });

        // نافذة واتساب
        const whatsappBtn = document.getElementById('whatsappBtn');
        const whatsappChat = document.getElementById('whatsappChat');
        
        whatsappBtn.addEventListener('click', function() {
            whatsappChat.classList.toggle('active');
        });

        // إغلاق نافذة واتساب عند النقر خارجها
        document.addEventListener('click', function(e) {
            if (!whatsappBtn.contains(e.target) && !whatsappChat.contains(e.target)) {
                whatsappChat.classList.remove('active');
            }
        });

        // تأثيرات الظهور عند التمرير
        function revealOnScroll() {
            const reveals = document.querySelectorAll('.reveal-item');
            
            reveals.forEach(reveal => {
                const windowHeight = window.innerHeight;
                const elementTop = reveal.getBoundingClientRect().top;
                const elementVisible = 150;
                
                if (elementTop < windowHeight - elementVisible) {
                    reveal.classList.add('revealed');
                }
            });
        }

        window.addEventListener('scroll', revealOnScroll);
        revealOnScroll(); // تشغيل عند تحميل الصفحة

        // تأثير hover للبطاقات
        const serviceCards = document.querySelectorAll('.service-card');
        serviceCards.forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-10px) scale(1.02)';
                this.style.boxShadow = '0 20px 50px rgba(0, 0, 0, 0.15)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
                this.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.08)';
            });
        });

        // تأثير الكتابة المتدرجة
        // متغيرات عامة للتحكم في الكتابة
window.typewriterTimeout = null;
window.isTyping = false;

// تأثير الكتابة المتدرجة
function typeWriter(element, text, speed = 100) {
    // إلغاء أي كتابة سابقة
    if (window.typewriterTimeout) {
        clearTimeout(window.typewriterTimeout);
    }
    
    let i = 0;
    element.innerHTML = '';
    element.style.borderLeft = '3px solid white';
    window.isTyping = true;
    
    function type() {
        if (i < text.length && window.isTyping) {
            element.innerHTML += text.charAt(i);
            i++;
            window.typewriterTimeout = setTimeout(type, speed);
        } else {
            // إخفاء المؤشر بعد انتهاء الكتابة
            window.typewriterTimeout = setTimeout(() => {
                element.style.borderLeft = 'none';
                window.isTyping = false;
            }, 1000);
        }
    }
    type();
}

// دالة لإيقاف الكتابة
window.stopTypewriter = function() {
    if (window.typewriterTimeout) {
        clearTimeout(window.typewriterTimeout);
        window.typewriterTimeout = null;
    }
    window.isTyping = false;
}

document.addEventListener("DOMContentLoaded", function () {
    const typewriterElement = document.querySelector(".typewriter");
    if (typewriterElement) {
        const originalText = typewriterElement.textContent;
        typewriterElement.textContent = "";
        typewriterElement.classList.remove("typewriter");
        
        setTimeout(() => {
            typeWriter(typewriterElement, originalText, 40);
        }, 500);
    }
});

        // تأثيرات إضافية للتفاعل
        document.querySelectorAll('.floating-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                // تأثير النقر
                const ripple = document.createElement('div');
                ripple.style.position = 'absolute';
                ripple.style.borderRadius = '50%';
                ripple.style.background = 'rgba(255, 255, 255, 0.6)';
                ripple.style.transform = 'scale(0)';
                ripple.style.animation = 'ripple 0.6s linear';
                ripple.style.pointerEvents = 'none';
                
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = e.clientX - rect.left - size / 2 + 'px';
                ripple.style.top = e.clientY - rect.top - size / 2 + 'px';
                
                this.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
        });

        // CSS للتأثير المتموج
        const style = document.createElement('style');
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(2);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
        // تأثير التحويم على الروابط
        document.querySelectorAll('a, button').forEach(element => {
            element.addEventListener('mouseenter', () => {
                cursor.style.transform = 'scale(1.5)';
                cursor.style.background = 'radial-gradient(circle, rgba(0,0,0,1) 0%, transparent 70%)';
            });
            
            element.addEventListener('mouseleave', () => {
                cursor.style.transform = 'scale(1)';
                cursor.style.background = 'radial-gradient(circle, rgba(0,0,0,0.8) 0%, transparent 70%)';
            });
        });

        // تأثير التمرير السلس
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // تحديث الألوان بناءً على الوقت (وضع ليلي/نهاري تلقائي)
        function updateThemeBasedOnTime() {
            const hour = new Date().getHours();
            const root = document.documentElement;
            
            if (hour >= 6 && hour < 18) {
                // الوضع النهاري - أبيض أكثر
                root.style.setProperty('--primary-bg', 'linear-gradient(135deg, #f8f9fa 0%, #e9ecef 50%, #dee2e6 100%)');
            } else {
                // الوضع الليلي - أسود أكثر
                root.style.setProperty('--primary-bg', 'linear-gradient(135deg, #000000 0%, #111111 50%, #1a1a1a 100%)');
            }
        }

        // تحديث الموضوع عند تحميل الصفحة
        updateThemeBasedOnTime();
        
        // تحديث الموضوع كل ساعة
        setInterval(updateThemeBasedOnTime, 3600000);
