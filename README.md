# Bone Marrow Transplant Survival Prediction (Machine Learning)

Machine learning framework for predicting survival outcomes of pediatric patients undergoing hematopoietic stem cell transplantation (HSCT).

## 📄 Research Paper

This implementation is based on the published study:

**"Survival Prediction of Children Undergoing Hematopoietic Stem Cell Transplantation Using Different Machine Learning Classifiers by Performing Chi-squared Test and Hyper-parameter Optimization: A Retrospective Analysis"**

*Published in Computational and Mathematical Methods in Medicine (2022)*

📖 [Read the full paper](https://onlinelibrary.wiley.com/doi/full/10.1155/2022/9391136)

## 📋 Overview

This project develops a machine learning framework to predict survival outcomes of pediatric patients undergoing HSCT. It includes:
- Data cleaning and preprocessing
- Chi-squared feature selection
- Model training with multiple classifiers
- Hyperparameter optimization
- Performance visualization and evaluation

## 📂 Repository Structure

```
.
├── data/                                    # Dataset files
├── tuning/                                  # Hyperparameter tuning configurations
├── data preprocessing.ipynb                 # Data cleaning, encoding, normalization
├── feature selection.ipynb                  # Chi-squared feature selection
├── data split_bonemarrow.ipynb             # Train/test data splitting
├── bone marrow-A.ipynb                      # Classifier 1 training
├── bone marrow-B.ipynb                      # Classifier 2 training
├── bone marrow-C.ipynb                      # Classifier 3 training
├── bone marrow-D.ipynb                      # Classifier 4 training
└── bone marrow data visualisation.ipynb    # Visual analytics and plots
```

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/ishrakratul/Bone-Marrow-Transplant-Survival-Prediction-Machine-Learning.git
cd Bone-Marrow-Transplant-Survival-Prediction-Machine-Learning
```

### 2. (Optional) Create a virtual environment
```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 📦 Requirements

- pandas
- numpy
- scikit-learn
- xgboost
- matplotlib
- seaborn
- jupyter

## 💻 Usage

### 1. Launch Jupyter Notebook
```bash
jupyter notebook
```

### 2. Run notebooks in the following order:

1. `data preprocessing.ipynb`
2. `feature selection.ipynb`
3. `data split_bonemarrow.ipynb`
4. `bone marrow-A.ipynb`
5. `bone marrow-B.ipynb`
6. `bone marrow-C.ipynb`
7. `bone marrow-D.ipynb`
8. `bone marrow data visualisation.ipynb`

### 3. Adjust dataset paths
Modify file paths in the notebooks as needed and rerun to reproduce results.

## 🔬 Methods

### Feature Selection
- **Chi-squared statistical test** for feature importance

### Classifiers
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Gradient Boosting
- AdaBoost
- XGBoost

### Optimization
- **Grid Search Cross-Validation** for hyperparameter tuning

### Evaluation Metrics
- Accuracy
- ROC-AUC
- Confusion Matrix
- Precision, Recall, F1-Score

## 📊 Key Results

- ✅ Reduced feature subset (~11 features) achieved **~94.7% accuracy**
- ✅ Tuned models performed better than baseline
- ✅ Dimensionality reduction improved efficiency without accuracy loss
- ✅ Demonstrated feasibility for ML-driven clinical decision systems

## 📚 Citation

If you use this code or find it helpful, please cite:

```bibtex
@article{ratul2022survival,
  title={Survival Prediction of Children Undergoing Hematopoietic Stem Cell Transplantation Using Different Machine Learning Classifiers by Performing Chi-squared Test and Hyper-parameter Optimization: A Retrospective Analysis},
  author={Ratul, I. J. and Wani, U. H. and Nishat, M. M. and Al-Monsur, A. and Ar-Rafi, A. M. and Faisal, F. and Kabir, M. R. and others},
  journal={Computational and Mathematical Methods in Medicine},
  year={2022},
  publisher={Hindawi}
}
```

**DOI:** https://doi.org/10.1155/2022/9391136

## 🤝 Contributing

Contributions are welcome! If you discover issues, have suggestions, or wish to extend the project with:
- New classifiers
- Explainability methods (SHAP, LIME)
- Additional visualizations
- Performance improvements

Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

Ishrak Jahan Ratul and collaborators

---

**Note:** This is a research implementation. For clinical use, please consult with medical professionals and follow appropriate validation procedures.
