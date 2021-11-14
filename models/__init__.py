#!/usr/bin/python3
"""
Initializes the model package and and creates a unique FileStorage instance
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
