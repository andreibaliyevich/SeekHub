import os
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from exceptions.form import InvalidFormDataError


class FileHandler:
    def __init__(self):
        self.media_dir = Path("media")

    def save_file(self, file: UploadFile, allowed_extensions: set) -> str:
        """
        Saves the file to the local media directory.
        :param file: Downloadable file.
        :param allowed_extensions: Set of valid file extensions.
        :return: Path to the saved file.
        """
        extension = file.filename.split(".")[-1].lower()

        if extension not in allowed_extensions:
            raise InvalidFormDataError({"file": "Unsupported file type."})

        self.media_dir.mkdir(exist_ok=True)
        unique_filename = f"{uuid4()}.{extension}"
        file_path = self.media_dir / unique_filename

        with file.file as f:
            with open(file_path, "wb") as out_file:
                out_file.write(f.read())

        return str(file_path)

    def delete_file(self, file_path: str) -> None:
        """
        Deletes the file if it exists.
        :param file_path: Path to file.
        """
        if os.path.exists(file_path):
            os.remove(file_path)
