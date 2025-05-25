
# ♻️  Geri Dönüşümden Ürün Önerici Chatbot

Bu proje geri dönüştürülebilir malzemeleri kullanarak neler üretilebileceğini öneren yapay zekâ destekli bir web uygulamasıdır.  
Kullanıcıdan aldığı malzeme bilgisine göre, Google Gemini modeli ile ürün önerileri sunar. Uygulama tamamen Türkçe arayüzlüdür.

---

## 🚀 Özellikler

- ✅ Kullanıcıdan metin girdisi alır (örnek: *pet şişe, karton kutu*)
- ✅ Gemini LLM kullanarak ürün önerileri oluşturur
- ✅ Sonuçları liste halinde gösterir
- ✅ Kullanıcı dostu, mobil uyumlu web arayüz
- ✅ Hafif, tek dosyalı Flask uygulaması

---

## 🧰 Kullanılan Teknolojiler

- Python + Flask
- Google Generative AI (Gemini 1.5 Flash)
- HTML + CSS (responsive tasarım)
- JavaScript (fetch API)

---

## 📁 Proje Yapısı

```
.
├── app.py               # Flask sunucu dosyası
├── requirements.txt     # Gerekli Python kütüphaneleri
├── static/
│   ├── style.css        # Özel sayfa tasarımı
│   └── images.png         # Logo/görsel
├── templates/
│   └── index.html       # Ana sayfa HTML dosyası
└── README.md            # Proje açıklaması (bu dosya)
```

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Ortamı Hazırlayın

```bash
python -m venv venv
source venv/bin/activate     # Windows için: venv\Scripts\activate
```

### 2. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 3. API Anahtarınızı Ekleyin

`app.py` içinde `GEMINI_API_KEY` değişkenine kendi Google API anahtarınızı girin:

```python
GEMINI_API_KEY = "your-api-key-here"
```

### 4. Uygulamayı Başlatın

```bash
python app.py
```


## ✨ Kullanım

1. Ana sayfadaki giriş alanına geri dönüştürülebilir malzeme adını yazın.  
   Örnek: `cam şişe`, `karton kutu`, `alüminyum kutu`
2. “DÖNÜŞTÜR” butonuna basın
3. Önerilen ürünler sayfanın altında listelenir
