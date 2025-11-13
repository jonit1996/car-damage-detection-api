from ultralytics import YOLO
import os

# Load YOLO model once at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models/CarDamageDetection_v5.1.pt')
model = YOLO(MODEL_PATH)

def detect_damage(image_path):
    """Run YOLO inference on image and return structured detections."""
    results = model(image_path)
    detections = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        detections.append({
            "bbox": [x1, y1, x2, y2],
            "confidence": round(conf, 2),
            "class_id": cls,
            "class_name": model.names[cls]
        })
    return detections
