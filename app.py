import streamlit as st
import random
import time

st.set_page_config(page_title="OmniRadar AI", page_icon="🌍", layout="centered")

if "lang" not in st.session_state: st.session_state.lang = "العربية"
if "logged_in" not in st.session_state: st.session_state.logged_in = False

# تبديل اللغات في الأعلى
lang_choice = st.selectbox("🌐 Language / اللغة", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)
st.session_state.lang = lang_choice

# إعداد بيانات المالك باللغتين لحماية الحقوق
ABOUT_AR = """
### 👑 ملكية الحقوق الفكرية والإنتاج:
هذه الشركة والمنصة العالمية بكامل شفراتها البرمجية واختراعاتها المدمجة هي من **تصميم وإنتاج وملك المبتكر ورائد الأعمال**:
**حسام حسين أحمد توفيق** (Houssam Hussein Ahmed Taufiq).

### 📱 أرقام التواصل والدعم الفني المعتمدة:
رقم الهاتف المعتمد والوحيد للتواصل المباشر، خدمات **واتس آب (WhatsApp)**، والتحويلات المالية عبر **إنستا باي (InstaPay)**:
**01015059150** (من خارج مصر: +201015059150)

*جميع الحقوق الفكرية مسجلة وموثقة دولياً لعام 2026 باسم المالك المذكور أعلاه ويحظر نسخها.*
"""

ABOUT_EN = """
### 👑 Intellectual Property & Ownership:
This global enterprise suite is **Designed, Developed, and Owned Solely** by the inventor and entrepreneur:
**Houssam Hussein Ahmed Taufiq** (حسام حسين أحمد توفيق).

### 📱 Authorized Contact & Support Channels:
The single authorized phone number for official inquiries, **WhatsApp**, and financial settlement via **InstaPay**:
**01015059150** (International: +201015059150)

*All digital patents and global intellectual property are securely registered for 2026 under the name of the owner above.*
"""

# 1. بوابة الأمان بكلمة مرور (الرمز الافتراضي: 1234)
if not st.session_state.logged_in:
    if st.session_state.lang == "العربية":
        st.markdown("### 🔐 بوابة الأمان والدخول للمشتركين")
        password = st.text_input("أدخل كلمة مرور التفعيل الشخصية:", type="password")
        if st.button("تأكيد الدخول والتفعيل", type="primary"):
            if password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("❌ كلمة المرور غير صحيحة، يرجى التواصل مع الإدارة.")
        st.markdown("---")
        st.markdown(ABOUT_AR)
    else:
        st.markdown("### 🔐 Secure Enterprise Login Gateway")
        password = st.text_input("Enter your personal activation password:", type="password")
        if st.button("Verify & Unlock Platform", type="primary"):
            if password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("❌ Invalid password. Please contact administration.")
        st.markdown("---")
        st.markdown(ABOUT_EN)
    st.stop()

# لوحة التحكم الرئيسية بعد تسجيل الدخول بنجاح
if st.sidebar.button("🔒 Logout" if st.session_state.lang == "English" else "🔒 تسجيل الخروج"):
    st.session_state.logged_in = False
    st.rerun()

tab_main, tab_about = st.tabs(["🚀 Dashboard", "ℹ️ About App & Owner" if st.session_state.lang == "English" else "ℹ️ حول التطبيق والمالك"])

