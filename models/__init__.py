#!/usr/bin/python3
# models/__init__.py

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

"""This module defines instance of FileStorage class"""
from models.engine.file_storage import FileStorage
storage = FileStorage('file.json')
storage.reload()
>>>>>>> e71b63a89d712137c8f5cc89211607390b9a353b
