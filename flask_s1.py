from flask import Flask, request, send_file, redirect, url_for
import os
from werkzeug.utils import secure_filename
import uuid

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return '''
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    <form action="/download" method="get">
        <select name="filename">
            {}
        </select>
        <input type="submit" value="Download">
    </form>
    '''.format(''.join(['<option value="{}">{}</option>'.format(f, f) for f in os.listdir(UPLOAD_FOLDER)]))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    filename = secure_filename(file.filename)
    for i in range(1000000):
        pass
    filename = str(uuid.uuid4()) + '_' + filename  # Rename to avoid overwriting
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'File uploaded successfully using port 5000'

@app.route('/download')
def download_file():
    filename = request.args.get('filename')
    if filename:
        print(f"file: {filename} is downloaded from port 5000")
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)
    else:
        return 'No file selected for download'

@app.route('/download_complete')
def download_complete():
    return 'File downloaded using port 5000'

if __name__ == '__main__':
    app.run(port=5000)
