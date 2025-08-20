# DL-Project-
# PNEUMONIA DETECTION USING DEEP LEARNING 
An interactive web application built with **Streamlit** and **TensorFlow** that detects pneumonia from chest X-ray images.  

This project was developed as part of our **college coursework** to demonstrate how deep learning can be applied in healthcare.

---

##  Live Demo
https://dl-project12345.streamlit.app/  

---

##  Team Members
- Tharan Prasad VM (https://github.com/Tharan-18)  
- Tharun V (https://github.com/21tharun)  
- [](https://github.com/username2)  
- [Teammate 3](https://github.com/username3)  

---

##  Features
-  Upload chest X-ray images for pneumonia detection.  
-  Deep learning model trained on medical imaging dataset.  
-  Interactive and user-friendly UI with **Streamlit**.  
-  Real-time predictions with probability scores.  

---

## Tech Stack
- **Frontend**: Streamlit  
- **Backend/ML**: TensorFlow, Keras, NumPy, Pandas, Scikit-learn  
- **Visualization**: Matplotlib  

---

---

##  Dataset
- **Source**: [Chest X-Ray Pneumonia Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)  
- Contains **5,863 X-ray images** categorized into:  
  - **Normal**  
  - **Pneumonia**  

---
## Run Locally (Optional)
1. Clone the repository:
   git clone https://github.com/Tharan-18/pneumonia-detection.git
   cd pneumonia-detection
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
    streamlit run app.py
4. Upload an X-ray image and view predictions

**Model Training Details**

.Base model: Custom CNN
.Optimizer: Adam
.Loss function: binary_crossentropy
.Epochs: 12
.Achieved accuracy: ~85% on test data

**Screenshots**
Add screenshots of the web app and predictions here
Example:

**Future Enhancements**

.Integrate Grad-CAM for explainability.
.Improve accuracy using transfer learning (VGG16/ResNet50).
.Deploy on cloud (AWS/GCP/Heroku).
.Add support for multi-disease classification.


**  Reference **

.TensorFlow Documentation
.Keras Documentation
.Streamlit
.Chest X-Ray Pneumonia Dataset

** License**

This project is licensed under the MIT License.
