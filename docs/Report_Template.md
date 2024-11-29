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
- **Link to your PowerPoint presentation file** [PPT File](https://docs.google.com/presentation/d/13YE06HoTJlvNeZFHI2jn-xXgX54LJz1d/edit?usp=drive_link&ouid=103169973481008814039&rtpof=true&sd=true)
- **Link to your YouTube video**[Link](https://youtu.be/fka4pfNkTkM)

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

The datasets were used from the database called MIMIC (Medical Information Mart for Intensive Care)(https://physionet.org/content/mimic-iv-ed-demo/2.2/):
- 
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


### 4. Exploratory Data Analysis (EDA)

The dataset, used for predicting patient admission and length of stay in emergency departments, consists of 69,057 observations and 22 features per observation, including both numeric and categorical data. The dataset underwent extensive preprocessing to address missing values, duplicates, and outliers.

Key exploratory analysis steps and findings are as follows:

- **Missing Values**: The target variable, `disposition`, has no missing values, but other features such as `acuity` have a few missing entries that were handled using median imputation for numerical features and removal for categorical ones. After preprocessing, no missing values remain in the dataset.

- **Duplicates**: Duplicate rows were identified and removed to ensure the dataset is unique.

- **Feature Types**: The dataset includes both numerical features (e.g., heart rate, blood pressure) and categorical features (e.g., gender, race, arrival transport). These features were encoded appropriately using techniques such as label encoding for categorical variables and imputation for numerical data.

- **Target Variable**: The target variable, `disposition`, represents the outcome of the patient's ED visit, categorized into various values like "ADMITTED", "DISCHARGED", and "TRANSFERRED". The distribution of the target variable is approximately balanced with 51% of observations showing "ADMITTED".

- **Outliers**: The dataset was cleaned by removing outliers using the Interquartile Range (IQR) method for continuous variables. This ensures the model focuses on the most relevant and valid data points.

- **Visualizations**: Various visualizations, such as scatter plots for the relationship between `heartrate` and `length_of_stay`, were created using Plotly to better understand the relationships between variables and their impact on predictions.

- **Feature Engineering**: The feature engineering process involved creating meaningful features, such as `length_of_stay`, calculated from the `intime` and `outtime` columns. This derived feature was used for the regression model.

- **Correlation Analysis**: Correlations between features were checked, with high correlations between variables such as blood pressure and heart rate, helping refine feature selection for model training.


## 4.2 Data Visualizations:

### Scatter Plot: Heart Rate vs Length of Stay
![Scatter Plot: Heart Rate vs Length of Stay](https://github.com/sujeeth26/UMBC-DATA606-Capstone/blob/main/docs/1st%20img.png?raw=true)

This plot visualizes the relationship between heart rate and length of stay, with data points colored according to the disposition (whether the patient was admitted or discharged). This helps to observe if higher heart rates correlate with longer stays, and whether there are any patterns based on admission status.

### Box Plot: Systolic Blood Pressure vs Disposition
![Box Plot: Systolic Blood Pressure vs Disposition](https://github.com/sujeeth26/UMBC-DATA606-Capstone/blob/main/docs/2nd%20img.png?raw=true)

This box plot shows how systolic blood pressure (SBP) varies across the disposition categories. It helps in understanding the distribution of blood pressure for both admitted and discharged patients, and whether there are significant differences between the two groups.

### Histogram: Length of Stay Distribution
![Histogram: Length of Stay Distribution](https://github.com/sujeeth26/UMBC-DATA606-Capstone/blob/main/docs/3rd%20img.png?raw=true)

This histogram displays the distribution of length of stay across all patients. It provides insights into how many patients have shorter or longer stays, helping to identify any skewness in the data.

### Correlation Heatmap
![Correlation Heatmap](https://github.com/sujeeth26/UMBC-DATA606-Capstone/blob/main/docs/4th_img.png?raw=true)

This heatmap visualizes the correlation between various vital signs (such as heart rate, blood pressure, and oxygen saturation) and length of stay. It allows for a quick assessment of how strongly these variables are related to the length of stay and can reveal any potential multicollinearity or significant relationships.



## 5. Model Training 

### 5.1 Model Selection:
The dataset underwent training with multiple models, including **Random Forest Classifier**, **XGBoost**, and **Logistic Regression**, to determine the most effective model for predicting patient admission status and length of stay. After evaluating all models, the **Random Forest Classifier** emerged as the best-performing model for the classification task, demonstrating the highest accuracy and robustness against overfitting. The **Random Forest Regressor** was selected for predicting the length of stay based on its ability to handle non-linear relationships in the data effectively.

### 5.2 Model Training:
- **Train-Test Split**: The model was trained and tested using an 80/20 train-test split, with 80% of the dataset used for training and the remaining 20% for testing. This approach ensures a robust evaluation of the model’s performance on unseen data, providing insight into its generalizability.
  
- **Python Packages**: The development of this project leveraged the following Python libraries:
  - **scikit-learn**: For model building, feature selection, and evaluation.
  - **pandas**: For data manipulation and handling missing values.
  - **NumPy**: For numerical operations.
  - **Plotly**: For generating interactive visualizations to compare different features and performance metrics.
  - **matplotlib** and **seaborn**: For data visualization and plotting performance metrics.

- **Development Environments**: The project was developed and tested across multiple environments, including local machines with Jupyter notebooks and Google Colab for accessing more computational resources. This setup allowed for iterative development and testing.

- **Model Evaluation**: Several metrics were used to evaluate the performance of the models:
  - **Accuracy Score**: This provides an overall measure of how well the model classifies admissions correctly.
  - **Precision, Recall, and F1-Score**: These metrics offer insights into how the model handles imbalanced classes and how well it predicts both positive and negative outcomes.
  - **R² (for regression)**: This metric is used to evaluate how well the model predicts the length of stay, with higher values indicating better model fit.
  - **Confusion Matrix**: This tool provides a detailed breakdown of the model's performance in terms of true positives, false positives, true negatives, and false negatives.

### 5.3 User Input:
The application collects user input through a web interface for various health-related parameters, such as:
- **Age**
- **Gender**
- **Blood Pressure**
- **Oxygen Saturation**
- **Pain Level**
- **Acuity Level**
  
The system validates each input based on predefined criteria (e.g., numerical ranges, categorical values). Once the input is validated, it is processed and used by the trained **Random Forest Classifier** to predict the likelihood of the patient being admitted. Additionally, the length of stay is estimated using the **Random Forest Regressor** if the patient is admitted.


### 5.4 Predicting Admission and Length of Stay for User Input:
Once the user provides the required information, the model predicts whether they will be admitted to the hospital. If the patient is admitted, the model estimates the **length of stay**. The system also provides feedback on the user’s risk of admission based on their input and compares their values to the dataset population.


## 6. Application of the Trained Models

The Streamlit app integrates a Random Forest Classifier for predicting patient admission status and a Random Forest Regressor for estimating the length of stay in a hospital based on user-provided data. The app considers various health parameters such as heart rate, blood pressure, oxygen saturation, temperature, and other vital signs. Users input their information through an intuitive sidebar interface, receiving real-time predictions on whether they are likely to be admitted and their expected length of stay. The app further enables users to compare their health metrics with the dataset's distribution across categories like age, blood pressure, and heart rate. Additionally, it offers a detailed analysis of how each health parameter contributes to the prediction results.
![STREAMLIT APPLICATION](https://github.com/sujeeth26/UMBC-DATA606-Capstone/blob/main/docs/STREAMLIT.png?raw=true)
## 7. Conclusion

In conclusion, the Random Forest models embedded in the Streamlit app provide a practical solution for individuals to evaluate their admission likelihood and hospital stay duration based on their health data. The models help users gain insights into their healthcare needs, making the app a valuable tool in hospital management systems for improving patient flow and optimizing resources.

---

### Limitations:

Despite its utility, the current model has some limitations. It relies on a set of vital signs and demographic features, potentially missing other critical factors affecting hospital admission and length of stay, such as comorbidities or specific medical history. Moreover, the model's performance might fluctuate depending on the completeness and accuracy of the input data. To address these limitations, future work could involve incorporating additional medical data and features for more comprehensive predictions.

---

### Lessons Learned:

Several lessons have emerged throughout this project. First, the importance of developing intuitive and user-friendly interfaces, such as the Streamlit app, which allows easy interaction with complex predictive models. Second, continuous model evaluation and validation are essential to ensure that the predictions remain reliable and relevant in real-world applications. Lastly, collaboration between healthcare professionals and data scientists is crucial for enhancing the model's relevance, ensuring it accurately addresses patient care and hospital operations.

---

### Future Scope:

Looking ahead, the app’s future scope includes the potential integration of more complex features such as patient medical history, comorbid conditions, and specific treatment protocols to improve the prediction accuracy. Additionally, exploring more advanced machine learning algorithms, like XGBoost or deep learning models, could further enhance the model’s performance. Future versions of the app could also incorporate personalized care recommendations based on patient-specific data and prediction outcomes. A mobile version of the tool could broaden its accessibility and improve healthcare practices by enabling real-time decision-making in clinical settings.

### 8. References 



1. **Streamlit Documentation:**  
   Streamlit. (n.d.). Streamlit Documentation. Streamlit. Retrieved from [https://docs.streamlit.io/](https://docs.streamlit.io/)

2. **Plotly Documentation:**  
   Plotly. (n.d.). Plotly Python Open Source Graphing Library. Plotly. Retrieved from [https://plotly.com/python/](https://plotly.com/python/)

3. **Journal Article:**  
   Holden, R. J., & Karsh, B. T. (2010). The Technology Acceptance Model: Its past and its future in health care. *Journal of Biomedical Informatics, 43*(1), 159–172. doi: [10.1016/j.jbi.2009.07.002](https://doi.org/10.1016/j.jbi.2009.07.002)



