def init():
    from scia import config
    config.project = 'crogeo'
    config.inifile = 'log.ini'


def main():
    from scia import get_logger
    import random
    for i in range(320):
        log = random.choice([
            get_logger('crogeo'),
            get_logger('root')
        ])
        func = random.choice([
            log.debug,
            log.info,
            log.warning,
            log.error
        ])
        func(f'Log message with hash {hash(log)}')


if __name__ == '__main__':

    init()
    main()
