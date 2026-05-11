from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import joblib

DECISION_TREE_MODEL_PATH = Path(__file__).resolve().parent / "titanic_decision_tree.joblib"


class RoseModel:
    def __init__(self, model_path: Path = DECISION_TREE_MODEL_PATH):
        self.model_path = model_path
        self.decision_tree: Optional[Any] = joblib.load(model_path) if model_path.is_file() else None
        if self.decision_tree is None:
            self.model_name = "unloaded"
            return

        model = self.decision_tree.steps[-1][1] if hasattr(self.decision_tree, "steps") else self.decision_tree
        self.model_name = model.__class__.__name__

    def get_accuracy(self):
        if self.decision_tree is None:
            return None
        import pandas as pd
        df = pd.read_csv(self.model_path.parent / "Titanic-Dataset.csv")
        X = df.drop(columns=["Survived"])
        y = df["Survived"]
        return float(self.decision_tree.score(X, y))