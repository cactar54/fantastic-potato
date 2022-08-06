import time
import uuid
from dataclasses import dataclass, field


@dataclass
class BasicDocument:
    def __init__(self):
        self.__id
        self.__docName
        self.__authorName
        self.__createDate
        self.__company
