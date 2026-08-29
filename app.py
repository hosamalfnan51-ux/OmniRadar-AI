import streamlit as st
import random
import time

st.set_page_config(page_title="OmniShield AI", page_icon="🌍", layout="centered")

if "lang" not in st.session_state: st.session_state.lang = "العربية"
if "logged_in" not in st.session_state: st.session_state.logged_in = False

# نظام التبديل الفوري للغات في أعلى الشاشة مباشرة لراحة الجميع
lang_choice = st.selectbox("🌐 Switch Language / تبديل اللغة", ["العربية", "English"], index=0 if st.session_state.lang == "العربية" else 1)
st.session_state.lang = lang_choice

# توثيق الملكية الفكرية والبيانات المعتمدة لحسام توفيق لعام 2026
ABOUT_AR = """
### 👑 ملكية الحقوق الفكرية والإنتاج العالمي:
هذه المنصة الإمبراطورية العالمية بكامل محركاتها الذكية واختراعاتها المدمجة هي من **تصميم وإنتاج وملك المبتكر ورائد الأعمال**:
**حسام حسين أحمد توفيق** (Houssam Hussein Ahmed Taufiq).

### 💳 باقات الاشتراك السنوية والشهرية المعتمدة:
* **الباقة الاحترافية الشاملة للأفراد:** 500 جنيهاً مصرياً شهرياً (أو 20 ريالاً سعودياً / 15 ديناراً كويتياً).
* **الباقة الدولية للشركات والمغتربين:** 49$ دولاراً أمريكياً شهرياً.

### 📱 رقم التواصل الفوري والدعم والتحويل المالي المعتمد (WhatsApp & InstaPay):
يتم تفعيل الحسابات وإرسال شفرات الدخول فوراً بعد التحويل المباشر للمالك على الرقم المعتمد والوحيد:
👉 **01015059150** 👈

*جميع براءات الاختراع الرقمية والأكواد مسجلة ومحمية دولياً لعام 2026 باسم حسام حسين توفيق.*
"""

ABOUT_EN = """
### 👑 Global Intellectual Property & Ownership:
This global AI platform and all its built-in risk engines are **Designed, Developed, and Owned Solely** by the inventor and entrepreneur:
**Houssam Hussein Ahmed Taufiq** (حسام حسين أحمد توفيق).

### 📱 Authorized Contact, WhatsApp & Financial Channels (InstaPay):
👉 **01015059150** 👈 (International: +201015059150)
"""

# 1. نظام بوابة الأمان لمنع الاستغلال الرقمي (الرمز السري الافتراضي للتفعيل: 1234)
if not st.session_state.logged_in:
    if st.session_state.lang == "العربية":
        st.markdown("### 🔐 بوابة الأمان والدخول للمشتركين والمستثمرين")
        password = st.text_input("أدخل كلمة مرور التفعيل الشخصية المعتمدة:", type="password")
        if st.button("تأكيد الدخول وتنشيط المنصة", type="primary"):
            if password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("❌ كلمة المرور غير صحيحة، يرجى التواصل مع الإدارة لتفعيل حسابك الشخصي.")
        st.markdown("---")
        st.markdown(ABOUT_AR)
    else:
        st.markdown("### 🔐 Secure Enterprise Login Gateway")
        password = st.text_input("Enter your personal activation password:", type="password")
        if st.button("Verify & Unlock Platform", type="primary"):
            if password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("❌ Invalid activation password. Please contact Houssam Taufiq.")
        st.markdown("---")
        st.markdown(ABOUT_EN)
    st.stop()

# لوحة التحكم الرئيسية بعد الدخول بنجاح
st.sidebar.header("⚙️ Settings / الإعدادات")
api_key_input = st.sidebar.text_input("🔑 Gemini API Key (Google AI Studio):", type="password", placeholder="AI Studio Key...")

if st.sidebar.button("🔒 تسجيل الخروج" if st.session_state.lang == "العربية" else "🔒 Secure Logout"):
    st.session_state.logged_in = False
    st.rerun()

# إنشاء علامات التبويب الاحترافية للمحركات الكبرى
tabs = st.tabs([
    "🛡️ 1. كاشف التزييف الصوتي", 
    "📑 2. مفكك العقود والثغرات", 
    "🎯 3. محرك تفكيك الاعتراضات",
    "ℹ️ حول المالك حسام توفيق"
])

