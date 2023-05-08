import json

from typing import List


from app.shared.dto.message import MessageCreate


class MockMessageRepo:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> List[MessageCreate]:
        items: List[MessageCreate] = []
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                items.append(MessageCreate(**item))
        return items
