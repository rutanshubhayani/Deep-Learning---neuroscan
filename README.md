# Brain Tumor Detection using MRI Scans 🧠🩻

A deep learning-based web application built with **TensorFlow** and **Streamlit** to detect brain tumors from MRI scans. The model classifies MRI images as **Tumor** or **No Tumor**, providing a quick and user-friendly interface for medical image analysis.

---

## 🚀 Features
- **Upload MRI Scans** for instant brain tumor classification
- **Streamlit Web Interface** for easy accessibility
- **Deep Learning Model** trained on Brain MRI dataset from Kaggle
- **Real-time Prediction** with high accuracy
- Simple and clean UI for smooth user experience

---

## �� Project Structure
```
neuroscan/
├── app.py                    # Streamlit app file
├── train_model.ipynb         # Model training notebook
├── brain_tumor_model.keras   # Trained model file
├── requirements.txt          # Required Python packages
├── setup.sh                  # Setup script for easy installation
├── run.sh                    # Run script for easy execution
├── README.md                 # Project documentation
└── dataset/                  # Brain MRI dataset
    └── brain-mri-images-for-brain-tumor-detection/
        ├── no/               # No tumor images
        └── yes/              # Tumor images
```

## 🧪 Dataset

Dataset used: [Brain Tumor MRI Dataset - Kaggle](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection)

## 🛠️ Tech Stack

- **Python**
- **TensorFlow / Keras**
- **Streamlit**
- **NumPy, Pandas, Matplotlib**
- **Pillow** for image processing

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd neuroscan
   ```

2. **Run the setup script**
   ```bash
   ./setup.sh
   ```
   This will:
   - Create a virtual environment
   - Install all required dependencies
   - Set up the project for immediate use

3. **Run the application**
   ```bash
   ./run.sh
   ```
   Or manually:
   ```bash
   source venv/bin/activate
   streamlit run app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:8501`
   - Upload an MRI image to get instant brain tumor detection results

---

## 📝 Manual Installation (Alternative)

If you prefer manual setup:

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🎯 Usage

1. **Upload Image**: Click "Browse files" to upload an MRI scan
2. **Get Prediction**: The model will analyze the image and display results
3. **View Results**: See the prediction (Tumor/No Tumor) with confidence score

---

## 👨‍💻 Author

Poojan Trivedi

📧 Email: trivedipoojan92@gmail.com

🔗 GitHub: [poojan20](https://github.com/poojan20)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

