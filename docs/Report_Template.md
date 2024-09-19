# The Template and Guideline for the Final Report

- This document serves as a guide for developing your project proposal, which will eventually become the final report.
- Start with the end in mind and adopt an agile approach:
  - Continuously make progress towards your goal.
  - Update this document continuously along the way.

## 1. Title and Author

- **Project Title**: Predicting Patient Admission and Length of Stay in Emergency Departments Using ML
- **Prepared for**: UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name**: SITHAGARI SUJEETH REDDY
- **Link to the author's GitHub repo of the project**: [GitHub](https://github.com/sujeeth26/UMBC-DATA606-Capstone)
- **Link to the author's LinkedIn profile**: [LinkedIn](https://www.linkedin.com/in/sujeeth-sithagari/)
- **Link to your PowerPoint presentation file**
- **Link to your YouTube video**

## 2. Background

### What is it about?

This project explores the application of machine learning techniques to predict two critical outcomes in emergency departments (EDs):
1. **Patient Admission**: Will a patient be admitted to the hospital or discharged after their ED visit?
2. **Length of Stay**: How long is a patient likely to stay in the ED?

By leveraging triage data (collected upon arrival) and vital sign data (recorded throughout the stay), the project aims to develop models that provide accurate predictions to improve hospital resource management and patient care.

### Why does it matter?

Efficient prediction of patient admission and length of stay is vital for:
- Optimizing hospital resources (e.g., beds, staff).
- Reducing ED congestion and wait times.
- Prioritizing care for high-risk patients.

These predictions help healthcare providers plan better, resulting in improved patient outcomes and operational efficiency in emergency departments.

### Research Questions

1. Can machine learning models predict whether a patient will be admitted based on triage and vital sign data?
2. Can we estimate the length of a patient's ED stay using these features?
3. How do interactive visualizations using Plotly enhance our understanding of the data and model results?

## 3. Data 

### Datasets Used

The datasets were used from the database called MIMIC (Medical Information Mart for Intensive Care):

- **ED Stays**: Records of patient visits to the emergency department.
- **Triage**: Data collected at the time of the patient's initial assessment.
- **Vitalsign**: Continuous recordings of patient vital signs during their stay.

### Data Size
- The dataset size is 5 MB.

### Data Shape
- **ED Stays**: 222 rows, 9 columns
- **Triage**: 222 rows, 11 columns
- **Vitalsign**: 1,038 rows, 11 columns

### Time Period
- The data spans from 2010 to 2020.

### What does each row represent?
- **ED Stays**: A single visit by a patient to the emergency department.
- **Triage**: The initial assessment of a patient’s condition.
- **Vitalsign**: A set of vital signs recorded at a specific time during the ED stay.

### Data Dictionary

| Column Name     | Data Type  | Definition                            | Values (if categorical)            |
|-----------------|------------|----------------------------------------|-------------------------------------|
| subject_id      | int        | Unique identifier for each patient    | N/A                                 |
| stay_id         | int        | Unique identifier for each ED stay    | N/A                                 |
| hadm_id         | int        | Hospital admission ID (if admitted)   | N/A                                 |
| intime          | datetime   | Time the patient entered the ED       | N/A                                 |
| outtime         | datetime   | Time the patient left the ED          | N/A                                 |
| disposition     | string     | Outcome of the ED visit               | ADMITTED, DISCHARGED, etc.          |
| temperature     | float      | Patient’s temperature (in Fahrenheit) | N/A                                 |
| heartrate       | float      | Heart rate in beats per minute        | N/A                                 |
| resprate        | float      | Respiratory rate in breaths per minute| N/A                                 |
| o2sat           | float      | Oxygen saturation level (%)           | N/A                                 |
| sbp             | float      | Systolic blood pressure               | N/A                                 |
| dbp             | float      | Diastolic blood pressure              | N/A                                 |
| pain            | float      | Patient’s reported pain level         | 0-10                                |
| chiefcomplaint  | string     | The patient’s primary reason for ED visit| Various complaints (e.g., chest pain, headache) |
| acuity          | int        | Urgency of the case                   | 1-5                                 |

### Target/Label Variables
- **Classification**: Admission status.
- **Regression**: Length_of_stay (time in hours).

### Features/Predictors
- **Triage Data**: temperature, heartrate, resprate, o2sat, sbp, dbp, pain, chiefcomplaint, acuity.
- **Demographics**: gender, race, arrival_transport.

## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook.
- Focus on the target variable and selected features, dropping all other columns.
- Produce summary statistics of key variables.
- Create visualizations (using **Plotly Express** recommended).
- Find out if the data require cleansing:
  - Missing values?
  - Duplicate rows?
- Determine if the data require splitting, merging, pivoting, melting, etc.
- Consider bringing in other data sources to augment your data (e.g., Census data).
- Pre-process textual data (normalize, remove stopwords, tokenize) for analysis.
- Ensure the resulting dataset is "tidy":
  - Each row represents one observation (ideally one unique entity/subject).
  - Each column represents one unique property of that entity.

## 5. Model Training 

- What models will you use for predictive analytics?
- How will you train the models?
  - Train vs. test split (80/20, 70/30, etc.).
  - Python packages (scikit-learn, NLTK, spaCy, etc.).
  - Development environments (laptop, Google Colab, GitHub CodeSpaces, etc.).
- How will you measure and compare model performance?

## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- **Streamlit** (recommended for its simplicity and ease of use)
- Dash
- Flask

## 7. Conclusion

- Summarize your work and its potential application.
- Point out the limitations of your work.
- Discuss lessons learned.
- Suggest future research directions.

## 8. References 

List articles, blogs, and websites that you have referenced or used in your project.
