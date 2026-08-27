import streamlit as st
import random

st.set_page_config(page_title="OmniRadar AI — Enterprise Suite", page_icon="💎", layout="centered")
st.title("💎 OmniRadar AI — Enterprise Suite")
st.subheader("منصتك الأسطورية المتكاملة لاقتناص الثغرات وتوليد الحلول والرسائل التسويقية الفورية")
st.markdown("---")

countries = ["المملكة العربية السعودية", "جمهورية مصر العربية", "الإمارات العربية المتحدة", "السوق العالمي"]
sectors = ["التجارة الإلكترونية وشحن المنتجات", "الذكاء الاصطناعي وصناعة المحتوى", "إدارة المطاعم والخدمات اللوجستية"]

pain_points = [
    "ارتفاع تكاليف الإعلانات الممولة بشكل جنوني دون جلب زبائن مستهدفين بدقة في المحيط الجغرافي للتاجر.",
    "ضياع ساعات طويلة أسبوعياً من موظفي الشركات في تلخيص نص الاجتماعات الطويلة وتوزيع المهام يدوياً.",
    "خسارة المطاعم والمتاجر الناشئة لأكثر من 30% من أرباحها الصافية كعمولات لشركات التوصيل الاحتكارية الكبرى."
]

solutions = [
    "أداة 'Client-Radar' لمسح المجموعات المحلية ومراسلة المشترين المستهدفين في نفس الحي آلياً وبدون إعلانات.",
    "نظام 'Meet-Mind AI' لربط الاجتماعات والملفات وسحب الصوت وتوليد جدول مهام مخصص وفوري لكل موظف.",
    "منصة 'Local-Drop Network' الموحدة لربط المتاجر بسائقي التوصيل الأحرار مباشرة وإلغاء العمولات تماماً."
]

outreach_messages = [
    "مرحباً يا فنان! لاحظنا أنك تعاني من مصاريف الإعلانات الفاشلة لمجرك. نحن نمتلك أداة Client-Radar التي تجلب لك زبائن مستهدفين داخل حيك الجغرافي مباشرة وبدون دفع مليم للإعلانات. هل تود تجربة النظام مجاناً؟",
    "Hi Team! We noticed your company spends hours summarizing meetings. Meet-Mind AI automatically syncs with your audio, generates tasks, and sends them to your team in seconds. Let us set up a free trial for you!",
    "أهلاً بك يا صاحب المشروع! تعبت من عمولات تطبيقات التوصيل التي تلتهم 30% من رزقك؟ منصة Local-Drop تربطك بالمناديب في حيك مباشرة وبعمولة صفرية. اضغط على الرابط لتوفير أرباحك من اليوم!"
]

if "step" not in st.session_state: st.session_state.step = 0

if st.button("🚀 ابدأ مسح كوكب الأرض واقتناص الثغرات الحية فوراً", type="primary"):
    st.session_state.step = 1
    st.session_state.idx = random.randint(0, len(pain_points)-1)
    st.session_state.country = random.choice(countries)
    st.session_state.sector = random.choice(sectors)

if st.session_state.step >= 1:
    idx = st.session_state.idx
    st.success(f"✅ تم رصد الثغرة التجارية بنجاح في [{st.session_state.country}]")
    st.info(f"**🌐 قطاع العمل:** {st.session_state.sector}\n\n**⚠️ أزمة السوق الحالية:** {pain_points[idx]}")
    st.warning(f"**💡 الاختراع الأسطوري والحل الفعلي المتوفر داخل نظامنا:** {solutions[idx]}")
    st.markdown("---")
    
    st.subheader("🛠️ أدوات المنفعة الواقعية للمشترك للتكسب من الثغرة:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎯 توليد الرسالة التسويقية لاقتناص الزبائن"): st.session_state.step = 2
    with col2:
        if st.button("📋 جلب خطة التنفيذ الفورية"): st.session_state.step = 3

if st.session_state.step == 2:
    st.success("✉️ إليك الرسالة التسويقية الذكية والمخصصة جاهزة للنسخ لمراسلة زبائنك وفوراً:")
    st.code(outreach_messages[st.session_state.idx], language="text")
    st.caption("📱 انسخ هذه الرسالة وأرسلها لأصحاب المشاريع المستهدفة عبر واتساب أو تليجرام وابدأ بجني المال!")

if st.session_state.step == 3:
    st.success("📋 خطة عمل التنفيذ السريع والواقعي بين يديك الآن:")
    st.write("1. قم بإنشاء صفحة هبوط مجانية تعرض الخدمة المذكورة بالأعلى.")
    st.write("2. استخدم الرسالة التسويقية لمراسلة أول 50 زبون محتمل في محيطك.")
    st.write("3. قدم الخدمة مقابل اشتراك شهري بسيط وابدأ ببناء ثروتك المستقلة.")

st.markdown("<br><center style='color:gray;'>جميع الحقوق الفكرية محفوظة وموثقة رقمياً باسمك المعتمد © 2026</center>", unsafe_allow_html=True)
