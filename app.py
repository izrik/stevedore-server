import os

from flask import Flask, request

app = Flask(__name__)

storage_path = os.path.join(os.getcwd(), 'instance', 'storage')


def copy_stream_to_file(stream, f, chunk_size=4096):
    while True:
        chunk = stream.read(chunk_size)
        if not chunk:
            break
        f.write(chunk)


@app.route('/')
def index():
    return 'stevedore-server'


@app.route('/files/<path:path>', methods=['PUT'])
def files(path):
    fullpath = os.path.join(storage_path, path)
    os.makedirs(os.path.dirname(fullpath))
    with open(fullpath, 'wb') as f:
        copy_stream_to_file(request.stream, f)
    return '✔︎', 201


app.run(debug=True, host='localhost', port=8080)
