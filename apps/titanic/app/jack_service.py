from titanic.app.walter_reader import WalterReader
from titanic.app.rose_model import RoseModel


class JackService:
    def __init__(self):
        self.rose = RoseModel()
        self.walter = WalterReader()

    def get_data(self):
        return self.walter.get_data()

    def get_count(self):
        return self.walter.get_count()

    def get_survived_count(self):
        return self.walter.get_survived_count()

    def get_dead_count(self):
        return self.walter.get_dead_count()

    def has_decision_tree_model(self) -> bool:
        return self.rose.decision_tree is not None

    def get_model_info(self):
        return {"model": self.rose.model_name, "accuracy": self.rose.get_accuracy()}