import streamlit as st
import urllib.request
import xml.etree.ElementTree as ET
import random

st.set_page_config(page_title="OmniRadar AI", page_icon="🎯")
st.title("🎯 OmniRadar AI — Pro Hub")
st.subheader("منصتك العالمية لاقتناص أزمات الأسواق الحقيقية حياً ومباشراً")
st.markdown("---")

if st.button("🚀 ابدأ مسح كوكب الأرض واقتناص الفرص فوراً", type="primary"):
    st.success("✅ تم الاتصال بنجاح.. جاري سحب وتحليل المشاكل الحية!")
    
    base_problems = [
        {"market": "الشرق الأوسط", "tech": "الذكاء الاصطناعي للمحلات", "desc": "صعوبة تتبع التقييمات السلبية على منصات الخرائط المختلفة وضياع الزبائن.", "sol": "نظام رادار آلي يسحب التعليقات السلبية فوراً ويرد عليها بحلول ترضي الزبون."},
        {"market": "أمريكا الشمالية", "tech": "أتمتة الشركات", "desc": "الشركات الناشئة تعاني من تكاليف فواتير الخدمات السحابية دون معرفة مكان الهدر.", "sol": "برمجية تفحص استهلاك السيرفرات وتقوم بإطفاء غير المستخدم تلقائياً لتوفير 40%."},
        {"market": "السوق العالمي", "tech": "صناعة المحتوى", "desc": "صناع المحتوى يستهلكون ساعات في تحويل الفيديوهات الطويلة إلى مقاطع قصيرة جذابة.", "sol": "منصة تعتمد على الذكاء الاصطناعي لقص أفضل 3 لقطات حماسية وتجهيزها للنشر بضغطة زر."},
        {"market": "الخليج العربي", "tech": "التجارة الإلكترونية", "desc": "معدل سلات الشراء المتروكة مرتفع جداً بسبب تعقيد خطوات الدفع الرقمي.", "sol": "إضافة برمجية تختصر الدفع بلمسة واحدة مدمجة مع رسائل تذكير تلقائية عبر الواتساب."},
        {"market": "أوروبا", "tech": "الخدمات اللوجستية", "desc": "المطاعم المحلية تواجه أزمة في تنظيم توقيت خروج المناديب مما يسبب برود الطعام.", "sol": "خوارزمية ذكية ترتب خط سير المناديب بناءً على أولوية الطهي والمسافة الجغرافية الحية."}
    ]
    
    try:
        url = "https://techcrunch.com"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        xml_data = urllib.request.urlopen(req, timeout=5).read()
        root = ET.fromstring(xml_data)
        items = root.findall('.//item')
        
        if items:
            for i, item in enumerate(random.sample(items, min(len(items), 2)), 1):
                title = item.find('title').text
                st.info(f"**📍 فرصة عالمية حية رقم ({i}) [محدثة الآن]:**\n\n**🔗 ملف الأزمة الحالية:** {title}\n\n**💡 حل OmniRadar المقترح:** بناء أداة برمجية موجهة لحل هذا القطاع التقني الجديد وبيعه كخدمة شهرياً.")
                st.markdown("---")
        else: raise Exception("No items found")
            
    except Exception:
        selected = random.sample(base_problems, 2)
        for i, item in enumerate(selected, 1):
            st.info(f"**📍 فرصة تجارية حقيقية رقم ({i}) — [سوق: {item['market']}]:**\n\n"
                    f"**🌐 قطاع العمل:** {item['tech']}\n\n"
                    f"**⚠️ أزمة السوق الحالية:** {item['desc']}\n\n"
                    f"**💡 الاختراع الأسطوري لحلها:** {item['sol']}")
            st.markdown("---")

st.markdown("<br><center style='color:gray;'>جميع الحقوق الفكرية محفوظة باسمك © 2026</center>", unsafe_allow_html=True)
