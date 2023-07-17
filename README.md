# Anomaly Detection - PatchCore

You need a linux server with gpu. Install Docker, NVIDIA Container Toolkit, VSCode and Remote-Containers extension  
  

-- ```git clone --branch version01 --single-branch https://github.com/Hamoon1987/my_anomalib.git``` and afterwards ```cd my_anomalib```    
-- ```docker build . --tag=anomalib```  
-- ```docker run -it -d --gpus all --name my_anomalib anomalib```  
-- Attach to the running container  
-- Put the normal, abnormal, and the images you want to check afterwards in ```datasets/<product_name>/normal```, ```datasets/<product_name>/abnormal```, and ```datasets/<product_name>/check``` folders respectively  
-- Set the training configuration: ```python changeConfig.py --product <product_name> --path ./datasets/<product_name> --model patchcore```  
-- To trian the model: ```python tools/train.py --model patchcore```  
-- To check the new images: ```python tools/inference/lightning_inference.py -h```  
As an example:  
```python tools/inference/lightning_inference.py --model patchcore --weights results/patchcore/cable/run/weights/lightning/model.ckpt --input datasets/cable/check/ --output results/patchcore/cable/checkimages```
-- Check the results in ```results/patchcore/cable/checkimages```  
