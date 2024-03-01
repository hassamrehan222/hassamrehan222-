from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import cv2
import os
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def processimage(filename, operation):
    print(f"the operation is {operation}  and filename is {filename}")
    img  = cv2.imread(f"uploads/{filename}")
    match operation:
        case  "cgray":
            imgprocessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"static/{filename}",imgprocessed)
    pass


@app.route('/')
def home():

    return render_template("index.html")

@app.route('/About')
def about():

    return render_template("about.html")

@app.route('/edit', methods=["GET", "POST"])
def edit():
   if request.method == "POST":
       operation = request.form.get("operation")

       if 'file' not in request.files:
           flash('No file part')
           return "error"
       file = request.files['file']
       # If the user does not select a file, the browser submits an
       # empty file without a filename.
       if file.filename == '':
           flash('No selected file')
           return "error no selected file"
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

           processimage(filename, operation)
           flash(f"your image has been processed and available <a href='/static/{filename}'>here</a>")
           return render_template("index.html")

       return render_template("index.html")


app.run(debug = True)
