<<<<<<< HEAD
#!/usr/bin/python3
"""
Initializes the model package and and creates a unique FileStorage instance
"""

from model.engine.file_storage import FileStorage

=======
"""Module for FileStorage autoinit."""
from models.engine.file_storage import FileStorage
>>>>>>> main
storage = FileStorage()
storage.reload()
