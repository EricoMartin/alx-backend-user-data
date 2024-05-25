#!/usr/bin/env python3
"""
BasicAuth Class
"""

import base64
from .auth import Auth
from typing import TypeVar

from models.user import User


class BasicAuth(Auth):
    """ Implement Basic Authorization protocol methods
    """
