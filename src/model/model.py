import logging
from pathlib import Path
import yaml
import whisper
import torch


def get_engine(model_config):
    """
    Функция чтения модели и инициализации весов
    :param: model_config: Path
    :return: ASR-модель
    """
    try:
        with open(model_config, 'r') as fin:
            model_params = yaml.safe_load(fin.read())
            weight = model_params['model']
            device = model_params['device']
        model = whisper.load_model(weight, device=f'cuda:{device}' if torch.cuda.is_available() else 'cpu')
        logging.info("speech_recognition_model uploaded successfully")
    except Exception as e:
        logging.critical(f"Failed to load model. {e}")
    return model
