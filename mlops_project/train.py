from __future__ import annotations

import pickle
from pathlib import Path

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_and_evaluate() -> tuple[float, LogisticRegression]:
    """Create a small classification dataset and train a basic model."""
    X, y = make_classification(
        n_samples=500,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        n_classes=2,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy, model


def main() -> None:
    accuracy, model = train_and_evaluate()

    output_dir = Path("artifacts")
    output_dir.mkdir(exist_ok=True)

    model_path = output_dir / "model.pkl"
    with model_path.open("wb") as file:
        pickle.dump(model, file)

    print(f"Model accuracy: {accuracy:.4f}")
    print(f"Model saved to: {model_path}")


if __name__ == "__main__":
    main()
