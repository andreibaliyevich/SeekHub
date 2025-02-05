"""
FileHandler Class for Managing File Operations

This module provides the `FileHandler` class to manage file operations, such as saving and deleting files. It ensures file type validation and organizes files within a `media` directory.

Classes:
    FileHandler:
        Handles file upload, storage, and deletion operations.

Methods:
    __init__():
        Initializes the `FileHandler` instance with the default media directory.

    save_file(file: UploadFile, allowed_extensions: set) -> str:
        Saves an uploaded file to the media directory after validating its extension.

    delete_file(file_path: str) -> None:
        Deletes a file from the filesystem if it exists.
"""

import os
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from exceptions.data import InvalidDataError


class FileHandler:
    """
    Handles file operations such as saving and deleting files.

    Attributes:
        media_dir (Path): The directory where files will be stored.
    """

    def __init__(self):
        """
        Initializes the `FileHandler` instance.

        Notes:
            - The `media` directory is used as the default storage location for files.
        """
        self.media_dir = Path("media")

    def save_file(self, file: UploadFile, allowed_extensions: set) -> str:
        """
        Saves an uploaded file to the media directory after validating its extension.

        Args:
            file (UploadFile): The uploaded file to be saved.
            allowed_extensions (set): A set of allowed file extensions (e.g., {"jpg", "png"}).

        Raises:
            InvalidDataError: If the file extension is not in the allowed extensions or failed to save file.

        Returns:
            str: The path to the saved file.
        """
        extension = file.filename.split(".")[-1].lower()

        if extension not in allowed_extensions:
            raise InvalidDataError({"file": "Unsupported file type."})

        self.media_dir.mkdir(exist_ok=True)
        unique_filename = f"{uuid4()}.{extension}"
        file_path = self.media_dir / unique_filename

        try:
            with file.file as f:
                with open(file_path, "wb") as out_file:
                    out_file.write(f.read())
        except Exception:
            raise InvalidDataError({"file": "Failed to save file."})

        return str(file_path)

    def delete_file(self, file_path: str) -> None:
        """
        Deletes a file from the filesystem if it exists.

        Args:
            file_path (str): The path to the file to be deleted.

        Notes:
            - If the file does not exist, no action is taken.
        """
        if os.path.exists(file_path):
            os.remove(file_path)
