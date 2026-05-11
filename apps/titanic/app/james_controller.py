from fastapi import FastAPI

from titanic.app.jack_service import JackService


app = FastAPI(title="Titanic (James)")


class JamesController:
    def __init__(self) -> None:
        self.service = JackService()

    def get_data(self):
        return self.service.walter.get_data()

    def get_count(self):
        return self.service.walter.get_count()

    def has_decision_tree_model(self) -> bool:
        return self.service.rose.model is not None

    def get_model_name_and_accuracy(self):
        return self.service.get_model_name_and_accuracy()
