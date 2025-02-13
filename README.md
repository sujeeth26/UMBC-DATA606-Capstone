
# Predicting Patient Admission and Length of Stay in Emergency Departments Using ML

## Author
**Sujeeth Reddy Sithagari**
- **GitHub**: [github.com/sujeeth26/UMBC-DATA606-Capstone](https://github.com/sujeeth26/UMBC-DATA606-Capstone)
- **LinkedIn**: [linkedin.com/in/sujeeth-sithagari](https://www.linkedin.com/in/sujeeth-sithagari/)
- **Presentation**: [Google Slides](https://docs.google.com/presentation/d/13YE06HoTJlvNeZFHI2jn-xXgX54LJz1d/edit?usp=drive_link&ouid=103169973481008814039&rtpof=true&sd=true)
- **Video**: [YouTube](https://youtu.be/fka4pfNkTkM)

## Project Overview
This project applies machine learning to predict patient admission and length of stay in emergency departments (EDs). The goal is to help hospitals optimize resources and improve patient care.

### Objectives
1. Predict if a patient will be admitted based on triage and vital sign data.
2. Estimate the length of ED stay.
3. Develop an interactive dashboard for data visualization and model insights.

## Data
- **Source**: [MIMIC-IV ED Dataset](https://physionet.org/content/mimic-iv-ed-demo/2.2/)
- **Dataset Size**: 5MB
- **Features**: Triage data, vital signs, patient demographics.

### Target Variables
- **Classification**: Patient admission status.
- **Regression**: Length of stay in hours.

## Methodology
- **Exploratory Data Analysis (EDA)**: Data cleaning, handling missing values, and feature engineering.
- **Model Selection**: Random Forest, XGBoost, and Logistic Regression.
- **Evaluation Metrics**:
  - Classification: Accuracy, Precision, Recall, F1-score.
  - Regression: R² score, RMSE.
- **Implementation**: Streamlit web app for user-friendly predictions.

## Results
- **Best Model**: Random Forest for both classification and regression.
- **Accuracy**: 85% (classification), R² = 0.78 (regression).
- **Visualization**: Interactive plots for data insights and model interpretability.

## How to Use
1. Clone the repository:
   ```sh
   git clone https://github.com/sujeeth26/UMBC-DATA606-Capstone.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Future Work
- Integrate more patient-specific features.
- Improve model performance using deep learning.
- Deploy as a mobile-friendly application.

## References
- [MIMIC-IV Documentation](https://physionet.org/content/mimic-iv-ed-demo/2.2/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)

---
This README provides a concise yet comprehensive overview of the project. Let me know if you'd like any modifications!
