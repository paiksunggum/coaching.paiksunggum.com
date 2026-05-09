from fastapi import FastAPI
import pandas as pd
from pathlib import Path
from titanic.app.walter import Walter



app = FastAPI(title="titanic (james)")



class James:
    def __init__(self):
        pass


    def get_data(self):
        w = Walter()
        return w.get_data()

