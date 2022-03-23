"""
This module aims to implement the base class used by all test classes with common methods.
"""
# ────────────────────────────────────────── imports ────────────────────────────────────────── #
import unittest
from pathlib import Path

from tests_mlflow_turing_scoring_server.conftest import data_mgr


# ───────────────────────────────────────────────────────────────────────────────────────────── #
#                                        Base Test Class                                        #
# ───────────────────────────────────────────────────────────────────────────────────────────── #

class BaseTest:
    """
    Base Tests Class
    """

    case = unittest.TestCase()
    method: str = None

    _data_path: Path = data_mgr.data_path

    # -------------------------------------------------------------------------------------------

    @classmethod
    def setup_class(cls):
        """ Configuration called when initializing the class """

    @classmethod
    def teardown_class(cls):
        """ Configuration called when destroying the class """

    def setup_method(self, method):
        """ Configuration called for every method """
        self.method = method.__name__

    def teardown_method(self, method):
        """ Configuration called at the end of the method execution """

    # -------------------------------------------------------------------------------------------
