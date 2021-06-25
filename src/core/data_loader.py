import numpy as np
import pandas as pd

from src.config import Constants
from src.utils import paths


class LoadData:

    def __init__(self, path=paths(Constants.DATA_PATH, "essays.csv")):
        self.labels = ['cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN']
        self.y_essays = self.data_essays[['cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN']]
        self.X_essays = self.data_essays['TEXT'].tolist()
        self.data_essays = pd.read_csv(self.path, encoding="ISO-8859-1")
        self.path = path

    def run(self):
        self.data_essays['cEXT'] = np.where(self.data_essays['cEXT'] == 'y', 1, 0)
        self.data_essays['cNEU'] = np.where(self.data_essays['cNEU'] == 'y', 1, 0)
        self.data_essays['cAGR'] = np.where(self.data_essays['cAGR'] == 'y', 1, 0)
        self.data_essays['cCON'] = np.where(self.data_essays['cCON'] == 'y', 1, 0)
        self.data_essays['cOPN'] = np.where(self.data_essays['cOPN'] == 'y', 1, 0)
        return self.data_essays, self.X_essays, self.y_essays, self.labels
