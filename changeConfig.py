import yaml
from argparse import ArgumentParser

def get_parser() -> ArgumentParser:
    """Get parser.

    Returns:
        ArgumentParser: The parser object.
    """
    parser = ArgumentParser()
    parser.add_argument("--model", required=True, type=str, default="padim", help="Name of the algorithm to train/test")
    parser.add_argument("--product", required=True, type=str, default="INFO", help="product name")
    parser.add_argument("--path", required=True, type=str, default="INFO", help="Path to the images")

    return parser

def changeconfig(args):
    config_path = "src/anomalib/models/" + args.model + "/config.yaml"
    with open(config_path) as f:
        list_doc = yaml.safe_load(f)
    list_doc["dataset"]['name'] = args.product
    list_doc["dataset"]['path'] = args.path

    with open("src/anomalib/models/patchcore/config.yaml", "w") as f:
        yaml.dump(list_doc, f)


if __name__ == "__main__":
    args = get_parser().parse_args()
    changeconfig(args)