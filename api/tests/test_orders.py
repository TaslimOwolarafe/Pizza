import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from flask_jwt_extended import create_access_token