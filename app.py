from distutils import file_util
import functools
import json
import os

import flask

from authlib.integrations.requests_client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
import tempfile

import drive_google_auth
import drive_google



app = flask.Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(drive_google_auth.app)
app.register_blueprint(drive_google.app)



@app.route('/')
def index():
    try:
        if drive_google_auth.is_logged_in():
            user_info = drive_google_auth.get_user_info()
            return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

        return 'You are not currently logged in.'
    except KeyError:
        return 'You are not currently logged in.' 

@app.route('/list-files', methods=['GET'])
def list_drive_file():
    files_dict = {}
    files = drive_google.build_drive_api_v3().files().list(pageSize=20, orderBy="folder", q='trashed=false').execute().get('files', [])
    for file in files:
        files_dict.update({file['name']: file['mimeType']})
    return json.dumps(files_dict)

@app.route('/create-folder', methods=['POST', 'GET'])
def create_drive_folder():
    folder_name = flask.request.args.get('folder-name')
    folder
    file_metadata = {
    'name': folder_name,
    'mimeType': 'application/vnd.google -apps.folder'
    } #todo configure True and false query parameters for ability to be able to create folders in folders
    id = drive_google.build_drive_api_v3().files().create(body=file_metadata, fields='id').execute()
    return id if id != None else 'Folder couldnt be created'

@app.route('/upload-files', methods=['POST'])
def upload_file():

    if flask.request.method == 'POST':
        file_to_upload = flask.request.files.get('file')
        print(flask.request.files)
        print(file_to_upload)
        if (not file_to_upload):
            return 'File not given'
        
    filename = secure_filename(file_to_upload.filename)

    fp = tempfile.TemporaryFile()
    ch = file_to_upload.read()
    fp.write(ch)
    fp.seek(0)

    mime_type = flask.request.headers['Content-Type']
    drive_google.save_file(filename, mime_type, fp)
    folder_id = flask.request.args.get('folder-id')
    