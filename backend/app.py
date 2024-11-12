from flask import Flask, request, jsonify
import torch
from PIL import Image

app = Flask(__name__)

# Cargar el modelo YOLOv11
# Asegúrate de que 'model.pt' esté en la misma carpeta que app.py
model = torch.hub.load('ultralytics/yolov11', 'custom', path='model.pt', force_reload=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    image = Image.open(file.stream)

    # Realizar la inferencia
    results = model(image)
    data = results.pandas().xyxy[0].to_dict(orient="records")  # Extraer resultados en formato JSON
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)), debug=True)
