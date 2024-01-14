#!/usr/bin/python3
"""
The module is base_module
parent class is BaseModule
"""

import uuid
from datetime import datetime
import models
#from models.engine.file_storage import storage


class BaseModel:
    instances = {}

    """BaseModel class that defines all instances
    and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """This is the class instantiator"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # Generate a unique ID
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
                    setattr(self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
                key = f"{self.__class__.__name__}.{self.id}"
            else:
                key = f"{self.__class__.__name__}.{self.id}"
            self._get_storage().new(self)
            self.__class__.instances[self.id] = self
            BaseModel.instances[key] = self
        else:
            self.id = str(uuid.uuid4())
            key = f"{self.__class__.__name__}.{self.id}"
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self._get_storage().new(self)
            self.__class__.instances[self.id] = self
            BaseModel.instances[key] = self

    def __str__(self):
        """Return a string representation of the object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Call save(self) method of storage."""
        self.updated_at = datetime.now()
<<<<<<< HEAD
        models.storage.save()
=======
        self._get_storage().save()

    @classmethod
    def all(cls):
        return cls.instances

    def _get_storage(self):
        from models import storage
        return storage
>>>>>>> e71b63a89d712137c8f5cc89211607390b9a353b

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def update_instance(cls, instance_id, attribute, value):
        """update specified attribute"""
        key = f"{cls.__name__}.{instance_id}"

        if key in cls.instances[key]:
            instance = self.instance[key]
            if attribute not in ['instance_id', 'created_at', 'updated_at']:
                setattr(instance, attribute, value)
                instance.save()
            else:
                print("cannot update id , created_at, updated_at")
        else:
            print("instance not found")
