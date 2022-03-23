"""
This module aims to implement the tests of the "ConfManager" singleton class.
"""
# pylint: disable=W0212
#       W0212: Access to a protected member _logging_conf of a client class (protected-access)
# ────────────────────────────────────────── imports ────────────────────────────────────────── #
import pytest

from mlflow_turing_scoring_server.conf.conf_manager import conf_mgr, ConfManager
from mlflow_turing_scoring_server.conf.logger_conf import file_logger_conf_factory

from tests_mlflow_turing_scoring_server.base.base_test import BaseTest
from tests_mlflow_turing_scoring_server.conftest import ROOT_PATH, TESTS_ENV_PATH


# ───────────────────────────────────────────────────────────────────────────────────────────── #
#                                         Test Class                                            #
# ───────────────────────────────────────────────────────────────────────────────────────────── #

class TestConfManager(BaseTest):
    """
    Configuration Manager testing class
    """

    def test_init(self):
        """
        Validation of the ConfManager.__init__
        """
        conf1 = ConfManager()
        conf2 = ConfManager(env_file=TESTS_ENV_PATH)

        self.case.assertEqual(str(ROOT_PATH.joinpath(*['src', '.env'])), conf1.env_file)
        self.case.assertEqual(str(TESTS_ENV_PATH), conf2.env_file)

    def test_update_conf_mgr(self):
        """
        Validation of the ConfManager.update_conf_mgr
        """
        conf = ConfManager()
        self.case.assertEqual(str(ROOT_PATH.joinpath(*['src', '.env'])), conf.env_file)

        conf.update_conf_mgr(env_file=str(TESTS_ENV_PATH))
        self.case.assertEqual(str(TESTS_ENV_PATH), conf.env_file)

        conf.update_conf_mgr(env_file='.env')
        self.case.assertIsNone(conf.env_file)

    def test_library_paths(self):
        """
        Validation of the ConfManager path configurations
        """
        expected = ROOT_PATH
        self.case.assertEqual(expected, conf_mgr.path_root, "path_root")

        expected = expected.joinpath('src')
        self.case.assertEqual(expected, conf_mgr.path_src, "path_src")

        expected = expected.joinpath("mlflow_turing_scoring_server")
        self.case.assertEqual(expected, conf_mgr.path_app, "path_app")

        expected = expected.joinpath('conf')
        self.case.assertEqual(expected, conf_mgr.path_conf, "path_conf")

    def test_logging_conf(self):
        """
        Validation of the logging_conf properties
        """
        expected = file_logger_conf_factory(
            _env_file=TESTS_ENV_PATH,
            prefix='LOGGER',
            sink=conf_mgr.defaults_logging_conf.get('sink'),
            level="debug",
            defaults=dict(unknown="unknown")
        )
        self.case.assertDictEqual(expected.dict(), conf_mgr.logging_conf.dict())

        conf_mgr._logging_conf = None
        self.case.assertDictEqual(expected.dict2add, conf_mgr.logging_conf.dict2add)


# ───────────────────────────────────────────────────────────────────────────────────────────── #

if __name__ == "__main__":
    pytest.main()
