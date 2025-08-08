from dataclasses import dataclass, field
from typing import Any, Dict, List


class DatabaseError(TypeError):
    def __init__(self):
        super().__init__(
            "Data is invalid because data must be one of type: [Dict, List, str, int, float]."
        )


class DataImportError(Exception):
    def __init__(self):
        super().__init__("Error: Data was not imported.")


@dataclass
class Database:
    def _validate_data(self, data: Any) -> None:
        if not isinstance(data, (Dict, List, str, int, float)):
            raise DatabaseError()

    def save_data(self, data: Any) -> str:
        try:
            self._validate_data(data)
            return f"Simulated data saving: saving {data}"
        except DatabaseError as e:
            raise DataImportError() from e


@dataclass
class DataImporter:
    database: Database = field(default_factory=Database)

    def import_data(self, data: Any):
        self.database.save_data(data)


# incorrect Type
try:
    data_importer = DataImporter()
    data_importer.import_data(("hello", "cat"))
except DataImportError as e:
    print(f"{e}")
    if e.__cause__:
        print(f"{e.__cause__}")
        print(f"{type(e.__cause__)}")

try:
    data_importer2 = DataImporter()
    data_importer2.import_data("shoe")
except DataImportError as e:
    print(e)

try:
    data_importer3 = DataImporter()
    data_importer3.import_data(["hello", "cat"])
except DataImportError as e:
    print(e)

try:
    data_importer4 = DataImporter()
    data_importer4.import_data({"hello": "cat"})
except DataImportError as e:
    print(e)
