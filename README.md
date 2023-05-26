MLP-6  - Predictive web application for customer churn rate for telecom service providers.

Industry
Telecommunications 

Skills
Python | Streamlit | Machine Learning algorithms | Machine Learning deployment | web development | EDA | Deep learning | Customer churn | Customer analysis

Problem statements
Build a front end application with an easy to use UI that allows you to predict customer churn rate. 
Behavioral Segmentation of base
Build predictive model
Adjust customer service, service or campaign depending on problem

Data Description
Must have data sources
Customer demographics/Acquisition data
Usage and reload data
Customer segment/ Campaign Data
Service history 

Dataset metrics - 
customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Churn

Stakeholder benefits 
Effectively manage customer churn through proactive and preventive management via using indicators of churn 
Reduce number of churned customers
Insights on churn behavior
Put marketing campaign efforts into potential customers with a low churn probability (market service more effectively and save costs)
Report loss due to churn 
Retention saves costs as it’s more effective than re-acquisition 
Classification of churners 



Methods
Based on findings make adjustments to service, customer service or campaigns depending on where the problem lies
Determine ratio of churn
Identify metrics that influence churn the most

Results 
General
Male more likely to churn 
SeniorCitizen is actually a categorical hence the 25%-50%-75% distribution is not proper
75% customers have tenure less than 55 months
Average Monthly charges are USD 64.76 whereas 25% customers pay more than USD 89.85 per month
Data is highly imbalanced, ratio = 73:27
So we analyse the data with other features while taking the target values separately to get some insights.
Since the % of these records compared to total dataset is very low ie 0.15%, it is safe to ignore them from further processing.'TotalCharges'
HIGH Churn seen in case of Month to month contracts, No online security, No Tech support, First year of subscription and Fibre Optics Internet
LOW Churn is seens in case of Long term contracts, Subscriptions without internet service and The customers engaged for 5+ years
Factors like Gender, Availability of PhoneService and # of multiple lines have alomost NO impact on Churn
This is also evident from the Heatmap below
Machine learning models 
Tested two models: Decision Trees and Random forests (Random forests best option) 
Unbalanced data corrected with SMOTEENN class, which is a combination of the Synthetic Minority Over-sampling Technique (SMOTE) and Edited Nearest Neighbors (ENN) which increased accuracy of model from 78% to 92% with lower false positives and negatives for class 1. 

Conclusion 
 Electronic check medium are the highest churners
 Contract Type - Monthly customers are more likely to churn because of no contract terms, as they are free to go customers.
 No Online security, No Tech Support category are high churners
 Non senior Citizens are high churners
Final ML model = RF Classifier with SMOTEENN, is now ready and dumped in model.sav, which we will use and prepare API's so that we can access our model from UI.

