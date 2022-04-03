from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename

import s3_client
import media_converter_client


app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


CURRENT_FILE = ''

# TODO: validate max size = 1024 * 1024 * 100, validate .extensions


@app.route("/")
def main_page():
    return render_template('index.html')


@app.route('/upload', methods=['post'])
def upload():

    if request.method == 'POST':
        img = request.files['file']
        if img:
            filename = secure_filename(img.filename)
            img.save(filename)

            s3_client.upload_file(filename)

            global CURRENT_FILE
            CURRENT_FILE = filename

            return render_template("index.html",
                                   status_color_upload='success',
                                   msg_upload='File upload success')

        else:
            return render_template("index.html",
                                   status_color_upload='error',
                                   msg_upload='No file chosen')


@app.route('/create_job', methods=['post'])
def create_job():

    if CURRENT_FILE == '':
        return render_template("index.html", msg_no_file='Upload the file first')
    else:
        cut_start = int(request.form['cut_start'])
        cut_end = int(request.form['cut_end'])

        # TODO: if cut_end - cut_start < 1 UI error, if cut_end - cut_start < 20 sec UI warning

        if cut_start < 10:
            cut_start = '0{}'.format(cut_start)
        if cut_end < 10:
            cut_end = '0{}'.format(cut_end)

        media_converter_client.create_job(CURRENT_FILE, cut_start, cut_end)
        return render_template("index.html", msg_job='Job sent')


@app.route('/download', methods=['post'])
def download():
    if CURRENT_FILE == '':
        return render_template("index.html",
                               status_color_download='error',
                               msg_download='File was not chosen')
    else:
        s3_client.download_file(CURRENT_FILE)
        return render_template("index.html",
                               status_color_download='success',
                               msg_download='Downloading')