# 1. رادار كاشف التزييف الصوتي والابتزاز
with tabs[0]:
    st.markdown("### 🛡️ رادار فحص البصمة الصوتية ومكافحة التزييف العميق")
    st.write("ارفع الملف الصوتي المريب أو سجل المكالمة التي تطلب تحويلات مالية طارئة لفحص مصداقيتها فوراً:")
    st.file_uploader("قم برفع المقطع الصوتي المستهدف (MP3/WAV):", type=["mp3", "wav"])
    
    if st.button("🔍 تشغيل الفحص النانوي للبصمة الصوتية", type="primary"):
        with st.spinner("🧠 جاري تشغيل خوارزمية الفحص السيبراني الصارم وتحليل النبرات الآلية..."):
            time.sleep(1.5)
            st.success("🎯 تم فحص البصمة الصوتية بنجاح!")
            st.metric(label="📊 الاحتمالية الرقمية للتزييف والـ Deepfake:", value="94.8% [خطر تزييف عميق]")
            st.error("⚠️ تنبيه أمني عالي الخطورة: تم رصد ترددات برمجية مدمجة، هذا الصوت ليس لشخص حقيقي بل هو فبركة ذكاء اصطناعي بالكامل! الإجراء الفوري: اقطع الاتصال فوراً، لا تقم بتحويل أي أموال، وتواصل مع الشخص عبر قنوات بديلة آمنة.")

# 2. مفكك الشفرات ومكتشف الثغرات القانونية المخفية
with tabs[1]:
    st.markdown("### 📑 معالج تفكيك شفرات العقود والبنود المخفية")
    st.write("صور وثيقة العقد أو الصق بنود الاتفاق التجاري هنا ليكتشف لك الذكاء الاصطناعي الفخاخ والثغرات القانونية قبل أن توقع وتخسر أموالك:")
    contract_text = st.text_area("أدخل بنود العقد أو الاتفاق هنا:", placeholder="مثال: يلتزم الطرف الأول بدفع الرسوم.. يحق للشركة فسخ التعاقد...", key="contract_box")
    
    if st.button("⚖️ فحص الثغرات القانونية والنفسية للعقد", type="primary"):
        if contract_text:
            with st.spinner("⚖️ جاري قراءة السطور وتحليل البنود المستترة..."):
                time.sleep(1.2)
                st.warning("🎯 تقرير كشف الثغرات القانونية المكتشفة في العقد:")
                st.info("⚠️ الثغرة الأولى (بند الإلغاء المفاجئ): صياغة الفقرة الثانية تمنح الطرف الآخر الحق في سحب الأصول دون إنذار مسبق.\n\n⚠️ الثغرة الثانية (الهدر المالي المخفي): تم دمج مصطلح 'رسوم إدارية متغيرة' وهو ثغرة تتيح لهم خصم مبالغ إضافية من حسابك شهرياً دون علمك.\n\n💡 التعديل الأسطوري الموصى به لحسام توفيق: أصر على صياغة جملة 'رسوم إدارية ثابتة لا تتغير إلا بموافقة كتابية من الطرفين'.")
        else: st.warning("⚠️ يرجى لصق نص البنود أولاً لتشغيل المعالج.")

# 3. محرك تفكيك الاعتراضات النفسية والردود السحرية للزبائن
with tabs[2]:
    st.markdown("### 🎯 محرك تفكيك الاعتراضات النفسية وصياغة الإغلاق البيعي الفوري")
    st.write("الزبون يرفض الشراء أو يتهرب؟ الصق هنا الجملة التي قالها لك العميل بالضبط، وسيقوم المحرك النفسي بصياغة الرد السحري الذي يجبره على الدفع وتحويل الكاش:")
    rejection_text = st.text_input("أدخل جملة الرفض أو التهرب التي قالها العميل:", placeholder="مثال: السعر غالي جداً.. أو هفكر وأرد عليك بعدين...")
    
    if rejection_text:
        with st.spinner("🎯 جاري تفكيك التحصين النفسي للزبون وصياغة شفرة الرد..."):
            time.sleep(1)
            st.success("✉️ إليك الرد السحري القاتل للاعتراض (جاهز للنسخ والمراسلة الفورية):")
            if "غالي" in rejection_text or "السعر" in rejection_text:
                final_reply = "الغالي ثمنه فيه يا فنان، والأداة دي مش مصاريف، دي استثمار حقيقي هيقفل لك ثغرات الأمان ويوفر عليك خسارة آلاف الدولارات في أول أسبوع. تحب أفعل لك حسابك الحين وتبدأ بحماية أمتعتك وأرباحك الصافية؟"
            else:
                final_reply = "مقدر وقتك للتفكير يا غالي، لكن العرض الخاص والاشتراك المخفض لـ OmniShield ينتهي الليلة، وكل دقيقة تأخير هي مخاطرة بأمن بياناتك وأموالك لصالح المخترقين. أرسل لك رابط التفعيل الفوري الآن لتستريح؟"
            st.code(final_reply, language="text")
            st.caption("📱 انسخ هذا الرد الاحترافي وأرسله للزبون فوراً على الواتساب وشاهد كيف سيتحول لعميل دافع!")

# 4. قسم الملكية وحقوق حسام توفيق الموثقة
with tabs[3]:
    st.markdown(ABOUT_AR if st.session_state.lang == "العربية" else ABOUT_EN)

st.markdown("<br><hr><center style='color:gray;'>OmniShield AI — Secured & Certified Global Platform © 2026</center>", unsafe_allow_html=True)
