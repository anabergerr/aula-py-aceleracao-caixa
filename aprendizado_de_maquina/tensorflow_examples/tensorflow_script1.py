import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

data_training = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [10, 5], [30, 30]])
labels_training = np.array([3, 5, 7, 9, 15, 60])

model = models.Sequential(
    [layers.Dense(64, activation="relu", input_shape=(2,)), layers.Dense(1)]
)

model.compile(
    optimizer="adam", loss="mean_squared_error", metrics=["mean_absolute_error"]
)

model.fit(data_training, labels_training, epochs=1000, verbose=0)

prev = model.predict(np.array([[500, 20]]))
print(prev)  # Deve imprimir algo próximo de 4 (2 + 2)
