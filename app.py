from flask import Flask, request, render_template_string, redirect
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import io
import base64
import re

app = Flask(__name__)

# Başlangıç stopword seti (WordCloud default stopwords)
stopwords_set = set(STOPWORDS)

last_text = ""  # Yüklenecek ve kullanılacak metin

HTML = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8" />
    <title>Excel'den Word Cloud</title>
</head>
<body>
    <h2>Excel'den Word Cloud Oluştur</h2>

    <form method="POST" enctype="multipart/form-data" action="/upload">
        <label>Excel dosyasını seç (.xlsx):</label><br>
        <input type="file" name="file" accept=".xlsx" required>
        <button type="submit">Yükle ve Oluştur</button>
    </form>

    <br><hr><br>

    <form method="POST" action="/stopwords">
        <label>Stopword ekle veya sil (virgülle ayır):</label><br>
        <input type="text" name="words" style="width:300px" placeholder="örnek: ve, ama, çünkü" required>
        <button name="action" value="add" type="submit">Ekle</button>
        <button name="action" value="remove" type="submit">Sil</button>
    </form>

    <p><b>Mevcut Stopword'ler:</b> {{ stopwords }}</p>

    {% if wordcloud %}
    <h3>Word Cloud</h3>
    <img src="data:image/png;base64,{{ wordcloud }}" style="max-width: 800px; border: 1px solid #ccc;"/>
    {% else %}
    <p><i>Henüz bir metin yüklenmedi veya Word Cloud oluşturulmadı.</i></p>
    {% endif %}
</body>
</html>
"""

def clean_text(text):
    # Küçük harf, rakamları çıkar, noktalama kaldır
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text

def generate_wordcloud(text, stopwords):
    if not text.strip():
        return None
    wc = WordCloud(width=800, height=400, background_color="white", stopwords=stopwords).generate(text)
    img = io.BytesIO()
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(img, format="png")
    plt.close()
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route("/", methods=["GET"])
def index():
    wc_img = generate_wordcloud(last_text, stopwords_set) if last_text else None
    return render_template_string(HTML, wordcloud=wc_img, stopwords=", ".join(sorted(stopwords_set)))

@app.route("/upload", methods=["POST"])
def upload():
    global last_text
    if "file" not in request.files:
        return redirect("/")
    file = request.files["file"]
    if not file or file.filename == "":
        return redirect("/")

    try:
        df = pd.read_excel(file)
        # D sütununu al (4. sütun, indeks 3)
        if df.shape[1] < 4:
            last_text = ""
        else:
            texts = df.iloc[:, 3].dropna().astype(str).tolist()
            combined = " ".join(texts)
            last_text = clean_text(combined)
    except Exception as e:
        last_text = ""
        print(f"Hata: {e}")

    return redirect("/")

@app.route("/stopwords", methods=["POST"])
def stopwords():
    global stopwords_set
    words_raw = request.form.get("words", "")
    action = request.form.get("action", "")

    words = [w.strip().lower() for w in re.split(r",|\n", words_raw) if w.strip()]
    if action == "add":
        stopwords_set.update(words)
    elif action == "remove":
        stopwords_set.difference_update(words)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
