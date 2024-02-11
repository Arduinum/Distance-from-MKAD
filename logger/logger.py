from datetime import datetime
from pathlib import Path


def writer_log(target:str, distance:float) -> None:
    """Функция запишет строку лога в файл"""

    path = Path(__file__).resolve().parent

    # откроем файл для записи лога и если файла нет создадим его
    with open(file=f'{path}/.log', mode='a', encoding='utf-8') as file:
        datetime_now = datetime.now()
        datetime_str = datetime_now.strftime('%d.%m.%Y %H:%M:%S')

        try:
            # пишем строку лога с расстоянием от мкад до цели в файл лога
            file.write(
                f'{datetime_str} - расстояние от МКАД до {target} {distance}\n'
            )
        except NotADirectoryError as err:
            print(err, 'введите путь для папки лога!')


if __name__ == '__main__':
    # пример работы с функцией
    writer_log(target='Тестовая цель', distance=40.545467)
