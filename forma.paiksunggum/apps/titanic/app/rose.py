import pickle
import pandas as pd
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "titanic_model.pkl"

class Rose:
    def __init__(self):
        pass

    def train_and_save(self):
        df = pd.read_csv(_CSV_PATH)
        
        df = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Survived"]].dropna()
        df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
        
        X = df.drop("Survived", axis=1)
        y = df["Survived"]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)
        
        with open(_MODEL_PATH, "wb") as f:
            pickle.dump(model, f)
        
        accuracy = model.score(X_test, y_test)
        return {"message": "모델 저장 완료", "accuracy": round(accuracy, 4), "model_path": str(_MODEL_PATH)}

    def load_model(self):
        with open(_MODEL_PATH, "rb") as f:
            return pickle.load(f)s