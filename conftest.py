import pytest
import yaml
from datetime import datetime

with open('config.yaml') as f:
    config = yaml.safe_load(f)


@pytest.fixture()
def get_logs() -> str:
    """
       1. Добавить фикстуру, возвращающую время старта шага в формате, пригодном для journalctl
       2. Реализовать для каждого шага сохранение в текстовый файл фрагмента системного лога за время работы шага
    """

    now = datetime.now().strftime("%b %d %H:%M:%S")
    with open(config['journal'], 'r') as j:
        for line in j:
            if line.find(now) == 0:
                with open('stat.txt', 'a') as stat:
                    stat.write(line)
    return now
