##### 🌊 Hydro World – Water Potability Analysis System

##### 

##### Hydro World is a full-stack water quality analysis system that predicts whether water is Safe or Unsafe for drinking based on physicochemical properties.

##### The system uses machine learning (SVM + Gradient Boosting) on a real-world dataset and provides a clean, user-friendly web interface for analysis.

##### 

##### 🚀 Features:

##### ✅ Real dataset-based prediction (Kaggle Water Potability dataset)

##### ✅ Machine Learning models:

##### &nbsp; - Support Vector Machine (SVM)

##### &nbsp; - Gradient Boosting

##### &nbsp; - Weighted Ensemble (Combined Model)

##### ✅ Pure CPU-based training (no GPU/PyTorch dependency issues)

##### ✅ Final output shown to users as Safe / Unsafe

##### ✅ Backend API with training \& prediction endpoints

##### ✅ Web UI for input and analysis

##### ✅ Model evaluation with Accuracy, Precision, Recall \& F1-score

##### ✅ Scalable project structure

##### 

##### 🧠 Machine Learning Overview:

##### 

##### Input Parameters:

##### \- pH

##### \- Hardness

##### \- Solids

##### \- Chloramines

##### \- Sulfate

##### \- Conductivity

##### \- Organic Carbon

##### \- Trihalomethanes

##### \- Turbidity

##### 

##### Target:

##### \- `0` → Unsafe

##### \- `1` → Safe

##### 

##### Models Used-

##### \- Support Vector Machine (SVM)

##### \- Gradient Boosting Classifier

##### \- Ensemble (weighted average of probabilities)

##### 

##### Why CPU-only?

##### 

##### \- Sklearn models are CPU-optimized

##### \- Avoids GPU configuration issues

##### \- Faster setup \& more stable deployment

##### 

##### 📊 Dataset:

##### 

##### \- Source: Kaggle – Water Potability Dataset

##### \- Link: \[https://www.kaggle.com/datasets/adityakadiwal/water-potability](https://www.kaggle.com/datasets/adityakadiwal/water-potability)

##### \- File: `data/water\_potability.csv`

##### 

##### 🗂 Project Structure:

##### 

##### Hydro\_World/

##### │

##### ├── backend/

##### │   ├── app.py

##### │   ├── routes/

##### │   └── services/

##### │

##### ├── ml/

##### │   ├── data/

##### │   │   ├── dataset\_loader.py

##### │   │   └── prepare\_data.py

##### │   │

##### │   ├── models/

##### │   │   ├── svm\_model.py

##### │   │   └── gb\_model.py

##### │   │

##### │   ├── ensemble/

##### │   │   └── combined\_model.py

##### │   │

##### │   ├── training/

##### │   │   └── trainer.py

##### │   │

##### │   └── utils/

##### │       └── checkpoint.py

##### │

##### ├── data/

##### │   └── water\_potability.csv

##### │

##### ├── web/

##### │   ├── static/

##### │   └── templates/

##### │

##### ├── run.py

##### └── README.md



##### ⚙️ Setup Instructions:

##### 

##### 1️⃣ Clone Repository

##### 

##### git clone <repo-url>

##### cd Hydro\_World

##### 

##### 2️⃣ Create Virtual Environment

##### 

##### python -m venv venv

##### venv\\Scripts\\activate   # Windows

##### 

##### 3️⃣ Install Dependencies

##### 

##### pip install -r requirements.txt

##### 

##### 4️⃣ Run Backend Server

##### 

##### python run.py

##### 

##### Server will start at:

##### 

##### http://127.0.0.1:8000

##### 

##### 🖥 Web Interface:

##### 

##### \- Enter water parameters

##### \- Click \*\*Analyze Water\*\*

##### \- Output shown as:

##### 

##### &nbsp; - ✅ Safe

##### &nbsp; - ❌ Unsafe

##### 

##### (Internally, ensemble ML models decide the result, but user sees only final classification.)

##### 

##### 📈 Model Performance:

##### 

##### \* Accuracy ~ 65–70%

##### \* Precision \& Recall optimized via probability thresholding

##### \* Realistic results due to real-world dataset imbalance

##### 

##### > Note: In water safety prediction, precision \& recall are more important than raw accuracy.

##### 

##### 

##### 🧪 Training Flow:

##### 

##### 1\. Load dataset

##### 2\. Handle missing values

##### 3\. Scale features

##### 4\. Train SVM \& Gradient Boosting

##### 5\. Build ensemble model

##### 6\. Evaluate \& save models

##### 7\. Use trained models for predictions

##### 

##### 

##### ❗ Important Notes:

##### 

##### \- No GPU / PyTorch is used

##### \- All models are sklearn-based

##### \- Stable on Windows

##### \- Designed to be extended later (DL models, real-time sensors, etc.)

##### 

##### 🔮 Future Enhancements (Optional):

##### 

##### \* Real-time sensor integration

##### \* Time-series water monitoring

##### \* Advanced ensemble weighting

##### \* Cloud deployment

##### \* Mobile-friendly UI

##### 

##### 👨‍💻 Author:

##### 

##### Built with focus on stability, clarity, and real-world usability.

##### Designed to be extendable without breaking the existing system.



