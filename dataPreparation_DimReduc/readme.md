# README - Data Preparation and Model Performance Impact

## 1. Optimized Data Preparation

### Encoding Categorical Variables
When the dataset contains columns of type "object" (text), these variables are transformed into numeric values using **OneHotEncoder** with `handle_unknown='ignore'` to prevent errors caused by unseen categories. The transformed features are added back to the dataset after dropping the original categorical columns.

### Feature Selection
Feature selection is performed in two steps:
1. **Low-variance feature removal:** Features with variance below the median variance are eliminated using **VarianceThreshold**.
2. **Top-K feature selection:** The 15 most significant features are selected using **SelectKBest** with the **f_classif** scoring function.

### Data Normalization
All features are scaled using **StandardScaler** to ensure that no variable disproportionately influences the model. This is particularly important for models like **SVM** and **neural networks**.

### Dimensionality Reduction
**PCA (Principal Component Analysis)** is applied to reduce dimensionality to 10 components while preserving as much variance as possible. The explained variance ratio is printed to verify the effectiveness of this step.

## 2. Impact on Model Performance

### Reduced Training Time
Feature selection and dimensionality reduction help decrease the number of input variables, leading to faster model training times. Models like **Random Forest** and **neural networks** benefit significantly from this optimization.

### Accuracy Improvement or Degradation
By removing less relevant features and reducing noise, models such as **SVM** and **Random Forest** may show improved accuracy. However, removing too many features may lead to slight accuracy degradation in certain cases.

## 3. Variations in Displayed Scores
Model performance is evaluated using **accuracy_score**. Due to feature selection and preprocessing steps, accuracy values may differ from raw dataset results. Additionally, the **variance of scores** obtained during **cross-validation** could be lower, indicating more stable model performance.

