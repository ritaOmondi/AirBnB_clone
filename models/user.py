#!/bin/usr/python3
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
from datetime import datetime
import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """User class instantiator"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
