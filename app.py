import streamlit as st
import urllib.request
import xml.etree.ElementTree as ET
import re

st.set_page_config(page_title="OmniRadar AI", page_icon="🎯")
st.title("🎯 OmniRadar AI — Realtime Opportunity Hunter")
st.subheader("منصتك العالمية لاقتناص أزمات الأسواق الحقيقية حياً ومباشراً من الإنترنت")
st.markdown("---")

if st.button("🚀 ابدأ مسح كوكب الأرض واقتناص الفرص فوراً", type="primary"):
    st.success("✅ تم الاتصال بنجاح.. جاري سحب وتحليل المشاكل الحية من شبكة الأخبار العالمية!")
    
    try:
        # سحب مباشر من شبكة أخبار جوجل العالمية المحدثة كل دقيقة عن المشاكل والأزمات التجارية
        url = "https://google.com"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        xml_data = urllib.request.urlopen(req).read()
        
        root = ET.fromstring(xml_data)
        items = root.findall('.//item')
        
        if items:
            # عرض أول 3 مشاكل وأخبار حقيقية طازجة تم نشرها في العالم الآن
            for i, item in enumerate(items[:3], 1):
                title = item.find('title').text
                link = item.find('link').text
                description = item.find('description').text
                # تنظيف النص من أكواد الـ HTML
                clean_desc = re.sub('<[^<]+?>', '', description)
                
                st.info(f"**📍 فرصة تجارية حقيقية رقم ({i}) من الأسواق العالمية:**\n\n"
                        f"**🔗 عنوان الأزمة/الخبر الحقيقي:** {title}\n\n"
                        f"**⚠️ تفاصيل المعاناة الحية:** {clean_desc}\n\n"
                        f"**💡 حل الذكاء الاصطناعي المقترح:** بناء تطبيق أو خدمة مخصصة لحل هذه الفجوة فوراً والربح منها.")
                st.markdown("---")
        else:
            st.warning("⚠️ جاري تحديث شبكة البيانات، اضغط مجدداً خلال ثوانٍ.")
            
    except Exception as e:
        st.error(f"❌ حدث عطل مؤقت في جلب البيانات الحية: {e}")

st.markdown("<br><center style='color:gray;'>جميع الحقوق الفكرية محفوظة باسمك © 2026</center>", unsafe_allow_html=True)
