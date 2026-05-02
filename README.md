# 🐶 Cat vs Dog Image Classifier

## 📌 Description

This project is a Convolutional Neural Network (CNN) based image classifier that predicts whether a given image is a **Cat 🐱** or a **Dog 🐶**.

The model is built using deep learning techniques and trained on image data to learn patterns and features that distinguish cats from dogs.

---

## ⚙️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy

---

## 🧠 Model Architecture

* Conv2D + ReLU
* MaxPooling2D
* Conv2D + ReLU
* MaxPooling2D
* Conv2D + ReLU
* MaxPooling2D
* Flatten
* Dense (512 neurons)
* Output Layer (Sigmoid)

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the program

```
python image.py
```

---

## 📂 Project Structure

```
cat-dog-classifier/
│
├── image.py
├── requirements.txt
├── README.md
```

---

## 📊 Output

The model takes an image as input and prints the prediction in the console:

* **Dog 🐶**
* **Cat 🐱**

---

## ⚠️ Note

* Dataset is not included due to large size.
* Update dataset and image paths in the code before running.

---

## 📈 Future Improvements

* Increase model accuracy with more epochs
* Add GUI or web interface
* Deploy as a web app
* Add real-time prediction using webcam

---

## 🙌 Author

Your Name

---
