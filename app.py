# app.py
import subprocess
from flask import Flask, render_template, request, send_from_directory, send_file
import os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dropdown_options = os.listdir("my_configs/")
    dropdown_options.remove('patchcore_custom.yaml')
    dropdown_options = [i[:-5] for i in dropdown_options]
    # dropdown_options = ['patchCore_cable', 'patchCore_bottle', 'patchCore_oilCap']

    if request.method == 'POST':
        print("hello")
        selected_option = request.form['dropdown']
        path = execute_command(selected_option)
        images = os.listdir(path)
        return render_template('index.html', dropdown_options=dropdown_options, path = path, images=images)
    
    return render_template('index.html', dropdown_options=dropdown_options)

def execute_command(option):
    # Build the command string
    command = f"python tools/inference/lightning_inference.py --tag {option}"

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {e}")
    option = option.split('_', 1)
    option = option[1]
    path = f"results/patchcore/{option}/checkimages/check/"
    return path

@app.route('/<path:filename>')
def serve_image(filename):  
    # images_directory = os.path.join(os.getcwd(), 'media')
    images_directory = os.getcwd()
    return send_file(os.path.join(images_directory, filename))


if __name__ == '__main__':
    app.run(debug=True)
