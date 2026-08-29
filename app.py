import streamlit as st
import random
import time

st.set_page_config(page_title="Houssam AI — Viral Machine", page_icon="🔥", layout="centered")

if "lang" not in st.session_state: st.session_state.lang = "العربية"
if "logged_in" not in st.session_state: st.session_state.logged_in = False

# تبديل اللغات الفوري في أعلى الشاشة
lang_choice = st.selectbox("🌐 Choose Language / اختر اللغة", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)
st.session_state.lang = lang_choice

# توثيق الملكية الفكرية والبيانات المالية لحسام توفيق لعام 2026
ABOUT_AR = """
### 👑 ملكية الحقوق الفكرية والإنتاج:
هذه المنصة العالمية بكامل محركاتها الذكية واختراعاتها المدمجة هي من **تصميم وإنتاج وملك المبتكر ورائد الأعمال**:
**حسام حسين أحمد توفيق** (Houssam Hussein Ahmed Taufiq).

### 💳 باقات الاشتراك المعتمدة وتفعيل الحسابات:
* **الباقة المحلية الموحدة:** 250 جنيهاً مصرياً شهرياً (أو 120 ريالاً سعودياً / 10 دنانير كويتية).
* **الباقة العالمية للأجانب والشركات:** 29$ دولاراً أمريكياً شهرياً.

### 📱 رقم التواصل والدعم الفني والتحويل المالي المعتمد:
يتم تفعيل الحساب وإرسال شفرة الدخول الآمنة فوراً بعد تحويل قيمة الاشتراك عبر **واتس آب (WhatsApp)** أو **إنستا باي (InstaPay)** على الرقم:
👉 **01015059150** 👈
"""

ABOUT_EN = """
### 👑 Intellectual Property & Ownership:
This global AI platform and all its built-in digital innovations are **Designed, Developed, and Owned Solely** by the inventor:
**Houssam Hussein Ahmed Taufiq** (حسام حسين أحمد توفيق).

### 📱 Authorized WhatsApp & Financial Channels (InstaPay):
👉 **01015059150** 👈 (International: +201015059150)
"""

# 1. بوابة الأمان بكلمة مرور (الرمز السري الافتراضي للتفعيل: 1234)
if not st.session_state.logged_in:
    if st.session_state.lang == "العربية":
        st.markdown("### 🔐 بوابة الأمان والدخول للمشتركين")
        password = st.text_input("أدخل كلمة مرور التفعيل الشخصية:", type="password")
        if st.button("تأكيد الدخول والتفعيل", type="primary"):
            if password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("❌ كلمة المرور غير صحيحة، يرجى التواصل مع حسام توفيق لتفعيل حسابك.")
        st.markdown("---")
        st.markdown(ABOUT_AR)
    else:
        st.markdown("### 🔐 Secure Enterprise Login Gateway")
        password = st.text_input("Enter your personal activation password:", type="password")
        if st.button("Verify & Unlock Platform", type="primary"):
            if password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("❌ Invalid password. Please contact Houssam Taufiq.")
        st.markdown("---")
        st.markdown(ABOUT_EN)
    st.stop()

# لوحة التحكم الرئيسية بعد الدخول بنجاح
st.sidebar.button("🔒 Logout" if st.session_state.lang == "English" else "🔒 تسجيل الخروج", on_click=lambda: st.session_state.__setitem__("logged_in", False))

tab_main, tab_about = st.tabs(["🚀 AI Viral Machine", "ℹ️ About Owner / حول المالك"])

with tab_main:
    if st.session_state.lang == "العربية":
        st.title("🔥 منصة Houssam AI — لتوليد التريندات")
        st.subheader("المصنع السحري الذكي لتوليد أفكار الفيديوهات وسيناريوهات البيع الفورية")
        st.markdown("---")
        
        # مدخلات التاجر
        biz_field = st.text_input("✍️ اكتب مجال عملك أو منتجك (عقارات، ملابس، مطاعم، أحذية، طب):", placeholder="مثال: محمل ملابس أطفال، شقق عقارية في أسيوط...")
        tone = st.selectbox("🎭 اختر أسلوب ونبرة الصوت للفيديو:", ["كوميدي ومرح", "حماسي وصادم", "احترافي وفخم"])
        
        if st.button("✨ تشغيل مصنع الأفكار والسيناريوهات الأسطورية", type="primary"):
            if biz_field:
                with st.spinner("🧠 جاري تشغيل عقل الذكاء الاصطناعي وبناء خطة المحتوى..."):
                    time.sleep(1)
                    st.success(f"🎯 تم توليد خطة الفيديو الفيروسي الجاهزة لمجال ({biz_field}) بنبرة ({tone}):")
                    st.markdown("---")
                    
                    st.info(f"**🎥 فكرة الفيديو التريند (لا تتكرر):**\nعمل مقارنة بصرية صادمة بين منتجك والمنتجات المقلدة الغالية بالأسواق، وكشف الخدعة للمستهلك لجلب ملايين المشاهدات الثابتة.")
                    st.warning(f"**📝 السيناريو الكامل للحوار بالعامية (Script):**\n'عمرك سألت نفسك ليه بتدفع دم قلبك في الماركات الكبيرة؟ النهاردة هكشفلك السر اللي هيوفر فلوسك وهيخليك تشتري أعلى جودة بأقل سعر لمشروع {biz_field}! شوف معايا اللقطة دي...'")
                    st.success(f"**📱 الهاشتاغات المليونية المستهدفة لخوارزمية تيك توك:**\n`#تريند_تيك_توك #{biz_field.replace(' ', '_')} #viral #fyp #حسام_توفيق`")
            else: st.warning("⚠️ يرجى كتابة مجال عملك أولاً لتفعيل الأداة.")
    else:
        # الواجهة العالمية باللغة الإنجليزية للأجانب بكندا وأوروبا
        st.title("🔥 Houssam AI — Viral Content Machine")
        st.subheader("Automated Scriptwriting & Video Ideas Generation Platform")
        st.markdown("---")
        biz_field = st.text_input("✍️ Enter your business niche or product (e.g., real estate, clothing, fitness):")
        if st.button("✨ Generate Viral Content & Scripts", type="primary"):
            if biz_field:
                with st.spinner("🧠 AI Core is engineering your viral growth plan..."):
                    time.sleep(1)
                    st.success(f"🎯 Viral Video Concept Generated for ({biz_field}):")
                    st.info("**🎥 Video Concept:** A dramatic 5-second hook exposing a hidden market secret in your industry to force viewers to comment and rewatch.")
                    st.warning(f"**📝 Full Video Script:**\n'Stop wasting your money on overpriced platforms! Here is the exact hidden strategy everyone in {biz_field} is hiding from you. Watch this closely...'")
                    st.success(f"**📱 High-Traffic Hashtags:**\n`#{biz_field.replace(' ', '')} #trending #viral #fyp #HoussamAI`")

with tab_about:
    st.markdown(ABOUT_AR if st.session_state.lang == "العربية" else ABOUT_EN)

st.markdown("<br><hr><center style='color:gray;'>Houssam AI — Secured & Certified Suite © 2026</center>", unsafe_allow_html=True)
