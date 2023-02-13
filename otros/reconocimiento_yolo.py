import torch
import torchvision

# from yolov5.models import Model
# from yolov5.utils.utils import load_classes

# model = Model(weights="modelos_yolo/best.pt")
# classes = load_classes("classes.names")

# img = preprocess_image("img/1.jpg")

# outputs = model(img)

# bboxes, labels, confs = postprocess(outputs, img.shape[2:], classes)

# visualize(img, bboxes, labels, confs)

model = torch.load("modelos_yolo/best.pt")
model.eval()

transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((224, 224)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

image = torch.unsqueeze(transform(image), 0)


with torch.no_grad():
    output = model(image)





