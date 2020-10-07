import os

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

print(tf.version.VERSION)


class FashionMnist:
    def __init__(self):
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def hook(self):
        self.create_model()
        image_list = self.get_data()
        self.preprocess(image_list[0], image_list[1])


    def get_data(self) -> []:
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

        print(f'훈련 행 {train_images.shape[0]} 열 {train_images.shape[1]}')
        print(f'테스트 행 {test_images.shape[0]} 열 {test_images.shape[1]}')

        plt.figure()
        plt.imshow(train_images[3])
        plt.colorbar()
        plt.grid(False)
        plt.show()

        return [train_images, train_labels, test_images, test_labels]


    

    def preprocess(self, train_images, train_labels):
        plt.figure(figsize=(10,10))
        for i in range(25):
            plt.subplot(5,5,i+1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(class_names[train_labels[i]])
        plt.show()
        


if __name__ == '__main__':
    fashion = FashionMnist()
    fashion.get_data()
    