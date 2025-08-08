from dataclasses import dataclass, field
from typing import Any, Dict, List


class DatabaseError(TypeError):
    """
    A specific error for when data types are invalid for the database.
    It inherits from TypeError, which is appropriate for type-related issues.
    """

    def __init__(self):
        super().__init__(
            "Data is invalid because data must be one of type: [Dict, List, str, int, float]."
        )


class DataImportError(Exception):
    """
    A higher-level error indicating a failure in the data import process.
    The underlying cause is chained to this exception.
    """

    def __init__(self):
        super().__init__("Error: Data was not imported.")


@dataclass
class Database:
    """
    Simulates a database with a method for saving data.
    The `save_data` method uses exception chaining.
    """

    def _validate_data(self, data: Any) -> None:
        """
        Validates the data type, raising a specific DatabaseError on failure.
        """
        if not isinstance(data, (Dict, List, str, int, float)):
            raise DatabaseError()

    def save_data(self, data: Any) -> str:
        """
        Simulates saving data. It handles the low-level DatabaseError
        and raises a higher-level DataImportError instead.
        """
        try:
            self._validate_data(data)
            return f"Simulated data saving: saving {data}"
        except DatabaseError as e:
            # Here, we raise a new exception from the caught exception (e).
            # The 'from e' clause preserves the traceback and context of the
            # original DatabaseError.
            raise DataImportError() from e


@dataclass
class DataImporter:
    """
    A class that uses the Database to import data.
    It uses composition to hold a reference to a Database object.
    """

    database: Database = field(default_factory=Database)

    def import_data(self, data: Any) -> None:
        """
        Calls the save_data method on the composed database object.
        """
        self.database.save_data(data)


# --- Demonstration of the working code ---

# Test a successful import with valid data types
try:
    print("--- Trying to import valid data (string) ---")
    data_importer_str = DataImporter()
    print(data_importer_str.import_data("shoe"))
except DataImportError as e:
    print(f"Caught an unexpected error: {e}")

try:
    print("\n--- Trying to import valid data (list) ---")
    data_importer_list = DataImporter()
    print(data_importer_list.import_data(["hello", "cat"]))
except DataImportError as e:
    print(f"Caught an unexpected error: {e}")

try:
    print("\n--- Trying to import valid data (dictionary) ---")
    data_importer_dict = DataImporter()
    print(data_importer_dict.import_data({"hello": "cat"}))
except DataImportError as e:
    print(f"Caught an unexpected error: {e}")


# Test a failed import with an invalid data type (tuple)
try:
    print("\n--- Trying to import invalid data (tuple) ---")
    data_importer_invalid = DataImporter()
    data_importer_invalid.import_data(("hello", "cat"))
except DataImportError as e:
    # We catch the higher-level exception here
    print(f"Caught the expected higher-level error: {e}")
    # We can access the original exception using the '__cause__' attribute
    if e.__cause__:
        print(f"The original cause was: {e.__cause__}")
        print(f"The type of the original cause is: {type(e.__cause__)}")
