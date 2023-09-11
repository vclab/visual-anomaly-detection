import yaml
from argparse import ArgumentParser

def get_parser() -> ArgumentParser:
    """Get parser.

    Returns:
        ArgumentParser: The parser object.
    """
    parser = ArgumentParser()
    parser.add_argument("--model", required=True, type=str, help="Name of the algorithm to train/test")
    parser.add_argument("--product", required=False, type=str, default='custom', help="product name")
    parser.add_argument("--path", required=False, type=str, default='datasets/custom', help="Path to the images")
    parser.add_argument("--tag", required=True, type=str, help="Tag name")

    return parser

def changeconfig(args):
    config_path = "src/anomalib/models/" + args.model + "/config.yaml"
    with open(config_path) as f:
        list_doc = yaml.safe_load(f)
    list_doc["dataset"]['name'] = args.product
    list_doc["dataset"]['path'] = args.path
    list_doc["dataset"]['tag'] = args.tag
    list_doc["dataset"]['model'] = args.model
    list_doc['dataset']['input'] = args.path  # + "/check/"
    list_doc['dataset']['output'] = "results/" + args.model + '/' + args.product + "/checkimages"
    list_doc['dataset']['weights'] = "results/" + args.model + '/' + args.product + "/run/weights/lightning/model.ckpt"
    
    config_path = "my_configs/" + args.tag +".yaml"
    with open(config_path, "w") as f:
        yaml.dump(list_doc, f)


if __name__ == "__main__":
    args = get_parser().parse_args()
    changeconfig(args)