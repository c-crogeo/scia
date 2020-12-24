<div align="center">
<h1>scia</h1>
<h4>Python logging extension</h4>
</div>

## Setup
- From sources
```bash
git clone https://github.com/crogeo/scia.git
cd scia
pip install .
```

## Usage

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

- Project name configuration
```python
from scia import config

config.project = 'myproject' # The logger name and the filename: logs/myproject.log
config.inifile = 'log.ini'  # Configuration file
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

## Licence
This source code is published under [MIT Licence](https://).

#
>Ma l'acqua gira e passa e non sa dirmi niente  
>di gente, me, o di quest'aria bassa  
>ottusa e indifferente cammina e corre via  
>lascia una scia e non gliene frega niente
>
>*Francesco Guccini*
