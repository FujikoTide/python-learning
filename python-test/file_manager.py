from dataclasses import dataclass

from click import FileError


@dataclass
class FileManager:
    filename: str
    mode: str
    _file = None

    def __enter__(self):
        file = open(self.filename, mode=self.mode)
        self._file = file
        return file

    def __exit__(self, exc_type, exc_value, traceback):
        if self._file is not None:
            self._file.close()
        else:
            raise FileError("File error occurred")


file_manager = FileManager("testfile.txt", "w")
with file_manager as f:
    f.write("hello")

file_manager2 = FileManager("testfile.txt", "r")
with file_manager2 as f:
    print(f.read())
