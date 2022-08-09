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


#Creating a document and generating a UUID4 and Unix Time for it, then printing the result for diagnostic checking
myDoc = BasicDocument
myDoc.docUuid = uuid.uuid4()
myDoc.createDate = time.time()

print("The document UUID4 is " + str(myDoc.docUuid) + " and the Unix Time is " + str(myDoc.createDate))