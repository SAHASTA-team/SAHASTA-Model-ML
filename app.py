# Import Flask 
from flask import Flask, render_template, request

# Put the code inside app.py
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Define all classes from the existing model
dic = {0 : 'apel',
       1 : 'ayam',
       2 : 'brokoli',
       3 : 'bubur',
       4 : 'jagung',
       5 : 'kacang',
       6 : 'keju',
       7 : 'pisang', 
       8 : 'roti',
       9 : 'susu'}

# Load model 
model = load_model('SAHASTA-Food Exception-92.30.h5')

# Create function to process the inserted image
model.make_predict_function()

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(224,224))
    i = image.img_to_array(i)/255.0
    i = i.reshape(1, 224,224,3)
    # p = model.predict_classes(i) () -> remove in TensorFlow 2.6.
    p = np.argmax(model.predict(i), axis=-1)
    return dic[p[0]]

# Create function to render the static and templates
# routes
@app.route("/", methods=['GET', 'POST'])
def main():
 return render_template("classification.html")

# If click submit button
@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename 
        img.save(img_path)

        p = predict_label(img_path)

    return render_template("classification.html", prediction = p, img_path = img_path)

# Create condition if the app wants to run
if __name__ =='__main__':
 #app.debug = True
 app.run(debug = True)