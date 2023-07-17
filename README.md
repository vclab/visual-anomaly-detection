# Anomaly Detection - PatchCore

You need a linux server with gpu. Install Docker, NVIDIA Container Toolkit, VSCode and Remote-Containers extension  
1- ```git clone https://github.com/Hamoon1987/my_anomalib.git``` and afterwards ```cd my_anomalib```    
2- ```docker build . --tag=anomalib```  
3- ```docker run -it -d --gpus all --name my_anomalib anomalib```  
4- Attach to the running container  
5- Put the normal, abnormal, and the images you want to check afterwards in ```datasets/<product_name>/normal```, ```datasets/<product_name>/abnormal```, and ```datasets/<product_name>/check``` folders respectively  
6- Set the config: ```python changeConfig.py --product <product_name> --path ./datasets/<product_name> --model patchcore```
6- To trian the model: ```python tools/train.py --model patchcore```  
7- To check the new images: ```python tools/inference/lightning_inference.py```  
8- Check the results in ```results/patchcore/custom/images```  
