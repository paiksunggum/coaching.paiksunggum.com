from titanic.app.jack_service import JackService


class JamesController:
    def __init__(self):
        self.jack = JackService()

    def get_model_name_and_accuracy(self):
        return self.service.get_model_name_and_accuracy()

    def get_data(self):
        return self.jack.get_data()

    def get_count(self):
        return self.jack.get_count()

    def get_survived_count(self):
        return self.jack.get_survived_count()

    def get_dead_count(self):
        return self.jack.get_dead_count()

    def has_decision_tree_model(self) -> bool:
        return self.jack.has_decision_tree_model()

    def get_model_info(self):
        return self.jack.get_model_info()
