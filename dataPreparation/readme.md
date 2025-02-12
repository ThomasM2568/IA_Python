# README - Data Preparation and Model Performance Impact

## 1. Optimized Data Preparation

### Encoding Categorical Variables
When the dataset contains columns of type "object" (text), these variables are transformed into numeric values using **OneHotEncoder**. This helps avoid errors related to models that don't support non-numeric data.

### Feature Selection
Only the most significant variables are retained. This step simplifies the model and can potentially improve its performance by reducing complexity.

### Data Normalization
All features are scaled using **StandardScaler**. This ensures that no variable disproportionately influences the model, which is especially important for models like **SVM** and **neural networks**.

## 2. Impact on Model Performance

### Reduced Training Time
Reducing the number of features leads to faster models. We observed that models like **Random Forest** and **neural networks** train faster after the data preparation process.

### Accuracy Improvement or Degradation
By removing noise from the data, some models like **SVM** and **Random Forest** may show improved accuracy. However, if too many variables are removed, a slight decrease in accuracy might be observed.

## 3. Variations in Displayed Scores
Model performance is displayed as usual. However, **accuracy_score** values may vary after the data preparation steps. Additionally, the **variance of scores** obtained during **cross-validation** could be lower.
