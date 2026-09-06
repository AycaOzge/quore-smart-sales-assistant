from flask import Blueprint, request, jsonify, render_template
from app.services.ai_service import AIService, AIServiceError
from app.database import lead_ekle, tum_leadler

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@main_bp.route('/health')
def health():
    return jsonify({"status": "ok"}), 200
@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.get_json() or {}
    mesaj = data.get('mesaj')
    gecmis = data.get('gecmis', [])

    if not mesaj:
        return jsonify({"hata": "Mesaj alanı boş olamaz!"}), 400

    try:
        yanit = AIService.yanit_uret(mesaj, gecmis)
        return jsonify({"yanit": yanit}), 200
    except AIServiceError as e:
        return jsonify({"hata": str(e)}), 503
    except Exception as e:
        return jsonify({"hata": f"Beklenmeyen bir hata oluştu: {str(e)}"}), 500

@api_bp.route('/leads', methods=['GET', 'POST'])
def leads_yonetimi():
    if request.method == 'POST':
        data = request.get_json() or {}
        isim = data.get('isim')
        telefon = data.get('telefon')
        mesaj = data.get('mesaj')

        if not isim or not telefon or not mesaj:
            return jsonify({"hata": "Tüm alanlar (isim, telefon, mesaj) zorunludur!"}), 400

        try:
            lead_ekle(isim, telefon, mesaj)
            return jsonify({"mesaj": "Lead başarıyla kaydedildi!"}), 201
        except Exception as e:
            return jsonify({"hata": f"Veritabanı hatası: {str(e)}"}), 500

    elif request.method == 'GET':
        try:
            leadler = tum_leadler()
            # SQLite satırlarını sözlüğe çevirelim
            liste = []
            for l in leadler:
                liste.append({
                    "id": l["id"],
                    "isim": l["isim"],
                    "telefon": l["telefon"],
                    "mesaj": l["mesaj"],
                    "tarih": l["tarih"]
                })
            return jsonify(liste), 200
        except Exception as e:
            return jsonify({"hata": f"Leadler alınamadı: {str(e)}"}), 500