"""
The application is initialized with the testing configuration
"""
# ────────────────────────────────────────── imports ────────────────────────────────────────── #
from mlflow_turing_scoring_server.conf.conf_manager import conf_mgr


from tests_mlflow_turing_scoring_server.conftest import TESTS_ENV_PATH


# ───────────────────────────────────────────────────────────────────────────────────────────── #
#                                 Global testing configuration                                  #
# ───────────────────────────────────────────────────────────────────────────────────────────── #

def update_conf_mgr(_env_file=TESTS_ENV_PATH):
    """
    Update Configuration Manager values with '.env.test' environment variables
    """
    conf_mgr.update_conf_mgr(env_file=_env_file)


# Configuration Manager update with environment variables and test paths
update_conf_mgr()
