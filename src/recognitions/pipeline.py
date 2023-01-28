from typing import Dict
import logging
from pathlib import Path

from src.model.model import get_engine


MODEL_CONFIG_PATH = Path("./configs/whisper_model_cfg.yml")


class TextRecognition:
    """
    Класс для распознавания речи в текст
    """

    def __init__(self):
        """
        Инициализация ASR-модели и экземпляра класса по текстовой обработке
        """
        self.model = get_engine(MODEL_CONFIG_PATH)

    def recognition(self, audio_path):
        """
        Метод по распознаванию речи в текст
        :param: audio_path: Path
        :return: словарь с результатом распознавания: Dict
        """
        try:
            model_output = self.model.transcribe(audio_path, language='Russian' , temperature=0)
            text_output = model_output["text"]
            result = {
                      "text_recognized": text_output,
                      }
            return result
        except Exception as e:
            logging.error(f'Failed to recognize speech. Cause: {e}')

    def __call__(self, audio_path: Path) -> Dict:
        return self.recognition(audio_path)
