# Anomaly Detection - PatchCore

You need a linux server with gpu. Install Docker, NVIDIA Container Toolkit, VSCode and Remote-Containers extension  
-- ```git clone --branch version01 --single-branch https://github.com/Hamoon1987/my_anomalib.git``` and afterwards ```cd my_anomalib```    
-- ```docker build . --tag=anomalib```  
-- ```docker run -it -d --gpus all --name my_anomalib anomalib```  
-- Attach to the running container  
-- Put the normal, abnormal, and the images you want to check afterwards in ```datasets/<product_name>/normal```, ```datasets/<product_name>/abnormal```, and ```datasets/<product_name>/check``` folders respectively  
-- Set the config: ```python changeConfig.py --product <product_name> --path ./datasets/<product_name> --model patchcore```
-- To trian the model: ```python tools/train.py --model patchcore```  
-- To check the new images:  
```bash
python tools/inference/lightning_inference.py \
    --model patchcore \
    --weights results/patchcore/<product_name>/run/weights/model.ckpt \
    --input datasets/<product_name>/test/ \
    --output results/patchcore/<product_name>/images
```
-- Check the results in ```results/patchcore/<product_name>/images```  
