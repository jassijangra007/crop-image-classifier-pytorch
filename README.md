# crop-image-classifier-pytorch
Deep learning-based crop classification system using EfficientNet (PyTorch) that automatically classifies and sorts agricultural images into categories.

# 🌾 Crop Image Classifier (PyTorch)

A deep learning-based image classification system that identifies different crop types using **EfficientNet-B0** and automatically sorts images into folders.

---

## 🚀 Features

* 🔍 Crop classification using deep learning
* ⚡ EfficientNet-B0 pretrained model
* 📂 Automatic image sorting into class folders
* 🧠 Supports multiple crop categories

---

## 🏷️ Classes

* barley
* builtup
* cabbage
* fodder
* mustard
* pulses
* safeda
* sugarcane
* wheat

---

## 📁 Project Structure

```
├── train.py
├── predict.py
├── crop_model.pth
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/crop-image-classifier-pytorch.git
cd crop-image-classifier-pytorch
pip install -r requirements.txt
```

---

## 🧪 Training

```bash
python train.py
```

Make sure your dataset folder structure is:

```
dataset/
 ├── wheat/
 ├── mustard/
 ├── pulses/
 └── ...
```

---

## 🔍 Prediction & Auto Sorting

Update paths in `predict.py`:

```python
input_folder = "your/input/folder"
output_folder = "your/output/folder"
```

Then run:

```bash
python predict.py
```

---

## 💾 Model

The trained model is saved as:

```
crop_model.pth
```

---

## 📌 Notes

* Ensure class order in `predict.py` matches training data.
* Works on CPU (no GPU required).
* Dataset not included due to size.

---

## 👨‍💻 Author

Jassi

---

## ⭐ If you like this project, give it a star!
