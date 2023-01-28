import logging.config
import yaml


def setup_logging(cfg_file_path: str) -> None:
    with open(cfg_file_path, "r") as fin:
        logging.config.dictConfig(yaml.safe_load(fin))
