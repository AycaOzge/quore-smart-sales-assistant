# QUORE Smart Sales Assistant

QUORE Smart Sales Assistant, ziyaretçilerin yapay zekâ destekli bir satış asistanı ile iletişim kurabildiği ve iletişim bilgilerini bırakabildiği web tabanlı bir projedir.

Proje, QUORE adlı kişiselleştirilebilir premium güzellik markası için geliştirilmiştir. Sistem; ziyaretçi arayüzü ve işletme sahibinin müşteri adaylarını görüntüleyebildiği yönetim paneli olmak üzere iki temel arayüzden oluşur.

## Özellikler

- Yapay zekâ destekli QUORE satış asistanı
- Kullanıcının mesajına göre ürün ve kişiselleştirme önerileri
- İsim ve telefon bilgisi ile lead kaydı
- Lead bilgilerinin SQLite veritabanında saklanması
- Yönetim panelinde kayıtların listelenmesi
- Wix Studio ve Velo entegrasyonu
- Flask REST API
- Groq API entegrasyonu
- Render üzerinde canlı backend

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Wix Studio
- Wix Velo
- JavaScript
- Render
- GitHub

## Proje Mimarisi

Proje Separation of Concerns (SoC) prensibine göre modüler olarak geliştirilmiştir.

- `config.py` — uygulama yapılandırması ve QUORE iş bağlamı
- `database.py` — SQLite veritabanı işlemleri
- `routes.py` — HTTP ve API rotaları
- `services/ai_service.py` — yapay zekâ servisi
- `run.py` — Flask uygulamasının giriş noktası

## API Uç Noktaları

- `GET /health` — backend durumunu kontrol eder
- `POST /api/sohbet` — kullanıcı mesajını yapay zekâ asistanına gönderir
- `POST /api/leads` — yeni müşteri adayını kaydeder
- `GET /api/leads` — kayıtlı müşteri adaylarını listeler

## Yapay Zekâ Modeli

Proje Groq API üzerinden çalışmaktadır. Proje yönergesinde belirtilen `llama-3.1-8b-instant` modeli mevcut Groq hesabında erişilebilir olmadığı için, çalışan ve erişilebilir bir Groq modeli kullanılmıştır.

## Çalıştırma

Bağımlılıkları yüklemek için:

pip install -r requirements.txt

Uygulamayı çalıştırmak için:

python run.py

API anahtarları ve diğer gizli bilgiler `.env` dosyasında tutulur ve güvenlik nedeniyle GitHub deposuna dahil edilmez.

## QUORE

QUORE; kişiselleştirilebilir renk, ten tonu, bitiş ve aromatik ritüel seçeneklerini akıllı biyomimetik tasarım yaklaşımıyla birleştiren konsept bir premium güzellik markasıdır.
