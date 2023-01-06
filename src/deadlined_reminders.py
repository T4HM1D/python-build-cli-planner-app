from abc import ABCMeta, abstractmethod, ABC
from _collections_abc import Iterable
from dateutil.parser import parse
from datetime import datetime


class DeadlinedMetaReminder(Iterable, ABCMeta):
    @abstractmethod
    def is_due(self):
        pass

    def __iter__(self):
        pass


class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass

    def __iter__(self):
        text = self.text
        formatted_date = self.date.isoformat()
        iter([text, formatted_date])


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst=True)

    def is_due(self):
        return self.date <= datetime.now()
