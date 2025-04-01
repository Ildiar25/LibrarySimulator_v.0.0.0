from typing import Dict, List


BookDict = Dict[str, int | str]
ClientDict = Dict[str, str | list[BookDict]]

FileList = List[BookDict | ClientDict]
