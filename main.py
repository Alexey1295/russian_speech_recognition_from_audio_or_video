import logging
import yaml
import argparse

from src.logging.utils import setup_logging
from src.recognitions.pipeline import TextRecognition
from src.data.loaders import AudioLoader


LOG_CONFIG = "./configs/logging.cfg.yml"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--content_type', required=True)
    parser.add_argument('--content_path', required=True)
    args = parser.parse_args()
    recognition = TextRecognition()
    try:
        if args.content_type == 'audiofile':
            result = recognition(audio_path=args.content_path)
        if args.content_type == 'videofile':
            loader = AudioLoader()
            audio_path = loader.get_audio_from_video(video_path=args.content_path)
            result = recognition(audio_path=audio_path)
            loader.delete_file(file_path=audio_path)
        if args.content_type == 'vk_video':
            loader = AudioLoader()
            audio_path = loader.get_audio_from_link_vk_video(vk_video_path=args.content_path)
            result = recognition(audio_path=audio_path)    
            loader.delete_file(file_path=audio_path)
        result['content_type'] = args.content_type
        result['content_path'] = args.content_path
        logging.debug(f'Result recognized: {result}')
    except Exception as e:
        logging.error(f'such content_type is set incorrectly, error: {e}')


if __name__ == "__main__":
    setup_logging(LOG_CONFIG)
    main()
