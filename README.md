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
git clone https://github.com/jassijangra007/crop-image-classifier-pytorch.git
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

## 📦 Pretrained Model (crop_model.pth)

This model is provided for **demonstration purposes only**.

* It has been trained on a limited dataset.
* The accuracy may not be optimal for real-world applications.
* Performance depends heavily on the **quality and quantity of training data**.

👉 You are encouraged to train your own model using:

```bash
python train.py
```

### ⚠️ Important Note

The model accuracy improves with:

* More training images 📈
* Better data quality 🎯
* Balanced class distribution ⚖️

In general:
**More data = Better accuracy**

---

### 🔁 Recommendation

For best results:

* Use a larger dataset
* Ensure proper labeling
* Train for more epochs


## 📌 Notes

* Ensure class order in `predict.py` matches training data.
* Works on CPU (no GPU required).
* Dataset not included due to size.

---

## 👨‍💻 Author

Jassi

---

## ⭐ If you like this project, give it a star!
