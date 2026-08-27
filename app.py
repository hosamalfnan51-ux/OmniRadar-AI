import streamlit as st
import json
import os

st.set_page_config(page_title="OmniRadar AI", page_icon="🎯", layout="centered")
st.title("🎯 OmniRadar AI — Global Live Solution Hub")
st.subheader("منصتك العالمية المعتمدة لاقتناص أزمات الأسواق وابتكار الحلول التجارية حياً ومباشراً")
st.markdown("---")

if st.button("🚀 ابدأ مسح كوكب الأرض واقتناص الفرص فوراً", type="primary"):
    st.success("✅ تم تفعيل عقل الذكاء الاصطناعي وجاري سحب وتحليل المشاكل الحية من مخزن البيانات العالمي!")
    
    file_path = "world_problems.json"
    
    try:
        # التأكد من وجود ملف البيانات وقراءته تلقائياً
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                problems_data = json.load(f)
            
            if problems_data:
                for i, item in enumerate(problems_data, 1):
                    st.info(f"**📍 فرصة تجارية عالمية حقيقية رقم ({i}) [تحديث حي]:**\n\n"
                            f"**🌐 قطاع وفئة العمل:** {item.get('tech', 'Global Tech')}\n\n"
                            f"**⚠️ أزمة السوق الحية المرصودة:** {item.get('desc', 'N/A')}\n\n"
                            f"**💡 الاختراع الأسطوري والحل المقترح:** {item.get('sol', 'N/A')}")
                    st.markdown("---")
            else:
                st.warning("⚠️ مخزن البيانات قيد التحديث الآلي حالياً، يرجى المحاولة بعد قليل.")
        else:
            st.error("❌ ملف البيانات الرئيسي غير موجود، جاري بناؤه تلقائياً بواسطة الروبوت الخفي.")
            
    except Exception as e:
        st.error(f"❌ حدث خطأ أثناء قراءة البيانات المتجددة: {e}")

st.markdown("<br><center style='color:gray;'>جميع الحقوق الفكرية محفوظة باسمك وموثقة رقمياً © 2026</center>", unsafe_allow_html=True)
