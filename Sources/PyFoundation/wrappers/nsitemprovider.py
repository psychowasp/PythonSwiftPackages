from swift_tools.swift_types import *
from typing import Optional

@wrapper(pyinit=False)
class NSItemProvider:

    suggestedName = property(Optional[str])
    #suggestedName = property(str)
#     #preferredPresentationSize = property(list[float])

    registeredTypeIdentifiers = property(list[str], setter= False) 
    
    def loadFileRepresentation(self,forTypeIdentifier: str, completionHandler: callable[(Optional[URL],Optional[Error]), None]): ...

    @no_labels(id=True)
    def hasItemConformingToTypeIdentifier(self, id: str) -> bool: ...

    def loadInPlaceFileRepresentation(self,forTypeIdentifier: str, completionHandler: callable[[Optional[URL],bool,Optional[Error]], None]): ...

    def loadDataRepresentation(self,forTypeIdentifier: str, completionHandler: callable[[Optional[data],Optional[Error]], None]): ...
