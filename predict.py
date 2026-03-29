import torch
import torchvision.models as models
import torchvision.transforms as transforms
from torch import nn
from PIL import Image
import os
import shutil

# -------- 1. Transform --------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# -------- 2. Recreate Model Architecture --------
model = models.efficientnet_b0(pretrained=False)

num_classes = 9   # IMPORTANT: You have 9 folders
model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)

# -------- 3. Load Trained Weights --------
model.load_state_dict(torch.load("crop_model.pth", map_location=torch.device('cpu')))
model.eval()

# -------- 4. Class Names (MUST MATCH TRAINING ORDER) --------
class_names = [
    "barley",
    "builtup",
    "cabbage",
    "fodder",
    "mustard",
    "pulses",
    "safeda",
    "sugarcane",
    "wheat"
]

# -------- 5. Folder Paths --------
input_folder = "C:/Jassi/MyAlbumsj/Pictures"
output_folder = "C:/Jassi/Sorted_Photos"

# -------- 6. Auto Sorting --------
for filename in os.listdir(input_folder):

    img_path = os.path.join(input_folder, filename)

    try:
        image = Image.open(img_path).convert("RGB")
        image = transform(image).unsqueeze(0)

        with torch.no_grad():
            output = model(image)
            _, predicted = torch.max(output, 1)

        class_name = class_names[predicted.item()]
        class_folder = os.path.join(output_folder, class_name)

        os.makedirs(class_folder, exist_ok=True)
        shutil.copy(img_path, class_folder)

        print(f"{filename} -> {class_name}")

    except Exception as e:
        print(f"Skipping {filename} | Error: {e}")

print("Sorting Completed Successfully!")
