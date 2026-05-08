from fastapi import FastAPI

from titanic.app.walter import Walter


app = FastAPI(title="Titanic (James)")


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