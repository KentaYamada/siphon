import yaml
from os import path
from logging import config, getLogger


def init_logger(filename):
    if not filename:
        raise ValueError()
    if not path.exists(filename):
        raise IOError()
    root, ext = path.splitext(filename)
    if ext != '.yaml':
        raise IOError('not suportted file {0}'.format(ext))

    text = ''
    with open(filename) as f:
        text = f.read()
    if not text:
        raise IOError('Failed read {0}'.format(filename))
    config.dictConfig(yaml.load(text))

    return getLogger()
