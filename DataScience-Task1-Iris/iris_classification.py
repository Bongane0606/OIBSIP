# %% [markdown]
# # Iris Flower Classification
# **OIBSIP Data Science Internship — Task 1**
#
# **Author:** Letsoenyo Clen Bongane
# **Objective:** Train a machine learning classification model to identify the
# species of an iris flower (Setosa, Versicolor, or Virginica) from its
# physical measurements (sepal length/width, petal length/width).

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
)

sns.set_theme(style="whitegrid")

# %% [markdown]
# ## 1. Load the Dataset
# The Iris dataset ships directly with scikit-learn, so no external download
# is required.

# %%
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

df.head()

# %% [markdown]
# ## 2. Exploratory Data Analysis (EDA)

# %%
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nNull values per column:\n", df.isnull().sum())

# %%
df.describe()

# %%
df["species"].value_counts()

# %% [markdown]
# **Observations:**
# - The dataset has 150 rows and 5 columns (4 numeric features + 1 categorical target).
# - There are no missing values, so no imputation is needed.
# - The dataset is perfectly balanced: 50 samples per species.

# %% [markdown]
# ## 3. Visualizations

# %%
pairplot = sns.pairplot(df, hue="species", diag_kind="hist", palette="viridis")
pairplot.fig.suptitle("Pairwise Feature Relationships by Species", y=1.02)
plt.show()

# %%
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
features = iris.feature_names
for ax, feature in zip(axes.flatten(), features):
    sns.boxplot(
        data=df, x="species", y=feature, hue="species",
        palette="viridis", ax=ax, legend=False
    )
    ax.set_title(f"{feature} by Species")
plt.tight_layout()
plt.show()

# %% [markdown]
# **Observations:**
# - *Setosa* is clearly separated from the other two species across almost
#   every feature — petal length and petal width in particular show no
#   overlap at all.
# - *Versicolor* and *Virginica* overlap somewhat, especially on sepal width
#   and sepal length, but are more separable on petal length and petal width.
# - This suggests **petal length** and **petal width** are the most
#   discriminative features for classification, while sepal width is the
#   weakest discriminator.

# %% [markdown]
# ## 4. Feature Selection Discussion
# Based on the pairplot and boxplots above, **petal length** and **petal
# width** show the cleanest separation between species and are likely to
# contribute the most predictive power. Sepal length and sepal width are
# still useful (especially in combination with the petal features) but show
# more class overlap on their own. For this task we keep all four features
# in the model — with only 4 features and 150 rows, there's no dimensionality
# problem, and letting the model weigh them avoids throwing away signal.

# %% [markdown]
# ## 5. Train/Test Split

# %%
X = df[iris.feature_names]
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Train size:", X_train.shape[0], "| Test size:", X_test.shape[0])

# %% [markdown]
# ## 6. Model Training
# We train two different classifiers and compare their performance:
# **Logistic Regression** and **K-Nearest Neighbours (KNN)**.

# %%
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)
y_pred_lr = log_reg.predict(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# %% [markdown]
# ## 7. Model Evaluation

# %%
acc_lr = accuracy_score(y_test, y_pred_lr)
acc_knn = accuracy_score(y_test, y_pred_knn)

print(f"Logistic Regression Accuracy: {acc_lr:.4f}")
print(f"KNN Accuracy: {acc_knn:.4f}")

# %%
print("=== Logistic Regression: Classification Report ===")
print(classification_report(y_test, y_pred_lr))

print("=== KNN: Classification Report ===")
print(classification_report(y_test, y_pred_knn))

# %%
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred_lr, ax=axes[0], colorbar=False, cmap="Blues"
)
axes[0].set_title("Logistic Regression — Confusion Matrix")

ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred_knn, ax=axes[1], colorbar=False, cmap="Blues"
)
axes[1].set_title("KNN — Confusion Matrix")

plt.tight_layout()
plt.show()

# %% [markdown]
# ## 8. Best Model Selection
#
# On this run, **KNN (k=5) achieved 100% accuracy** on the held-out test
# set, while **Logistic Regression achieved 96.67%**, missing one
# *versicolor* sample (misclassified as *virginica*) — visible in its
# confusion matrix and its lower recall on *versicolor* (0.90) in the
# classification report above.
#
# **Declared best model: KNN.** With well-separated, low-dimensional data
# like Iris, a distance-based method like KNN can draw tighter decision
# boundaries around each species cluster than a linear model like Logistic
# Regression, which assumes classes are linearly separable in feature space
# — and *versicolor* vs *virginica* isn't perfectly linear.
#
# That said, this result comes with a caveat worth stating honestly: with
# only 30 test samples, a single flower going either way changes the
# accuracy by ~3.3%. On a dataset this small, "KNN beat Logistic Regression"
# is a real result from this split, but not a strong enough margin to
# declare KNN categorically superior — a different `random_state` in the
# train/test split could easily flip the ranking. For that reason, Logistic
# Regression remains a reasonable production choice despite scoring
# slightly lower here, given its interpretability and constant-time
# prediction cost.

# %% [markdown]
# ## 9. Summary
#
# - The Iris dataset is small, clean, and perfectly balanced (50 samples per
#   species), with no missing values.
# - Petal length and petal width are the most discriminative features;
#   *setosa* is fully separable from the other two species on these alone.
# - KNN (k=5) scored 100% accuracy vs. 96.67% for Logistic Regression on
#   this test split, with the one LR error occurring on the
#   *versicolor*/*virginica* boundary — the genuinely harder distinction in
#   this dataset.
# - Given the small test set (30 samples), this margin should be read as a
#   real but not decisive result. In practice, either model performs
#   strongly here; the choice between them comes down to interpretability
#   and inference-cost tradeoffs as much as raw accuracy.