import streamlit as st
import random
import time

# إعدادات الواجهة الأساسية والوضع الليلي المدمج
st.set_page_config(page_title="OmniRadar AI — Pro Global", page_icon="🌍", layout="centered")

# نظام إدارة اللغات والترجمة الشاملة (عربي / إنجليزي)
if "lang" not in st.session_state: st.session_state.lang = "العربية"
if "logged_in" not in st.session_state: st.session_state.logged_in = False

# قائمة التبديل بين اللغات في أعلى الشاشة مباشرة لسهولة الوصول للمتعلم وغير المتعلم
col_l, col_r = st.columns([8, 2])
with col_r:
    lang_choice = st.selectbox("🌐 Language", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)
    st.session_state.lang = lang_choice

# نصوص الواجهة باللغتين
TEXTS = {
    "العربية": {
        "title": "🌍 منصة OmniRadar AI العالمية", "subtitle": "النظام الأسطوري الشامل لاقتناص ثغرات الأسواق وإدارة حلول الابتكار",
        "login_title": "🔐 بوابة الأمان والدخول للمشتركين", "pass_label": "أدخل كلمة مرور التفعيل الشخصية:", "login_btn": "تأكيد الدخول والتفعيل",
        "wrong_pass": "❌ كلمة المرور غير صحيحة، يرجى التواصل مع الإدارة لتفعيل حسابك.", "logout_btn": "🔒 تسجيل الخروج",
        "sidebar_head": "🗺️ الرادار الجغرافي الدولي", "select_country": "اختر الدولة أو القارة المستهدفة:",
        "region_label": "اكتب اسم المحافظة / المدينة / القرية المستهدفة:", "region_placeholder": "مثال: أسيوط، السالمية، Ontario، الدلتا...",
        "scan_btn": "🚀 ابدأ محرك التنبؤ واقتناص الثغرات فوراً", "scanning": "🧠 جاري تشغيل عقل الذكاء الاصطناعي وفحص السجلات...",
        "scan_success": "✅ تم الفحص التنبؤي الجغرافي بنجاح! إليك الفجوة الحية المكتشفة:",
        "sector_lbl": "🌐 قطاع وفئة العمل المستهدفة:", "issue_lbl": "⚠️ ثغرة وأزمة السوق الحالية وبؤرة المعاناة:",
        "sol_lbl": "💡 الاختراع الأسطوري والحل الفعلي الممنوح داخل نظامنا:",
        "tool_lbl": "🛠️ أدوات المنفعة الواقعية والتنفيذ الفوري للمشترك لحصد المال:",
        "msg_btn": "🎯 توليد الرسالة التسويقية لاقتناص الزبائن", "steps_btn": "📋 جلب خطة التنفيذ والتعامل الواقعي",
        "msg_title": "✉️ الرسالة التسويقية الذكية والمخصصة (جاهزة للنسخ):", "msg_tip": "📱 انسخ هذه الرسالة وأرسلها لأصحاب المشاريع المحتملين فوراً للتكسب!",
        "steps_title": "📋 خطة عمل التنفيذ السريع والتعامل الميداني المربح مع الزبون:",
        "chat_title": "🤖 مساعد OmniRadar AI الخارق للاستشارات والبيع العكسي", "chat_placeholder": "اكتب سؤالك الاستراتيجي هنا واضغط Enter (مثال: كيف أقنع زبون؟)...",
        "chat_wait": "🧠 جاري تحليل السؤال وصياغة الحل الواقعي المباشر...", "chat_user": "👤 سؤالك:", "chat_bot": "🤖 الرد الأسطوري المباشر:",
        "about_tab": "ℹ️ حول التطبيق والمالك", "about_content": """
        ### 👑 ملكية الحقوق الفكرية والإنتاج:
        هذه الشركة والمنصة العالمية بكامل شفراتها البرمجية واختراعاتها المدمجة هي من **تصميم وإنتاج وملك المبتكر ورائد الأعمال**:
        **حسام حسين أحمد توفيق** (Houssam Hussein Ahmed Taufiq).
        
        ### 📱 أرقام التواصل والدعم الفني المعتمدة:
        رقم الهاتف المعتمد والوحيد للتواصل المباشر، خدمات **واتس آب (WhatsApp)**، والتحويلات المالية عبر **إنستا باي (InstaPay)**:
        **01015059150** (من خارج مصر: +201015059150)
        
        *جميع الحقوق الفكرية وبراءات الاختراع الرقمية مسجلة وموثقة دولياً لعام 2026 باسم المالك المذكور أعلاه ويحظر نسخها.*
        """
    },
    "English": {
        "title": "🌍 OmniRadar AI — Global Platform", "subtitle": "The Ultimate System for Market Gap Detection & Innovation Management",
        "login_title": "🔐 Secure Enterprise Login Gateway", "pass_label": "Enter your personal activation password:", "login_btn": "Verify & Unlock Platform",
        "wrong_pass": "❌ Invalid password. Please contact administration to activate your account.", "logout_btn": "🔒 Secure Logout",
        "sidebar_head": "🗺️ Global Geographic Filter", "select_country": "Select Target Country/Continent:",
        "region_label": "Type Target Province / City / Village:", "region_placeholder": "e.g., Cairo, Ontario, Salmiya, London...",
        "scan_btn": "🚀 Launch Predictive Market Scanner", "scanning": "🧠 AI Core is scanning international market registries...",
        "scan_success": "✅ Geographic scan successful! Live market gap detected:",
        "sector_lbl": "🌐 Target Industrial Sector:", "issue_lbl": "⚠️ Current Market Crisis & Pain Point:",
        "sol_lbl": "💡 Suggested AI Solution & Tool Provided Within Our System:",
        "tool_lbl": "🛠️ Practical Monetization Tools & Action Plans for Subscribers:",
        "msg_btn": "🎯 Generate Client Outreach Message", "steps_btn": "📋 Fetch Practical Implementation Strategy",
        "msg_title": "✉️ Smart & Tailored Marketing Message (Ready to Copy):", "msg_tip": "📱 Copy this text and send it directly to potential clients to secure deals!",
        "steps_title": "📋 Field Action Plan & Practical Client Management Strategy:",
        "chat_title": "🤖 OmniRadar AI — Advanced Query & Business Assistant", "chat_placeholder": "Type your strategic business question here and press Enter...",
        "chat_wait": "🧠 Analyzing question and generating professional action steps...", "chat_user": "👤 Your Query:", "chat_bot": "🤖 Strategic Response:",
        "about_tab": "ℹ️ About App & Owner", "about_content": """
        ### 👑 Intellectual Property & Ownership:
        This global enterprise suite and all its built-in digital innovations are **Designed, Developed, and Owned Solely** by the inventor and entrepreneur:
        **Houssam Hussein Ahmed Taufiq** (حسام حسين أحمد توفيق).
        
        ### 📱 Authorized Contact & Support Channels:
        The single authorized phone number for official inquiries, **WhatsApp**, and financial settlement via **InstaPay**:
        **01015059150** (International: +201015059150)
        
        *All digital patents and global intellectual property are securely code-stamped for 2026 under the name of the owner above.*
        """
    }
}

