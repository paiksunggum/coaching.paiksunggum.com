from fastapi import FastAPI

from titanic.app.rose import DECISION_TREE_MODEL_PATH
from titanic.app.walter import Walter


app = FastAPI(title="titanic (james)")


class James:
    def __init__(self):
        pass


    def get_data(self):
        w = Walter()
        return w.get_data()

    def get_count(self):
        w = Walter()
        return w.get_count()

    def get_survived_count(self):
        w = Walter()
        return w.get_survived_count()

    def get_dead_count(self):
        w = Walter()
        return w.get_dead_count()

    def has_decision_tree_model(self) -> bool:
        """Rose.save_model() 기본 경로에 결정 트리 joblib가 있는지 판단한다."""
        return DECISION_TREE_MODEL_PATH.is_file()