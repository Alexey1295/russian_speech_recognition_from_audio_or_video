# Распознавание русской речи из аудио или видео

### Описание
Данный проект можно использовать для распознавания русской речи из следующих источников:
 - аудиофайл по локальному пути
 - видеофайл по локальному пути
 - видеофайл по ссылке из vk.com

Для распознавания русской речи используется предобученная модель https://openai.com/blog/whisper/

На момент данной записи доступны для использования 5 типов моделей в зависимости от их размера:

|  Size  | Parameters | Multilingual model | Required VRAM |
|:------:|:----------:|:------------------:|:-------------:|
|  tiny  |   ~39 M    |       `tiny`       |     ~1 GB     |
|  base  |   ~74 M    |       `base`       |     ~1 GB     |
| small  |   ~244 M   |      `small`       |     ~2 GB     |
| medium |   ~769 M   |      `medium`      |     ~5 GB     |
| large  |  ~1550 M   |      `large`       |    ~10 GB     |


Выбранную модель можно указать в соответсвующем конфигурационном фале (по умолчанию: medium).

### Структура
**configs** - конфиги к логированию и настройкам модели (веса, выбор видеокарты для вычислений)

**src** - пайплайн

**main.py** - основной скрипт запуска

**requirements.txt** - перечень необходимых библиотек 

### Использование

```
pip3 install -r requirements.txt
python3 main.py --content_type <audiofile or videofile or vk_video>
                --content_path <path to file or link to vk-video>
```

Результат распознавания будет выведен в логах.
