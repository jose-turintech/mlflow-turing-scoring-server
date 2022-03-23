from loguru import logger

from mlflow_turing_scoring_server.conf.conf_manager import conf_mgr


class ServiceExample:
    def __init__(self):
        logger.info("Created new a ServiceExample instance")

    @property
    def env_file(self):
        return conf_mgr.env_file
