import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import re
from io import BytesIO

# --- DEFAULT STOPWORDS ---
DEFAULT_STOPWORDS = {
    "bir", "ve", "bu", "şu", "o", "da", "de", "mi", "ki", "ile", "gibi", "ya", "ne", "için",
    "kadar", "ancak", "hatta", "hem", "ise", "yani", "ama", "veya", "diye", "sadece", "çok",
    "az", "daha", "en", "yine", "hep", "üzerine", "sonra", "olan", "birçok", "birkaç",
    "aslında", "elbette", "belki", "bile", "fakat", "çünkü", "çoğu", "bazı", "bazen",
    "bazılarını", "bazısı", "bazıları", "about", "or", "have", "is", "no", "has", "on", "more", "to",
    "at", "from", "this", "make", "which", "you", "not", "can", "of", "an", "it", "and", "all", "for",
    "we", "will", "so", "that", "but", "like", "are", "if", "they", "in", "with", "what", "as",
    *[str(i) for i in range(0, 10)],
    *list("abcçdefgğhıijklmnoöprsştuüvyzqwxyz")
}

st.set_page_config(layout="wide")
st.title("🔠 Word Cloud ve Analiz Uygulaması")

# Sidebar
st.sidebar.header("📁 Dosya Yükle ve Analiz Seçenekleri")
uploaded_file = st.sidebar.file_uploader("Excel dosyası yükleyin (.xlsx)", type=["xlsx"])

# ANALİZ SEÇİMLERİ (HEATMAP KALDIRILDI)
st.sidebar.subheader("📊 Analizler")
analizler = {
    "Bar Chart (Kelime Frekansı)": False,
    "Bubble Chart": False
}
if "selected_analyses" not in st.session_state:
    st.session_state.selected_analyses = analizler.copy()

for key in analizler.keys():
    st.session_state.selected_analyses[key] = st.sidebar.checkbox(
        key, value=st.session_state.selected_analyses.get(key, False)
    )

# STOPWORD YÖNETİMİ
st.sidebar.subheader("🚫 Stopword Yönetimi")
if "stopwords" not in st.session_state:
    st.session_state.stopwords = DEFAULT_STOPWORDS.copy()

new_stop = st.sidebar.text_input("Yeni stopword ekle")
if st.sidebar.button("Ekle") and new_stop:
    st.session_state.stopwords.add(new_stop.lower())
    st.sidebar.info("Stopword eklendi. Lütfen sayfayı yenileyin.")

st.sidebar.markdown("### Mevcut Stopwordler")
for word in sorted(st.session_state.stopwords):
    col1, col2 = st.sidebar.columns([8, 1])
    col1.markdown(f"`{word}`")
    if col2.button("❌", key=f"del_{word}"):
        st.session_state.stopwords.remove(word)
        st.sidebar.info("Stopword çıkarıldı. Lütfen sayfayı yenileyin.")

# Analiz Fonksiyonu
def draw_analyses(texts, stopwords, selected_analyses):
    all_text = " ".join(texts).lower()
    words = re.findall(r"[\wçğıiöşü]+", all_text)
    filtered_words = [w for w in words if w not in stopwords]
    word_freq = Counter(filtered_words)

    st.header("📈 Word Cloud ve Analizler")

    wc = WordCloud(width=800, height=600, background_color="white").generate_from_frequencies(word_freq)
    fig_wc, ax_wc = plt.subplots(figsize=(10, 7))
    ax_wc.imshow(wc, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc)

    img_buffer = BytesIO()
    fig_wc.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    st.download_button("💾 WordCloud PNG indir", data=img_buffer, file_name="wordcloud.png", mime="image/png")

    st.markdown("### Kelime Frekans Tablosu")
    freq_df = pd.DataFrame(word_freq.most_common(), columns=["Kelime", "Frekans"])
    st.dataframe(freq_df, height=300)

    if selected_analyses.get("Bar Chart (Kelime Frekansı)"):
        st.subheader("📊 Kelime Frekans Bar Grafiği")
        fig_bar, ax_bar = plt.subplots(figsize=(10, 5))
        top_words = word_freq.most_common(20)
        words_bar = [w[0] for w in top_words]
        counts_bar = [w[1] for w in top_words]
        ax_bar.bar(words_bar, counts_bar, color='skyblue')
        ax_bar.set_xticklabels(words_bar, rotation=45, ha='right')
        ax_bar.set_ylabel("Frekans")
        st.pyplot(fig_bar)
        st.markdown("""**Grafik Açıklaması:** En sık geçen 20 kelimenin frekanslarını gösterir.  
**Yorum:** Metindeki baskın kavramları ve tekrar eden temaları kolayca belirlemenizi sağlar.""")

    if selected_analyses.get("Bubble Chart"):
        st.subheader("🫧 Bubble Chart (Kelime Dağılımı)")
        top_words = word_freq.most_common(20)
        bubble_df = pd.DataFrame(top_words, columns=["Kelime", "Frekans"])
        fig_bubble, ax_bubble = plt.subplots(figsize=(10, 6))
        sizes = bubble_df["Frekans"] * 30
        ax_bubble.scatter(x=range(len(bubble_df)), y=[1] * len(bubble_df),
                          s=sizes, alpha=0.6, color="skyblue")

        for i, row in bubble_df.iterrows():
            ax_bubble.text(i, 1, row["Kelime"], ha='center', va='center', fontsize=10)

        ax_bubble.axis('off')
        st.pyplot(fig_bubble)
        st.markdown("""**Grafik Açıklaması:** Frekans büyüklüğüne göre kabarcıklarla gösterim sağlar.  
**Yorum:** Kelimelerin etkilerini sezgisel olarak fark etmeyi kolaylaştırır.""")

# Dosya yüklendiyse
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    default_col = "D" if "D" in df.columns else df.columns[0]
    selected_column = st.selectbox(
        "📋 Analiz için sütun seçin",
        options=df.columns,
        index=df.columns.get_loc(default_col)
    )

    texts = df[selected_column].astype(str).tolist()

    if texts:
        draw_analyses(texts, st.session_state.stopwords, st.session_state.selected_analyses)
else:
    st.info("Lütfen sol panelden bir Excel dosyası yükleyin ve analizleri seçin.")
