# Project 2: Data Classification Using AI (Iris Dataset + KNN)

# 1. INPUT: Load dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score

data = load_iris()
X = data.data          # features: sepal/petal length & width
y = data.target        # classes: setosa, versicolor, virginica

# 2. Understand the dataset
print("Samples:", X.shape[0])
print("Features:", X.shape[1])
print("Classes:", data.target_names)

# 3. PROCESS: Split into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

# 4. Scale features (StandardScaler: mean=0, variance=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Apply classification algorithm: K-Nearest Neighbors
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)                # FIT: memorize the map
predictions = model.predict(X_test)        # PREDICT: apply logic

# 6. OUTPUT: Validate results
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions, target_names=data.target_names))
print("F1 Score (weighted):", f1_score(y_test, predictions, average='weighted'))