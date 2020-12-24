import logging.handlers
from datetime import datetime
from os import listdir
from pathlib import Path


class TimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):

    def __init__(self,
                 filename,
                 when='midnight',
                 interval=1,
                 backup_count=90,
                 encoding=None,
                 delay=False,
                 utc=False,
                 at_time=None):
        self.file = Path(filename)
        self.directory = self.file.parent
        self.directory.mkdir(parents=True, exist_ok=True)
        kwargs = {
            'when': when,
            'interval': interval,
            'backupCount': backup_count,
            'encoding': encoding,
            'delay': delay,
            'utc': utc,
            'atTime': at_time
        }
        super().__init__(filename, **kwargs)
        self.namer = self._namer
        # Add references
        self.baseFilename = self.__getattribute__('baseFilename')
        self.suffix = self.__getattribute__('suffix')
        self.extMatch = self.__getattribute__('extMatch')
        self.backupCount = self.__getattribute__('backupCount')
        self.__setattr__('getFilesToDelete', self._get_files_to_delete)

    def _namer(self, default):
        """
        Define a custom name of old files
        :param default: Used by superclass. It contains last modification time (str)
        :return: new filename (str)
        """
        fmt = self.suffix
        dtstr = default[len(self.baseFilename + '.'):]
        dt = datetime.strptime(dtstr, self.suffix)
        return self.directory / dt.strftime(f'{fmt}{self.file.suffix}')

    def _get_files_to_delete(self):
        """
        Override method of superclass because there is a custom namer function
        :return: list of files to delete
        """
        result = []
        for file in listdir(self.directory):
            if self.extMatch.match(file):
                result.append(self.directory / file)
        if len(result) >= self.backupCount:
            return sorted(result)[:len(result) - self.backupCount]
        return []
