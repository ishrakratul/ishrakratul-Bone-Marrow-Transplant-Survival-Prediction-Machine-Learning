project:
  title: "Bone Marrow Transplant Survival Prediction (Machine Learning)"
  description: >
    Implementation of data preprocessing, feature selection, model training, and
    evaluation workflows for survival prediction of pediatric patients undergoing
    hematopoietic stem cell transplantation (HSCT).  
    Based on the published study:
    "Survival Prediction of Children Undergoing Hematopoietic Stem Cell Transplantation
    Using Different Machine Learning Classifiers by Performing Chi-squared Test and
    Hyper-parameter Optimization: A Retrospective Analysis"
    Published in *Computational and Mathematical Methods in Medicine (2022)*  
    DOI: https://onlinelibrary.wiley.com/doi/full/10.1155/2022/9391136

overview:
  summary: |
    This project develops a machine learning framework to predict survival outcomes
    of pediatric patients undergoing HSCT. It includes data cleaning, Chi-squared
    feature selection, model training with multiple classifiers, hyperparameter
    optimization, and visualization of results.

  key_steps:
    - Data cleaning and preparation
    - Feature selection using Chi-squared test
    - Model training with multiple classifiers
    - Hyperparameter tuning (Grid Search CV)
    - Visualization and performance evaluation

repository_structure:
  files:
    - "data preprocessing.ipynb: Data cleaning, encoding, normalization"
    - "feature selection.ipynb: Chi-squared feature selection"
    - "data split_bonemarrow.ipynb: Train/test data splitting"
    - "bone marrow-A.ipynb: Classifier 1 training"
    - "bone marrow-B.ipynb: Classifier 2 training"
    - "bone marrow-C.ipynb: Classifier 3 training"
    - "bone marrow-D.ipynb: Classifier 4 training"
    - "bone marrow data visualisation.ipynb: Visual analytics and plots"

installation:
  steps: |
    1. Clone the repository:
         git clone https://github.com/<your-username>/bone-marrow-survival-ml.git
         cd bone-marrow-survival-ml

    2. (Optional) Create a virtual environment:
         python -m venv venv
         source venv/bin/activate      # Mac/Linux
         venv\Scripts\activate         # Windows

    3. Install dependencies:
         pip install -r requirements.txt

requirements:
  - pandas
  - numpy
  - scikit-learn
  - xgboost
  - matplotlib
  - seaborn
  - jupyter

usage:
  steps: |
    1. Launch Jupyter Notebook:
         jupyter notebook

    2. Run notebooks in the following order:
         - data preprocessing.ipynb
         - feature selection.ipynb
         - data split_bonemarrow.ipynb
         - bone marrow-A.ipynb
         - bone marrow-B.ipynb
         - bone marrow-C.ipynb
         - bone marrow-D.ipynb
         - bone marrow data visualisation.ipynb

    3. Adjust dataset paths and rerun to reproduce results.

methods:
  feature_selection: "Chi-squared statistical test"
  classifiers:
    - Logistic Regression
    - Decision Tree
    - Random Forest
    - K-Nearest Neighbors
    - Gradient Boosting
    - AdaBoost
    - XGBoost
  optimization: "Grid Search Cross-Validation"
  metrics:
    - Accuracy
    - ROC-AUC
    - Confusion Matrix

results:
  highlights: |
    - Reduced feature subset (~11 features) achieved ~94.7% accuracy
    - Tuned models performed better than baseline
    - Dimensionality reduction improved efficiency without accuracy loss
    - Demonstrated feasibility for ML-driven clinical decision systems

citation:
  text: |
    Ratul, I. J., Wani, U. H., Nishat, M. M., Al-Monsur, A., Ar-Rafi, A. M., Faisal, F., Kabir, M. R., et al.
    "Survival Prediction of Children Undergoing Hematopoietic Stem Cell Transplantation Using Different
    Machine Learning Classifiers by Performing Chi-squared Test and Hyper-parameter Optimization:
    A Retrospective Analysis."
    *Computational and Mathematical Methods in Medicine, 2022.*
    DOI: https://onlinelibrary.wiley.com/doi/full/10.1155/2022/9391136

contributing:
  guidelines: |
    Contributions are welcome!
    If you discover issues, have suggestions, or wish to extend the project
    (new classifiers, explainability methods, or visualizations),
    please open an issue or submit a pull request.
