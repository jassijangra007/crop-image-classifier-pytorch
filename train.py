import torch
import torchvision
from torchvision import datasets, transforms, models
from torch import nn, optim
import os
import shutil
from PIL import Image

# Image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Load dataset
train_data = datasets.ImageFolder("dataset", transform=transform)
train_loader = torch.utils.data.DataLoader(train_data, batch_size=16, shuffle=True)

# Load pretrained model
model = models.efficientnet_b0(pretrained=True)

# Modify final layer
model.classifier[1] = nn.Linear(model.classifier[1].in_features, len(train_data.classes))

# Loss & optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(5):
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1} completed")

# Save model
torch.save(model.state_dict(), "crop_model.pth")
