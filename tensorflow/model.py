import tensorflow as tf
import pandas as pd
import numpy as np

# region CONSTANTS

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']


# endregion
def load_data():
    # Full data set load.
    _data = pd.read_csv("iris.data", header=None)
    assert _data.shape[0] == 5
    _data.columns = CSV_COLUMN_NAMES

    return


if __name__ == '__main__':
    pass