T = TEXTS[st.session_state.lang]

# 1. نظام بوابة الأمان لمنع الاستغلال (بوابة الدفع والتفعيل بكلمة مرور)
# كلمة المرور الافتراضية للتطبيق هي: 1234 (يمكنك تغييرها لأي كلمة تريدها)
if not st.session_state.logged_in:
    st.markdown(f"### {T['login_title']}")
    password = st.text_input(T['pass_label'], type="password")
    if st.button(T['login_btn'], type="primary"):
        if password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error(T['wrong_pass'])
    st.markdown("---")
    # عرض التوثيق الفكري أسفل صفحة الدخول لحمايتك قبل تفعيل الحساب
    st.markdown(T['about_content'])
    st.stop()

# في حالة الدخول بنجاح، يتم تفعيل لوحة التحكم الكاملة
st.sidebar.button(T['logout_btn'], on_click=lambda: st.session_state.__setitem__("logged_in", False))

# إنشاء الأقسام وعلامات التبويب الكبرى (لوحة التحكم الرئيسية + قسم حول التطبيق المطور على جنب)
tab_main, tab_about = st.tabs(["🚀 Dashboard", f"{T['about_tab']}"])

with tab_main:
    # الشباك الجانبي الذكي لتغطية جميع دول العالم
    st.sidebar.header(T['sidebar_head'])
    global_countries = [
        "جمهورية مصر العربية (All Provinces)", "دولة الكويت (All Regions)", "المملكة العربية السعودية", 
        "الإمارات العربية المتحدة", "Canada & USA", "European Union", "United Kingdom", "Asia & Australia"
    ]
    country_selected = st.sidebar.selectbox(T['select_country'], global_countries)
    region_typed = st.sidebar.text_input(T['region_label'], placeholder=T['region_placeholder'])

    # محرك الأزمات الداخلي التنبؤي
    DATA_POOL = [
        {
            "sector_ar": "إدارة المطاعم والخدمات اللوجستية وتوصيل الطلبات", "sector_en": "Logistics & Food Delivery Management",
            "issue_ar": "تتكبد المطاعم والمتاجر الناشئة خسائر تلتهم 30% من صافي أرباحها اليومية كعمولات إجبارية لصالح تطبيقات التوصيل الاحتكارية الكبرى.",
            "issue_en": "Small restaurants are losing up to 30% of their net margins due to high commissions enforced by monopoly delivery platforms.",
            "sol_ar": "منصة 'Local-Drop Network' الموحدة لربط المتاجر بسائقي التوصيل المستقلين في الحي مباشرة لتقليص العمولات إلى صفر وبدء التوصيل بأسعار عادلة للطرفين.",
            "sol_en": "Deploying 'Local-Drop Network' to connect stores directly with neighborhood couriers, slashing platform commissions to 0%.",
            "msg_ar": "أهلاً بك يا صاحب المشروع! تعبت من عمولات تطبيقات التوصيل التي تلتهم 30% من رزقك؟ منصة Local-Drop تربطك بالمناديب في حيك مباشرة وبعمولة صفرية. تواصل معنا لتوفير أرباحك وتأمين عملائك من اليوم!",
            "msg_en": "Hi Owner! Tired of delivery apps taking 30% of your hard-earned revenue? Local-Drop connects you directly with independent drivers for 0% commission. Contact us to deploy your automated hub today!",
            "steps_ar": "1. انسخ الرسالة التسويقية الذكية المخصصة بالأعلى.\n2. أرسلها إلى 20 مطجر أو مطعم في منطقتك الجغرافية وعارض عليهم الخدمة.\n3. خذ منهم اشتراك شهري ثابت ومخفض ووفر لهم آلاف الدنانير/الجنيهات وابدأ في جني المال.",
            "steps_en": "1. Copy the generated outreach message.\n2. Contact local business owners via WhatsApp or email.\n3. Offer them the zero-commission direct setup for a flat monthly subscription fee."
        },
        {
            "sector_ar": "التجارة الإلكترونية والتسويق الرقمي للمحلات التجارية", "sector_en": "E-Commerce & Hyper-Local Digital Marketing",
            "issue_ar": "أصحاب المحلات التجارية والخدمات الصغيرة يعانون من الارتفاع الجنوني لتكاليف الإعلانات الممولة على منصات التواصل الاجتماعي دون جلب زبائن حقيقيين في محيطهم الجغرافي المباشر.",
            "issue_en": "Local shop owners face extreme customer acquisition costs on social media ads without targeting immediate paying clients in their vicinity.",
            "sol_ar": "أداة 'Client-Radar' الذكية لمسح المجموعات والمجتمعات المحلية ومراسلة المشترين المستهدفين داخل نفس المنطقة آلياً وبدون دفع مليم واحد للإعلانات الفاشلة.",
            "sol_en": "Using 'Client-Radar' software core to scan regional groups, filtering prospective local buyers and automating targeted direct message responses.",
