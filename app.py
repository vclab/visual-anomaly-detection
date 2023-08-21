# app.py
import subprocess
from flask import Flask, render_template, request, send_from_directory, send_file
import os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dropdown_options = ['patchCore_cable', 'patchCore_bottle', 'patchCore_oilCap']

    if request.method == 'POST':
        selected_option = request.form['dropdown']
        path = execute_command_for_option(selected_option)
        images = os.listdir("media/" + path)
        return render_template('index.html', dropdown_options=dropdown_options, path = path, images=images)
    
    return render_template('index.html', dropdown_options=dropdown_options)

def execute_command_for_option(option):
    # Build the command string
    command = f"python tools/inference/lightning_inference.py --tag {option}"

    # try:
    #     subprocess.run(command, shell=True, check=True)
    # except subprocess.CalledProcessError as e:
    #     print(f"Error executing the command: {e}")

    path = f"{option}"
    return path

@app.route('/media/<path:filename>')
def serve_image(filename):  
    images_directory = os.path.join(os.getcwd(), 'media')
    return send_file(os.path.join(images_directory, filename))


if __name__ == '__main__':
    app.run(debug=True)
