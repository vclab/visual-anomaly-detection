# Anomaly Detection - PatchCore

1- ```git clone https://github.com/Hamoon1987/my_anomalib.git```  
2- ```cd my_anomalib```  
3- ```docker build . --tag=anomalib```  
4- ```docker run -it -d --gpus all --name my_anomalib anomalib```  
5- Attach to the running container  
6- Put the normal, abnormal, and test images in ```dataset/custom/normal```, ```dataset/custom/abnormal```, and ```dataset/custom/check``` folders.  
7- ```python tools/train.py --model patchcore```  
8- ```python tools/inference/lightning_inference.py```  
9- Check the results in ```results/patchcore/custom/imagescd```  
