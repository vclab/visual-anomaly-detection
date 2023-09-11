# app.py
import subprocess
from flask import Flask, render_template, request, send_from_directory, send_file, session
import os
import shutil

app = Flask(__name__)
app.secret_key = '184174562bf2be3fc810beeaa41ac1140d3ecc3565d5269f'


@app.route('/')
def home():
    dropdown_options = os.listdir("my_configs/")
    dropdown_options.remove('patchcore_custom.yaml')
    dropdown_options = [i[:-5] for i in dropdown_options]

    return render_template('home.html', dropdown_options = dropdown_options)




@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        tag = request.form['dropdown']
        path = get_path(tag)
        product = get_product(tag)
        session['tag'] = tag
        session['product'] = product
    return render_template('secondPage.html', tag=tag, path = path)

    

@app.route('/submit_address', methods=['POST'])
def submit_address():
    # if 'submit' in request.form:
    address = request.form['address']
    tag = session.get('tag')
    product = session.get('product')
    # Do something with the submitted address, e.g., process it or save it
    change_address(product, address, tag)
    inference(tag)
    results_path = get_results(product, address)
    images = os.listdir(results_path)
    
    # elif 'upload' in request.form:
    #     address = request.form['address']
    #     # address = "C:/Users/100844431/Master/AxiomInternship/Newfolder"
    #     if os.path.exists(address) and os.path.isdir(address):
    #         # Define the destination folder on the server where you want to copy files
    #         server_destination = 'media/'

    #         # Copy files from the user's local folder to the server
    #         for filename in os.listdir(address):
    #             print(filename)
    #             source_file = os.path.join(address, filename)
    #             destination_file = os.path.join(server_destination, filename)
    #             shutil.copy(source_file, destination_file)
            
    #         # Process the uploaded image as needed
    #     return "uploaded"
    return render_template('thirdPage.html', address = address, images=images, tag=tag, results_path=results_path)

def change_address(product, address, tag):

    command = f"python changeConfig.py --product {product} --path {address} --model patchcore  --tag {tag}"
    print(command)
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {e}")

def inference(tag):
    command = f"python tools/inference/lightning_inference.py --tag {tag}"

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {e}")

def get_path(option):

    option = option.split('_', 1)
    option = option[1]
    path = f"datasets/{option}/check/"
    return path

def get_product(option):
    option = option.split('_', 1)
    product = option[1]
    return product

def get_results(product, address):
    tmp = address.split('/', -1)
    folder = tmp[-2]
    path = f"results/patchcore/{product}/checkimages/" + folder + "/"
    return path


@app.route('/upload_folder', methods=['POST'])
def upload_folder():
    uploaded_files = request.files.getlist('folder_path')
    product = session.get('product')
    if not os.path.exists("media/"+ product):
        os.makedirs("media/"+ product)

    for uploaded_file in uploaded_files:
        if uploaded_file.filename != '':
            # Define the destination folder on the server where you want to save the uploaded files
            server_destination = 'media/'+ product + '/'

            # Save each uploaded file to the server
            destination_file = os.path.join(server_destination, uploaded_file.filename)
            uploaded_file.save(destination_file)

            # You can add additional processing for each uploaded file here
    tag = session.get('tag')
    product = session.get('product')
    # Do something with the submitted address, e.g., process it or save it
    address = 'media/' + product + '/'
    change_address(product, address, tag)
    inference(tag)
    results_path = get_results(product, address)
    images = os.listdir(results_path)
    # You can add a response indicating that all files were uploaded successfully
    return render_template('thirdPage.html', address = address, images=images, tag=tag, results_path=results_path)




@app.route('/<path:filename>')
def serve_image(filename):  
    images_directory = os.getcwd()
    return send_file(os.path.join(images_directory, filename))


if __name__ == '__main__':
    app.run(debug=True)
