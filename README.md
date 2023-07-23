# Anomaly Detection - PatchCore

You need a linux server with gpu. Install Docker, NVIDIA Container Toolkit, VSCode and Remote-Containers extension  
  
## Preparing the environement  
1- Get the latest code: ```git clone --branch version01 --single-branch https://github.com/Hamoon1987/my_anomalib.git``` and afterwards ```cd my_anomalib```    
2- Build the docker image: ```docker build . --tag=anomalib```  
3- Run the docker image: ```docker run -it -d --gpus all --name my_anomalib anomalib```  
4- Attach to the running container  
  
## Default run
1- We need normal and abnormal images of the product to train the model. Put the normal, abnormal, and the images you want to check afterwards in ```datasets/custom/normal```, ```datasets/custom/abnormal```, and ```datasets/custom/check``` folders respectively    
2- To trian the model: ```python tools/train.py```  
3- To check the new images: ```python tools/inference/lightning_inference.py```  
Check the results in ```results/patchcore/custom/checkimages```  
4- To evaluate the model: ```python tools/test.py```  
## Basic run
1- Put the normal, abnormal, and the images you want to check afterwards in ```datasets/<product_name>/normal```, ```datasets/<product_name>/abnormal```, and ```datasets/<product_name>/check``` folders respectively   
Example: ```datasets/cable/normal```, ```datasets/cable/abnormal```, and ```datasets/cable/check```  
2- Set the training configuration: ```python changeConfig.py --product <product_name> --path ./datasets/<product_name> --model <model_name>  --tag <tag_name>```  
Example: ```python changeConfig.py --product cable --path ./datasets/cable --model patchcore  --tag patchcore_cable_v01```  
3- To trian the model: ```python tools/train.py --tag <tag>```  
Example: ```python tools/train.py --tag patchcore_cable_v01```  
4- To check the new images: ```python tools/inference/lightning_inference.py --tag <tag_name>```  
Example: ```python tools/inference/lightning_inference.py --tag patchcore_cable_v01```  
Check the results in ```results/patchcore/custom/checkimages```  
5- To evaluate the model: ```python tools/test.py --tag <tag_name>``` 
Example:  ```python tools/test.py --tag patchcore_cable_v01```  

