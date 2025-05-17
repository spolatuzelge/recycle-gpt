from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Google Gemini API anahtarınızı buraya ekleyin
GEMINI_API_KEY = "api-key"

# API anahtarını yapılandırma
genai.configure(api_key=GEMINI_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')  # Ana sayfa

@app.route('/get-products', methods=['GET'])
def get_products():
    material = request.args.get('material').lower()
    prompt = f"""Geri dönüştürülebilir malzeme olan '{material}'leri bir arada kullanarak hangi ürünler yapılabilir? 
                Kısaca birkaç örnek verir misiniz?"""

    try:
        # Modeli çağır
        model = genai.GenerativeModel("gemini-1.5-flash")
        # Prompt ile içerik oluştur
        response = model.generate_content(prompt)

        print("API Yanıtı:", response.text)  # Yanıtı terminale yazdır

        # Yanıtı listeye dönüştür, boş elemanları filtrele ve yıldız işaretlerini kaldır
        products = [line.replace("*", "").strip() for line in response.text.split("\n") if line.strip()]
        print("Ürünler Listesi:", products)  # Ürün listesini kontrol et

        # JSON formatında döndür
        return jsonify({"products": products})
    except Exception as e:
        print("Hata:", e)  # Hata varsa terminale yazdır
        return jsonify({"products": ["Bir hata oluştu: " + str(e)]})

if __name__ == '__main__':
    app.run(debug=True)
