import shutil
import os

# Local folder path (change this to the path of your local folder)
local_folder_path = 'C:/Users/100844431/Master/AxiomInternship/Newfolder'

# Server destination path (change this to the path on the server)
server_destination = 'media/'

# Copy files from local folder to server
for filename in os.listdir(local_folder_path):
    source_file = os.path.join(local_folder_path, filename)
    destination_file = os.path.join(server_destination, filename)
    shutil.copy(source_file, destination_file)
