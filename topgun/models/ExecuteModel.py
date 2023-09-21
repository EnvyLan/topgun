from pydantic import BaseModel


class ExecuteModel(BaseModel):

    words: str
    file_list: list
