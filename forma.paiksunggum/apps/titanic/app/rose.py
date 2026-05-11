from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "titanic_decision_tree.joblib"
DECISION_TREE_MODEL_PATH = _MODEL_PATH


class Rose:
    def __init__(self):
        pass

    def save_model(self, path=None):
        """Titanic CSV로 결정 트리를 학습하고 joblib 파일로 저장한다."""
        df = pd.read_csv(_CSV_PATH)
        drop_cols = ["Survived", "PassengerId", "Name", "Ticket", "Cabin"]
        X = df.drop(columns=[c for c in drop_cols if c in df.columns])
        y = df["Survived"]

        numeric = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
        categorical = ["Sex", "Embarked"]

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", SimpleImputer(strategy="median"), numeric),
                (
                    "cat",
                    Pipeline(
                        steps=[
                            ("impute", SimpleImputer(strategy="most_frequent")),
                            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                        ]
                    ),
                    categorical,
                ),
            ]
        )

        model = Pipeline(
            steps=[
                ("prep", preprocessor),
                ("clf", DecisionTreeClassifier(random_state=42, max_depth=5)),
            ]
        )
        model.fit(X, y)

        out = Path(path) if path else _MODEL_PATH
        joblib.dump(model, out)
        return str(out.resolve())


if __name__ == "__main__":
    r = Rose()
    saved = r.save_model()
    print(saved)
