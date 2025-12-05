# Model Card

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
- Out-of-scope Uses: Assisting with approving individuals for loans, gauging credit-worthiness, etc.

## Metrics
Average of the performance metrics in slice_output.txt:
- Precision: `0.96`
- Recall: `0.89`
- F-Beta: `0.91`

## Evaluation Data
- Datasets: This model was evaluated using a 20% sample of the original data. This was chosen for simplicity.
- Preprocessing:
  - Encoding: `sklearn.preprocessing._encoders.OneHotEncoder`
    - Used for the categorical features
  - Label Binarization: `sklearn.preprocessing._label.LabelBinarizer`
    - Used to process the labels

## Training Data
- Dataset Name: US Census Income (DOI 10.24432/C5GP7S)
- Dataset Source: https://archive.ics.uci.edu/dataset/20/census+income
- Training set size: 80% of data
- Test set size: 20% of data

## Ethical Considerations
- This model was trained solely to predict if an individual is likely to make above or below 50K USD, and should only be used as such. Using this model to determine if applicants or candidates are elligible for loans, financial assitance, etc. would not be an ethical application of this model.

## Caveats and Recommendations
- This data was extracted from the 1996 US Census, so it is recommended to adjust for inflation. $50K USD in 1996 is roughly equivalent to about $100K in 2025.
- This model was unsupervised and the feature weights are not entirely clear. It would be prudent to make another model with data in the same format, but from a more recent period of time, then comparing the results to this model. 
    - This could help determine how applicable, or otherwise outdated, this model is for present days.