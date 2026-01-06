#import yolo from ultralytics
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Run detection on an image
#results = model("https://ultralytics.com/images/bus.jpg", save=True)
#detection using camera
model(source=0,show=True, save=True)
#print("Detection completed. Image saved.")