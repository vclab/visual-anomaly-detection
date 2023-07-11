# Anomaly Detection - PatchCore

1- ```git clone https://github.com/Hamoon1987/my_anomalib.git``` and afterwards ```cd my_anomalib```    
2- ```docker build . --tag=anomalib```  
3- ```docker run -it -d --gpus all --name my_anomalib anomalib```  
4- Attach to the running container  
5- Put the normal, abnormal, and test images in ```dataset/custom/normal```, ```dataset/custom/abnormal```, and ```dataset/custom/check``` folders  
6- To trian the model: ```python tools/train.py --model patchcore```  
7- To check the new images: ```python tools/inference/lightning_inference.py```  
8- Check the results in ```results/patchcore/custom/images```  
