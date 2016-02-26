# encoding: utf-8
"""
Teams module
============
"""

from app.extensions.api import api_v1


def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    Init teams module.
    """
    api_v1.add_oauth_scope('teams:read', "Provice access to team details")
    api_v1.add_oauth_scope('teams:write', "Provice write access to team details")

    # Touch underlying modules
    from . import models, resources
