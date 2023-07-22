# Anomaly Detection - PatchCore

You need a linux server with gpu. Install Docker, NVIDIA Container Toolkit, VSCode and Remote-Containers extension  
  
## Preparing the environement  
1- Get the latest code: ```git clone --branch version01 --single-branch https://github.com/Hamoon1987/my_anomalib.git``` and afterwards ```cd my_anomalib```    
2- Build the docker image: ```docker build . --tag=anomalib```  
3- Run the docker image: ```docker run -it -d --gpus all --name my_anomalib anomalib```  
4- Attach to the running container  
  
## Default run
1- We need normal and abnormal images of the product to train the model. Put the normal, abnormal, and the images you want to check afterwards in ```datasets/<product_name>/normal```, ```datasets/<product_name>/abnormal```, and ```datasets/<product_name>/check``` folders respectively    
2- To trian the model: ```python tools/train.py```  
3- To check the new images: ```python tools/inference/lightning_inference.py```  
Check the results in ```results/patchcore/custom/checkimages```  
4- To evaluate the model: ```python tools/test.py```  
