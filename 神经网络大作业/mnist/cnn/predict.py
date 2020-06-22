import tensorflow as tf
from PIL import Image
import numpy as np

from train import CNN




class Predict(object):
    def __init__(self):
        latest = tf.train.latest_checkpoint('./ckpt')
        self.cnn = CNN()
        # 恢复权重
        self.cnn.model.load_weights(latest)

    def predict(self, image_path):
        # 以黑白读取
        img = Image.open(image_path).convert('L')
        flatten_img = np.reshape(img, (28, 28, 1))
        x = np.array([1 - flatten_img])

       
        y = self.cnn.model.predict(x)

        # 因为x只传入了一张图片，取y[0]
        # np.argmax()取得最大值下标
        print(image_path)
        print(y[0])
        print('        -> Predict digit', np.argmax(y[0]))


if __name__ == "__main__":
    app = Predict()
    app.predict('../images/4.png')
    app.predict('../images/5.png')
    app.predict('../images/1.png')
