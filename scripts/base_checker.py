import sys
import logging
import time
from datetime import datetime

import schedule
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))

logger.addHandler(console_handler)

class BaseChecker:
    def __init__(self, scan_path, log_path):
        self.scan_path = Path(scan_path)
        self.log_path = Path(log_path)

        if not Path.exists(self.scan_path):
            raise ValueError(f'Path does not exist {self.scan_path} or is not a directory')

        try:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            logger.error(f'An error occurred when creating the directory: {e}')
            sys.exit(1)

        file_handler = logging.FileHandler(self.log_path, mode='a')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))

        logger.addHandler(file_handler)

    def check(self) -> None:
        weekday = datetime.today().weekday()
        if weekday < 5:
            try:
                tmp_files = list(self.scan_path.glob("*.tmp"))
                logger.debug(f"Найдено файлов .tmp: {len(tmp_files)}")
                for tmp_filepath in self.scan_path.glob("*.tmp"):
                    Path(tmp_filepath).unlink()

                logger.info(f'Eltex. Временные файлы очищены')
            except FileNotFoundError:
                logger.error("File not found: Filepath is invalid")
                sys.exit(1)
            except PermissionError:
                logger.error("Permissions error occured: make sure that the script was run with administrator rights")
                sys.exit(1)
        else:
            logger.debug("Сегодня выходной день, проверка производиться не будет")

def main():

    if len(sys.argv) != 3:
        logger.error("Usage error occured, a right way to transmission of arguments: <scan_path> <log_path>")

    scan_path = sys.argv[1]
    log_path = sys.argv[2]

    try:
        checker = BaseChecker(scan_path, log_path)
    except Exception as e:
        logger.error(f'An error occurred when creating the object: {e}')
        sys.exit(1)

    # checker.check()
    schedule.every(1).hours.do(checker.check)
    schedule.run_all()

    logger.debug("Скрипт запущен и будет выполняться каждый час по будним дням.")
    logger.debug("Для остановки нажмите Ctrl+C")

    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("Скрипт остановлен пользователем.")
        sys.exit(0)


if __name__ == '__main__':
    main()