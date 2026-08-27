import streamlit as st
from duckduckgo_search import DDGS
st.set_page_config(page_title="OmniRadar AI", page_icon="🎯")
st.title("🎯 OmniRadar AI — Live Version")
st.subheader("منصتك الأسطورية العالمية لاقتناص الزبائن والمشاكل الحقيقية حياً من الإنترنت")
st.markdown("---")
if st.button("🚀 ابدأ مسح كوكب الأرض واقتناص الفرص فوراً", type="primary"):
    st.success("✅ تم الاتصال بالإنترنت وجاري سحب المشاكل الحية الآن...")
    try:
        with DDGS() as ddgs:
            res = list(ddgs.text('site:reddit.com "need an app for" OR "تعبت من مشكلة"', max_results=3))
        if res:
            for i, r in enumerate(res, 1):
                st.info(f"**📍 فرصة حقيقية رقم ({i}):**\n\n**🔗 المصدر:** {r['title']}\n\n**⚠️ نص الشكوى الحية:** {r['body']}")
                st.markdown("---")
        else: st.warning("⚠️ لم يتم العثور على فرص جديدة في هذه الثواني، اضغط مجدداً لمسح أعمق.")
    except Exception as e: st.error(f"تحديث مؤقت في الخادم، اعد المحاولة: {e}")
st.markdown("<br><center style='color:gray;'>جميع الحقوق الفكرية محفوظة باسمك © 2026</center>", unsafe_allow_html=True)
