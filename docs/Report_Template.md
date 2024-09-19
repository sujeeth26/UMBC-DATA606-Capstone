# The Template and Guideline for the Final Report

- This document serves as a guide for developing project proposal which will eventually become the proposal and final report.
- You start with the end in mind and adopt an agile approach:
  - Making progress continuously towards your goal.
  - Updating this document continuously along the way.
 
## 1. Title and Author

- Project Title:Predicting Patient Admission and Length of Stay in Emergency Departments Using ML
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author Name:SITHAGARI SUJEETH REDDY
- Link to the author's GitHub repo of the project:https://github.com/sujeeth26/UMBC-DATA606-Capstone
- Link to the author's LinkedIn profile:https://www.linkedin.com/in/sujeeth-sithagari/
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

Provide the background information about the chosen topic. 

- What is it about? 
This project explores the application of machine learning techniques to predict two critical outcomes in emergency departments (EDs):
1.	Patient Admission: Will a patient be admitted to the hospital or discharged after their ED visit?
2.	Length of Stay: How long is a patient likely to stay in the ED?
By leveraging triage data (collected upon arrival) and vital sign data (recorded throughout the stay), the project aims to develop models that provide accurate predictions to improve hospital resource management and patient care. 

- Why does it matter? 
Efficient prediction of patient admission and length of stay is vital for:
•	Optimizing hospital resources (e.g., beds, staff).
•	Reducing ED congestion and wait times.
•	Prioritizing care for high-risk patients.
These predictions can help healthcare providers plan better, resulting in improved patient outcomes and operational efficiency in emergency departments.

- What are your research questions?

1.	Can machine learning models predict whether a patient will be admitted based on triage and vital sign data?
2.	Can we estimate the length of a patient's ED stay using these features?
3.	How do interactive visualizations using Plotly enhance our understanding of the data and model results?


## 3. Data 

Describe the datasets you are using to answer your research questions.

The datasets were provided by a healthcare institution and include:
•	ED Stays: Records of patient visits to the emergency department.
•	Triage: Data collected at the time of the patient's initial assessment.
•	Vitalsign: Continuous recordings of patient vital signs during their stay.

Data Size:
The datasets are small, approximately 5 MB in total.

Data Shape:
•	ED Stays: 222 rows, 9 columns
•	Triage: 222 rows, 11 columns
•	Vitalsign: 1,038 rows, 11 columns

Time Period:
The data spans 2010 to 2020.
What does each row represent?:
•	ED Stays: A single visit by a patient to the emergency department.
•	Triage: The initial assessment of a patient’s condition.
•	Vitalsign: A set of vital signs recorded at a specific time during the ED stay.

Data Dictionary:

## Data Dictionary

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



Target/Label Variables:
•	Classification: disposition (admission status).
•	Regression: length_of_stay (time in hours).

Features/Predictors:
•	Triage Data: temperature, heartrate, resprate, o2sat, sbp, dbp, pain, chiefcomplaint, acuity.
•	Demographics: gender, race, arrival_transport.


## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook
- You would focus on the target variable and the selected features and drop all other columns.
- produce summary statistics of key variables
- Create visualizations (I recommend using **Plotly Express**)
- Find out if the data require cleansing:
  - Missing values?
  - Duplicate rows? 
- Find out if the data require splitting, merging, pivoting, melting, etc.
- Find out if you need to bring in other data sources to augment your data.
  - For example, population, socioeconomic data from Census may be helpful.
- For textual data, you will pre-process (normalize, remove stopwords, tokenize) them before you can analyze them in predictive analysis/machine learning.
- Make sure the resulting dataset need to be "tidy":
  - each row represent one observation (ideally one unique entity/subject).
  - each columm represents one unique property of that entity. 

## 5. Model Training 

- What models you will be using for predictive analytics?
- How will you train the models?
  - Train vs test split (80/20, 70/30, etc.)
  - Python packages to be used (scikit-learn, NLTK, spaCy, etc.)
  - The development environments (your laptop, Google CoLab, GitHub CodeSpaces, etc.)
- How will you measure and compare the performance of the models?

## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- **Streamlit** (recommended for its simplicity and ease to learn)
- Dash
- Flask

## 7. Conclusion

- Summarize your work and its potetial application
- Point out the limitations of your work
- Lessons learned 
- Talk about future research direction

## 8. References 

List articles, blogs, and websites that you have referenced or used in your project.
