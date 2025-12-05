# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- Name: Income Predictor Based on Census Demographics
- Model Type: Unsupervised random forest classifier
- Model Version: `1.0.0`
- Architecture:
  - scikit-learn `RandomForestClassifier()`
    - `100` estimators
    - `99` as the random state seed
    - All other values left as their defaults

## Intended Use
- Primary Uses: Predicting if a person is likely to make above or below $50K USD based on personal and environmental demographics.
- Primary Users: Hobbyists, researchers.
- Out-of-scope Uses: Assisting with approving individuals for loans, gauging their "worth", etc.

## Factors


## Metrics
_Please include the metrics used and your model's performance on those metrics._

## Evaluation Data
- Datasets: 
- Motivation: 
- Preprocessing: 

## Training Data
- Dataset Name: US Census Income (DOI 10.24432/C5GP7S)
- Dataset Source: https://archive.ics.uci.edu/dataset/20/census+income
- Training set size: 80% of data
- Test set size: 20% of data

## Ethical Considerations
- This model was trained solely to predict if an individual is likely to make above or below 50K USD, and should only be used as such.

## Caveats and Recommendations
- This data was extracted from the 1996 US Census, so it is recommended to adjust for inflation. $50K USD in 1996 is roughly equivalent to about $100K in 2025
- This model was unsupervised and the feature weights are not entirely clear. It would be prudent to make another model with data in the same format, but from a more recent period of time, then comparing the results to this model. This would help determine how applicable, or otherwise outdated, this model is for present days.
- Validations were performed using the same data with some imputations. It is as close to data from 1996 that we can get, while still having a decently sized pool of data to pull from.




-----


• Model Details. Basic information about the model.
    – Person or organization developing model
    – Model date
    – Model version
    – Model type
    – Information about training algorithms, parameters, fairness constraints or other applied approaches, and features
    – Paper or other resource for more information
    – Citation details
    – License
    –Where to send questions or comments about the model
• Intended Use. Use cases that were envisioned during development.
    – Primary intended uses
    – Primary intended users
    – Out-of-scope use cases
• Factors. Factors could include demographic or phenotypic
groups, environmental conditions, technical attributes, or
others listed in Section 4.3.
    – Relevant factors
    – Evaluation factors
• Metrics. Metrics should be chosen to reflect potential realworld impacts of the model.
    – Model performance measures
    – Decision thresholds
    – Variation approaches
• Evaluation Data. Details on the dataset(s) used for the
quantitative analyses in the card.
    – Datasets
    – Motivation
    – Preprocessing
• Training Data. May not be possible to provide in practice.
When possible, this section should mirror Evaluation Data.
If such detail is not possible, minimal allowable information
should be provided here, such as details of the distribution
over various factors in the training datasets.
• Quantitative Analyses
    – Unitary results
    – Intersectional results
• Ethical Considerations
• Caveats and Recommendations