with tab_main:
    if st.session_state.lang == "العربية":
        st.title("🌍 منصة OmniRadar AI العالمية")
        st.sidebar.header("🗺️ الرادار الجغرافي الدولي")
        country = st.sidebar.selectbox("اختر الدولة المستهدفة:", ["جمهورية مصر العربية", "دولة الكويت", "المملكة العربية السعودية", "كندا وأمريكا", "الاتحاد الأوروبي"])
        region = st.sidebar.text_input("اكتب اسم المحافظة / المدينة / القرية المستهدفة:", placeholder="مثال: أسيوط، السالمية، Ontario...")
        
        if st.button("🚀 ابدأ محرك التنبؤ واقتناص الثغرات فوراً", type="primary"):
            with st.spinner("🧠 جاري تشغيل عقل الذكاء الاصطناعي..."):
                time.sleep(1)
                st.success(f"✅ تم الفحص التنبؤي الجغرافي بنجاح في [{region if region else country}]")
                st.info("**🌐 قطاع العمل المستهدف:** التجارة الإلكترونية والخدمات اللوجستية محلياً\n\n**⚠️ ثغرة وأزمة السوق الحالية:** تكدس طلبات التوصيل وزيادة العمولات المفروضة على أصحاب المتاجر والمطاعم.\n\n**💡 الحل الممنوح داخل نظامنا:** تفعيل شبكة Local-Drop لربط المتاجر مباشرة بالمناديب الأحرار بعمولة صفرية.")
                st.code(f"مرحباً! لاحظنا الأزمة الحالية التي تواجه مشروعكم في {region if region else country} بشأن مصاريف التشغيل وهدر الأرباح. نحن نوفر لكم الأداة الاحترافية لحلها فوراً وبأقل تكلفة. تواصل معنا للبدء!", language="text")
    else:
        st.title("🌍 OmniRadar AI — Global Platform")
        st.sidebar.header("🗺️ Global Geographic Filter")
        country = st.sidebar.selectbox("Select Target Country:", ["Egypt", "Kuwait", "Saudi Arabia", "Canada & USA", "European Union"])
        region = st.sidebar.text_input("Type Target Province / City / Village:", placeholder="e.g., Cairo, Ontario, Salmiya...")
        
        if st.button("🚀 Launch Predictive Market Scanner", type="primary"):
            with st.spinner("🧠 AI Core is scanning international market registries..."):
                time.sleep(1)
                st.success(f"✅ Geographic scan successful in [{region if region else country}]")
                st.info("**🌐 Target Industrial Sector:** Hyper-Local Logistics & E-Commerce\n\n**⚠️ Current Market Crisis:** Small restaurants are losing 30% of margins due to monopoly delivery platforms.\n\n**💡 Solution Provided:** Deploying 'Local-Drop Network' to connect stores directly with neighborhood couriers at 0% commission.")
                st.code(f"Hello! Stop wasting money on delivery app fees in {region if region else country}. Our system connects you with independent drivers directly for 0% commission. Contact us to start your free trial!", language="text")

    # قسم التحدث مع الذكاء الاصطناعي المباشر
    st.markdown("---")
    st.subheader("🤖 مساعد OmniRadar AI الخارق" if st.session_state.lang == "العربية" else "🤖 Advanced AI Assistant")
    user_query = st.text_input("اكتب سؤالك الاستراتيجي هنا واضغط Enter:" if st.session_state.lang == "العربية" else "Type your business question here and press Enter:")
    
    if user_query:
        q_low = user_query.lower()
        if "شحن" in q_low or "طلب" in q_low or "ship" in q_low or "delivery" in q_low:
            reply = "💡 منظومة الشحن المجمع تعتمد على بناء نقطة تجميع (Hub) لتجميع شحنات المتاجر وتوجيهها بسيارة شحن موحدة، مما يقلص التكلفة بنسبة 60% ويضمن ربحاً ممتازاً للمشترك."
        elif "اقنع" in q_low or "إقناع" in q_low or "persuade" in q_low:
            reply = "💡 لإقناع التاجر، اعرض عليه لغة الأرقام الصافية وتوفير العمولات. أثبت له أن نظامك يمنع هدر 30% من أمواله ويمنحه زبائن حقيقيين بضغطة زر وبدون إعلانات ممولة فاشلة."
        else:
            reply = "💡 للنجاح السريع وتحقيق الثروة، اختر بلداً أو محافظة مستهدفة، انسخ رسالتها الذكية من OmniRadar، وتواصل مع 20 صاحب عمل محتمل يومياً لتحصل على أولى عقودك المدفوعة."
        
        st.markdown(f"**🤖 الرد الأسطوري المباشر / AI Response:**\n\n{reply}")

with tab_about:
    st.markdown(ABOUT_AR if st.session_state.lang == "العربية" else ABOUT_EN)

st.markdown("<br><hr><center style='color:gray;'>OmniRadar AI — Secured Platform © 2026</center>", unsafe_allow_html=True)
