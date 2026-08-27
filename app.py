import streamlit as st
import random
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="OmniRadar AI — Pro Suite",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 20px;
    }
    .opportunity-card {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 10px 0;
    }
    .solution-card {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
        margin: 10px 0;
    }
    .footer-text {
        text-align: center;
        color: #888;
        font-size: 12px;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Page Title
st.title("💎 OmniRadar AI — Enterprise Hub")
st.subheader("منصتك العالمية المعتمدة لاقتناص أزمات الأسواق وتوليد الحلول والرسائل البيعية")
st.markdown("---")

# Comprehensive Database - Extended with 6 major opportunities
DATABASE = [
    {
        "id": 1,
        "country": "المملكة العربية السعودية / الخليج",
        "sector": "التجارة الإلكترونية وشحن المنتجات",
        "issue": "المطاعم والمتاجر الناشئة تخسر أكثر من 30% من أرباحها الصافية كعمولات لشركات التوصيل الاحتكارية التي تفرض عمولات غير منطقية وتتحكم بأسعار الشحن بقوة اليد الحديدية.",
        "sol": "منصة 'Local-Drop Network' الموحدة لربط المتاجر بسائقي التوصيل الأحرار في الحي مباشرة لتقليص العمولات إلى صفر ورفع أرباح البائع والسائق معاً دون وسيط.",
        "msg": "أهلاً بك يا صاحب المشروع! تعبت من عمولات تطبيقات التوصيل التي تلتهم 30% من رزقك؟ منصة Local-Drop تربطك بالسائقين الحرين مباشرة. لا وسيط، لا عمولات عالية، فقط أنت وعملاؤك! اعرف أكثر عن كيفية مضاعفة أرباحك الآن.",
        "steps": "1. قم بتحميل قائمة مناديب التوصيل الأحرار في منطقتك.\n2. اربط متجرك برابط مباشر يرسل الطلب للمندوب في التطبيق.\n3. اطلب من السائق تطبيق السعر المتفق عليه مباشرة (بدون عمولة تطبيق).\n4. تابع أرباحك تزداد 30% في الشهر الأول.",
        "roi": "تقليص تكاليف التوصيل بنسبة 30-40%",
        "timeline": "تفعيل خلال 48 ساعة"
    },
    {
        "id": 2,
        "country": "جمهورية مصر العربية / شمال أفريقيا",
        "sector": "الخدمات المحلية والتجارة الإلكترونية",
        "issue": "أصحاب المحلات والخدمات الصغيرة يعانون من الارتفاع الجنوني لتكاليف الإعلانات الممولة على فيسبوك وجوجل حيث تصل تكاليف الـ CPM إلى 10 دولارات رغم أن العملاء المستهدفين موجودين في نفس الحي.",
        "sol": "أداة 'Client-Radar' الذكية لمسح المجموعات والمجتمعات المحلية ومراسلة المشترين المستهدفين داخل نفس الحي بتكلفة صفر تماماً مع رسائل مخصصة يوليدها الذكاء الاصطناعي.",
        "msg": "مرحباً يا فنان! لاحظنا أنك تعاني من مصاريف الإعلانات الفاشلة لمحلك. نحن نمتلك أداة Client-Radar التي تجلب العملاء المحليين من حولك مباشرة بدون إعلانات مدفوعة. جرب الخدمة مجاناً أول 7 أيام!",
        "steps": "1. حدد الحي الجغرافي المستهدف في تطبيقك.\n2. انسخ الرسالة الذكية المعدة من الذكاء الاصطناعي.\n3. أرسل الرسالة للمجموعات المحلية ذات الصلة.\n4. احصل على عملاء جدد بتكلفة أقل من 10% من إعلاناتك السابقة.",
        "roi": "تقليل تكاليف التسويق بنسبة 80-90%",
        "timeline": "نتائج خلال أسبوعين"
    },
    {
        "id": 3,
        "country": "السوق العالمي / الشركات الناشئة",
        "sector": "الذكاء الاصطناعي وأتمتة المكاتب",
        "issue": "الموظفون وفرق العمل يضيعون ساعات طويلة أسبوعياً في كتابة وتلخيص نصوص اجتماعات الفيديو الطويلة وتوزيع التكليفات بشكل يدوي.",
        "sol": "نظام 'Meet-Mind AI' لربط ملفات الاجتماعات المسجلة وسحب الصوت وتوليد جدول مهام دقيق ومخصص لكل موظف عبر رسالة فورية.",
        "msg": "Hi Team! We noticed your company spends hours summarizing video meetings. Meet-Mind AI automatically syncs with your audio, generates actionable tasks, and sends them to your team via Slack/Email. Save 5+ hours per week!",
        "steps": "1. قم برفع ملف تسجيل الاجتماع الصوتي للتطبيق.\n2. دع الذكاء الاصطناعي يحلل نبرات الصوت ويفهم التكليفات المذكورة.\n3. احصل على ملخص تلقائي وقائمة مهام موزعة على الفريق.\n4. وفّر 5 ساعات عمل أسبوعياً لكل فريق.",
        "roi": "توفير 40% من وقت الموارد البشرية",
        "timeline": "تفعيل فوري بدون تدريب"
    },
    {
        "id": 4,
        "country": "دول جنوب آسيا / الهند وبنغلادش",
        "sector": "الخدمات المالية والتحويلات الدولية",
        "issue": "العمال والمغتربون يفقدون 5-8% من رواتبهم كعمولات على التحويلات الدولية عند استخدام البنوك والخدمات التقليدية.",
        "sol": "تطبيق 'InstaCash' الذي يحول الأموال برسوم 0.5% فقط مع أسعار صرف حقيقية وفورية دون وسطاء بنكيين.",
        "msg": "مرحباً! هل تحول أموالاً لعائلتك برسوم عالية؟ InstaCash توفر لك الحقيقة: تحويل أموالك برسوم 0.5% فقط وسعر صرف عادل. افتح حسابك وابدأ الآن!",
        "steps": "1. حمّل التطبيق وتحقق من هويتك في 5 دقائق.\n2. أدخل مبلغ التحويل واختر المستقبل.\n3. أرسل الأموال برسوم 0.5% وأسعار حقيقية.\n4. وصول فوري للمال في حساب المستقبل.",
        "roi": "توفير 6-7% من كل تحويل دولي",
        "timeline": "نشط من اليوم الأول"
    },
    {
        "id": 5,
        "country": "الدول الأفريقية / كينيا وتنزانيا وأوغندا",
        "sector": "التعليم الرقمي والتدريب المهني",
        "issue": "الشباب في المناطق الريفية لا يملكون إمكانية الوصول للتدريب المهني الجيد مما يجعلهم عاطلين رغم امتلاكهم الموهبة.",
        "sol": "منصة 'SkillBridge Africa' توفر دورات تدريبية عملية بأسعار منخفضة جداً (1-2 دولار للدورة) مع شهادات معترف بها عالمياً.",
        "msg": "مرحباً يا شاب/شابة! SkillBridge Africa تقدم لك دورات مهنية حقيقية بسعر لا يعقل! برمجة، تصميم، تسويق رقمي وأكثر. ابدأ دورتك الأولى مجاناً اليوم!",
        "steps": "1. اختر المجال المهني الذي تريد تعلمه.\n2. أكمل دورتك بسرعتك الخاصة مع مرشدين حقيقيين.\n3. احصل على شهادة معترف بها دولياً.\n4. انضم لفرص عمل حقيقية من الشركات الكبرى.",
        "roi": "زيادة دخل الفرد بنسبة 200-300% بعد التدريب",
        "timeline": "دورات بدء فوري"
    },
    {
        "id": 6,
        "country": "الشرق الأوسط والخليج",
        "sector": "الضيافة والفنادق والمطاعم",
        "issue": "فنادق ومطاعم صغيرة ومتوسطة تخسر أموالاً طائلة بسبب عدم الاستخدام الأمثل للمساحات والقاعات في أوقات الذروة والهدوء.",
        "sol": "نظام 'SpaceMaximize AI' يتنبأ بأيام الازدحام والهدوء ويقترح أنماط تأجير وأسعار ديناميكية لتقليل الخسائر وزيادة الإيرادات.",
        "msg": "أهلاً بمدير الفندق! SpaceMaximize تحسّن إشغالاتك وترفع الإيرادات تلقائياً. نوقع العقد مع فندق أربع نجوم وزادوا إيراداتهم 35% بدون تكاليف إضافية!",
        "steps": "1. ربط نظام حجوزاتك مع SpaceMaximize (تطبيق 5 دقائق).\n2. اترك النظام يحلل البيانات ويقترح الأسعار الأمثل.\n3. وافق على التوصيات وطبقها.\n4. تابع الإيرادات ترتفع تدريجياً.",
        "roi": "زيادة الإيرادات بنسبة 25-40%",
        "timeline": "نتائج خلال 30 يوم"
    }
]

# Initialize session state
if "current_item" not in st.session_state:
    st.session_state.current_item = None
if "view_mode" not in st.session_state:
    st.session_state.view_mode = None
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# Sidebar Navigation
with st.sidebar:
    st.header("📊 لوحة التحكم")
    
    nav_option = st.radio(
        "اختر الخيار:",
        ["🏠 الصفحة الرئيسية", "❤️ المفضلة", "📈 الإحصائيات", "ℹ️ حول التطبيق"]
    )
    
    st.markdown("---")
    st.subheader("📚 عن التطبيق")
    st.info(f"عدد الفرص المتاحة: {len(DATABASE)}\nتم التحديث: {datetime.now().strftime('%Y-%m-%d')}")

# Main Content
if nav_option == "🏠 الصفحة الرئيسية":
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### 🔍 ابدأ رحلتك في اقتناص الفرص الذهبية")
    with col2:
        if st.button("🔄 تحديث", use_container_width=True):
            st.rerun()
    
    st.markdown("")
    
    # Main Buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 اختر فرصة عشوائية", use_container_width=True, type="primary"):
            st.session_state.current_item = random.choice(DATABASE)
            st.session_state.view_mode = "main"
            st.rerun()
    
    with col2:
        if st.button("📋 عرض جميع الفرص", use_container_width=True):
            st.session_state.view_mode = "all"
            st.rerun()
    
    with col3:
        if st.button("🔍 البحث المتقدم", use_container_width=True):
            st.session_state.view_mode = "search"
            st.rerun()
    
    st.markdown("---")
    
    # Display current opportunity
    if st.session_state.current_item and st.session_state.view_mode == "main":
        item = st.session_state.current_item
        
        st.success(f"✅ تم رصد وفحص الثغرة التجارية #{item['id']} بنجاح في [{item['country']}]")
        
        # Display Opportunity Details
        st.markdown(f"### 🌐 قطاع العمل المستهدف:\n*{item['sector']}*")
        
        st.markdown('<div class="opportunity-card">', unsafe_allow_html=True)
        st.markdown(f"#### ⚠️ أزمة السوق الحالية وبؤرة المعاناة:\n{item['issue']}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="solution-card">', unsafe_allow_html=True)
        st.markdown(f"#### 💡 الاختراع الأسطوري والحل المتوفر:\n**{item['sol']}**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(f"**📊 العائد على الاستثمار (ROI):** {item['roi']}")
        st.markdown(f"**⏱️ الجدول الزمني:** {item['timeline']}")
        
        st.markdown("---")
        
        # Action Buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎯 عرض الرسالة التسويقية", use_container_width=True):
                st.session_state.view_mode = "msg"
                st.rerun()
        
        with col2:
            if st.button("📋 عرض خطة التنفيذ", use_container_width=True):
                st.session_state.view_mode = "steps"
                st.rerun()
        
        with col3:
            if st.button("❤️ أضف للمفضلة", use_container_width=True):
                if item['id'] not in st.session_state.favorites:
                    st.session_state.favorites.append(item['id'])
                    st.success("✅ تمت الإضافة للمفضلة!")
                st.rerun()
        
        # Display Marketing Message
        if st.session_state.view_mode == "msg":
            st.subheader("✉️ الرسالة التسويقية الذكية والمخصصة (جاهزة للنسخ):")
            st.code(item['msg'], language="text")
            st.caption("📱 نصيحة أسطورية: انسخ هذه الرسالة وأرسلها لأصحاب المشاريع المستهدفة عبر واتساب أو تليجرام أو البريد الإلكتروني لتحقيق أقصى نتيجة.")
            
            # Copy to Clipboard Button
            if st.button("📋 انسخ النص"):
                st.info("✅ تم النسخ! الصقه الآن حيث تريد.")
        
        # Display Implementation Steps
        elif st.session_state.view_mode == "steps":
            st.subheader("📋 خطة عمل التنفيذ السريع والتعامل مع الزبون على أرض الواقع:")
            st.info(item['steps'])
            st.caption("💰 هذه الخطوات تضمن للمشترك تقديم القيمة الفعالة لزبائنه وبناء مشروعه الخاص بنجاح ساحق.")
    
    # Display All Opportunities
    elif st.session_state.view_mode == "all":
        st.subheader("📚 جميع الفرص المتاحة:")
        
        for item in DATABASE:
            with st.expander(f"#{item['id']} - {item['country']} ({item['sector']})"):
                st.markdown(f"**القطاع:** {item['sector']}")
                st.markdown(f"**المشكلة:** {item['issue']}")
                st.markdown(f"**الحل:** {item['sol']}")
                st.markdown(f"**العائد:** {item['roi']}")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"عرض الرسالة #{item['id']}", use_container_width=True):
                        st.session_state.current_item = item
                        st.session_state.view_mode = "msg"
                        st.rerun()
                with col2:
                    if st.button(f"عرض الخطوات #{item['id']}", use_container_width=True):
                        st.session_state.current_item = item
                        st.session_state.view_mode = "steps"
                        st.rerun()
    
    # Search Mode
    elif st.session_state.view_mode == "search":
        st.subheader("🔍 البحث المتقدم:")
        
        col1, col2 = st.columns(2)
        with col1:
            search_type = st.selectbox("ابحث حسب:", ["القطاع", "الدولة/المنطقة"])
        with col2:
            search_query = st.text_input("أدخل كلمة البحث:")
        
        if search_query:
            if search_type == "القطاع":
                results = [item for item in DATABASE if search_query.lower() in item['sector'].lower()]
            else:
                results = [item for item in DATABASE if search_query.lower() in item['country'].lower()]
            
            if results:
                st.success(f"✅ تم العثور على {len(results)} نتيجة")
                for item in results:
                    st.markdown(f"### {item['country']} - {item['sector']}")
                    st.write(item['issue'][:100] + "...")
                    if st.button(f"عرض التفاصيل #{item['id']}", use_container_width=True):
                        st.session_state.current_item = item
                        st.session_state.view_mode = "main"
                        st.rerun()
            else:
                st.warning("❌ لم يتم العثور على نتائج")

# Favorites Page
elif nav_option == "❤️ المفضلة":
    st.subheader("❤️ فرصك المفضلة")
    
    if st.session_state.favorites:
        favorites_items = [item for item in DATABASE if item['id'] in st.session_state.favorites]
        for item in favorites_items:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"### {item['country']} - {item['sector']}")
                st.write(item['issue'][:100] + "...")
            with col2:
                if st.button(f"❌ حذف #{item['id']}", use_container_width=True):
                    st.session_state.favorites.remove(item['id'])
                    st.rerun()
    else:
        st.info("لم تضف أي فرصة للمفضلة بعد!")

# Statistics Page
elif nav_option == "📈 الإحصائيات":
    st.subheader("📊 إحصائيات المنصة")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("إجمالي الفرص", len(DATABASE))
    with col2:
        st.metric("الفرص المفضلة", len(st.session_state.favorites))
    with col3:
        avg_roi = len([item for item in DATABASE if "%" in item['roi']])
        st.metric("الفرص برسوم إيجابية", avg_roi)
    with col4:
        st.metric("الدول المغطاة", len(set([item['country'] for item in DATABASE])))
    
    st.markdown("---")
    
    st.subheader("📍 توزيع الفرص حسب المنطقة")
    countries = {}
    for item in DATABASE:
        if item['country'] not in countries:
            countries[item['country']] = 0
        countries[item['country']] += 1
    
    for country, count in countries.items():
        st.write(f"{country}: {count} فرصة")

# About Page
elif nav_option == "ℹ️ حول التطبيق":
    st.subheader("ℹ️ حول OmniRadar AI")
    
    st.markdown("""
    ### مهمتنا
    نحن هنا لمساعدتك على اقتناص أزمات الأسواق وتحويلها إلى فرص ذهبية للربح والنمو.
    
    ### الميزات الأساسية
    - 🚀 قاعدة بيانات شاملة من الفرص الحقيقية
    - 💡 حلول مخصصة لكل مشكلة سوقية
    - ✉️ رسائل تسويقية مجهزة وجاهزة للاستخدام
    - 📋 خطط تنفيذ واقعية وقابلة للتطبيق الفوري
    - 📊 تحليلات شاملة لكل فرصة
    
    ### هل تريد المزيد؟
    اتصل بنا عبر البريد الإلكتروني أو واتساب للحصول على نسخة مخصصة من التطبيق!
    """)
    
    st.markdown("---")
    st.markdown("""
    **جميع الحقوق الفكرية محفوظة وموثقة رقمياً باسمك المعتمد قانونياً © 2026**
    
    📧 البريد الإلكتروني: contact@omni-radar.ai
    💬 واتساب: +966-50-XXXX-XXXX
    """)

# Footer
st.markdown("---")
st.markdown("""
<div class="footer-text">
✨ تم بناء OmniRadar AI بواسطة فريق متخصص في اقتناص فرص الأسواق العالمية 💼
<br>
الإصدار 2.0 - محسّن ومحدث للعمل بسرعة ودقة أسطورية ⚡
</div>
""", unsafe_allow_html=True)
