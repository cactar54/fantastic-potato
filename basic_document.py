import time
import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class BasicDocument:
    docUuid: str = field(init=False, default_factory=str)
    createDate: str = field(init=False, default_factory=str)

    def __init__(self):
        self.__docUuid
        self.__docName
        self.__authorName
        self.__createDate
        self.__company

   # def document_verification(self):

   #     docUuid = uuid.uuid4()
   #     createDate = time.time()

   #     print(docUuid)
   #     print(createDate)


myDoc = BasicDocument