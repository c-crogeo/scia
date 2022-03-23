# scia
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/crogeo/scia/blob/master/LICENSE)

Python logging extension - crogeo.org

## Installation
- From sources
```bash
git clone https://github.com/crogeo/scia.git
cd scia
pip install .
```
- From PyPi
```bash
pip install scia
```

## Documentation

- Config file: log.ini
```ini
[loggers]
keys=root,daily

[handlers]
keys=console,daily

[formatters]
keys=fmt

[logger_root]
level=INFO
handlers=console
qualname=root
propagate=0

[logger_daily]
level=DEBUG
handlers=console,daily
qualname=%(project)s
propagate=0

[handler_daily]
class=scia.handlers.TimedRotatingFileHandler
level=DEBUG
formatter=fmt
args=('logs/%(project)s.log', 'midnight')

[handler_console]
class=StreamHandler
level=DEBUG
formatter=fmt
args=(sys.stdout,)

[formatter_fmt]
format=%(asctime)s - %(name)10s - %(levelname)8s - %(message)s
```

- Usage
```python
from scia import get_logger

log = get_logger('myproject')

log.debug('Debug message')
log.info('Info message')
log.warning('Warning message')
log.error('Error message')
```

- Project name configuration
```python
from scia import config

config.project = 'myproject' # The logger name and the filename: logs/myproject.log
config.inifile = 'log.ini'  # Configuration file
```

## License
Crogeo scia is [MIT licensed](./LICENSE).
