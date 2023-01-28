import logging
import os
import regex as re
from pathlib import Path
import requests
import time
import ffmpeg
from bs4 import BeautifulSoup as BS
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip


class AudioLoader:

    def __init__(self):
        """
        Класс для сохранения и удаления аудиофайлов
        """
        self.ydl_opts = {"external_downloader": "ffmpeg",
                         "noplaylist": True,
                         "quiet": True,
                         "format": "bestaudio/best",
                         "postprocessors": [{'key': 'FFmpegExtractAudio',
                                             'preferredcodec': 'mp3',
                                             'preferredquality': '192',
                                             }
                                            ],
                         }

    def get_audio_from_link_vk_video(self, vk_video_path):
        """
        Получение аудио из видео по ссылке из vk.com
        :param vk_video_path:str
        :return: audio_path: str
        """
        t0 = time.time()
        result = re.search('video-?[0-9]+_[0-9]+', vk_video_path).group(0)
        owner_id = result[result.find('video') + 5:result.find('_')]
        video_id = result[result.find('_') + 1:]
        oid = re.search(r"video[^_]*", vk_video_path).group(0).replace('video', '')
        vid_id = re.search(r"_.*", vk_video_path).group(0).replace('_', '')
        r = requests.get(vk_video_path, verify=True)
        soup = str(BS(r.text, features="html.parser"))
        try:
            vid_hash = re.search(r"hash.*\"\sitemprop", soup).group(0).\
            replace('itemprop', '').replace('hash=', '').replace('\" ', '')
            url_for_parse = f'https://vk.com/video_ext.php?oid={oid}&id={vid_id}&hash={vid_hash}'
        except:
            url_for_parse = f'https://vk.com/video_ext.php?oid={oid}&id={vid_id}'
        url = url_for_parse
        file_path = f'video-{owner_id}_{video_id}.mp3'
        try:
            self.ydl_opts['outtmpl'] = file_path
            with YoutubeDL(self.ydl_opts) as ydl:
                ydl.download(url)
            logging.debug(f'The audio upload process is completed in {time.time()-t0} s')
        except Exception as e:
            logging.debug(f'Error loading audio from video: {e}')
            file_path = None
        return file_path

    def get_audio_from_video(self, video_path):
        """
        Получение аудиофайла из видеофайла (в формате .mp4 или .wav) по локальному пути
        :param video_path: Path
        :return: audio_path: Path
        """
        try:
            video = VideoFileClip(video_path)
            audio = video.audio
            audio_path = video_path[:-3] + 'mp3'
            audio.write_audiofile(audio_path)
            logging.debug(f'Success to convert video to audio to path {audio_path}')
            return audio_path
        except Exception as e:
            logging.error(f'Failed to convert video to audio: {e}')

    @staticmethod
    def delete_file(file_path):
        """
        Удаление файла
        :param file_path:str
        :return: None
        """
        os.remove(file_path)
