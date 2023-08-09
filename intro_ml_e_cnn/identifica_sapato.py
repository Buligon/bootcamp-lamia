import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Forma, tamanho da imagem
    keras.layers.Dense(128, activation=tf.nn.relu),
    # qtde de itens de diferentes roupas representados nos dados
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(
    optimizer=tf.optimizers.Adam(),  # gera novos parâmetros para as funcs
    loss='sparse_categorical_crossentropy'  # mede quão bons foram os resultados
    )

model.fit(train_images, train_labels, epochs=5)

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[0])
print(test_labels[0])
