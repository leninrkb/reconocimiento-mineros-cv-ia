import cv2
import torch
from torchvision import transforms

# Carga el modelo en memoria
model = torch.load("modelos_yolo/best.pt")
model.eval()

# Procesamiento de video
cap = cv2.VideoCapture(0) # Abre el stream de video de la cámara web

# while True:
#     ret, frame = cap.read() # Lee el siguiente frame del video
#     if not ret:
#         break

#     # Preprocesamiento de la imagen
#     image = transforms.ToTensor()(frame)
#     image = image.unsqueeze(0)

#     # Predicción de objetos
#     with torch.no_grad():
#         prediction = model(image)

#     # Dibuja rectángulos alrededor de los objetos detectados
#     for box in prediction:
#         x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#     # Muestra la imagen resultante
#     cv2.imshow("Output", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()
