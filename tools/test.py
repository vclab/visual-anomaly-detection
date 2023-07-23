"""Test This script performs inference on the test dataset and saves the output visualizations into a directory."""

# Copyright (C) 2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser, Namespace
import yaml
from pytorch_lightning import Trainer, seed_everything

from anomalib.config import get_configurable_parameters
from anomalib.data import get_datamodule
from anomalib.models import get_model
from anomalib.utils.callbacks import get_callbacks


def get_parser() -> ArgumentParser:
    """Get parser.

    Returns:
        ArgumentParser: The parser object.
    """
    parser = ArgumentParser()
    parser.add_argument("--tag", type=str, required=False, default="patchcore_custom", help="Tag name")
    # parser.add_argument("--model", type=str, required=False, default="patchcore", help="Name of the algorithm to train/test")
    # parser.add_argument("--config", type=str, required=False, default="src/anomalib/models/patchcore/config.yaml", help="Path to a model config file")
    # parser.add_argument("--weight_file", type=str, required=False, default= "results/patchcore/custom/run/weights/lightning/model.ckpt")

    return parser


def test(args: Namespace):
    """Test an anomaly model.

    Args:
        args (Namespace): The arguments from the command line.
    """
    config_path = "my_configs/" + args.tag +".yaml"
    with open(config_path) as f:
        list_doc = yaml.safe_load(f)

    config = get_configurable_parameters(
        model_name=list_doc["dataset"]['model'],
        config_path=config_path,
        weight_file=list_doc["dataset"]['weights'],
    )

    if config.project.seed:
        seed_everything(config.project.seed)

    datamodule = get_datamodule(config)
    model = get_model(config)

    callbacks = get_callbacks(config)

    trainer = Trainer(callbacks=callbacks, **config.trainer)
    trainer.test(model=model, datamodule=datamodule)


if __name__ == "__main__":
    args = get_parser().parse_args()
    test(args)
