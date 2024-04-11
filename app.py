import idx2numpy
import numpy as np
from flask import Flask, send_file, render_template
from PIL import Image
import io
import random

app = Flask(__name__)

# MNISTデータを読み込む
images_file = 'data/train-images-idx3-ubyte'
labels_file = 'data/train-labels-idx1-ubyte'

images = idx2numpy.convert_from_file(images_file)
labels = idx2numpy.convert_from_file(labels_file)

@app.route('/mnist/<int:digit>')
def mnist_image(digit):
    # 与えられた数字に対応する全ての画像のインデックスを取得
    indices = np.where(labels == digit)[0]
    # ランダムにインデックスを選択
    random_index = random.choice(indices)
    image = Image.fromarray(images[random_index])

    # メモリ内に画像を保存し、それを送信する
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return send_file(img_byte_arr, mimetype='image/png')

@app.route('/')
def show_time():
    return render_template('time.html')

if __name__ == '__main__':
    app.run()
