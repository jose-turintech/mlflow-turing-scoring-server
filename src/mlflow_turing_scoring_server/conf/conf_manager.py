"""
This module implements and instantiates the common configuration class used in the project.
"""
# ────────────────────────────────────────── imports ────────────────────────────────────────── #
import sys
import tempfile
from pathlib import Path
from typing import Dict

from loguru import logger

from mlflow_turing_scoring_server.conf.logger_conf import logger_conf_factory, FileLoggerConf, file_logger_conf_factory


# ───────────────────────────────────────────────────────────────────────────────────────────── #
#                                     Configuration Manager                                     #
# ───────────────────────────────────────────────────────────────────────────────────────────── #

class ConfManager:
    """ Configuration Manager class """

    # APP paths
    path_conf: Path = Path(__file__).parent.resolve()  # conf package
    path_app: Path = path_conf.parent.resolve()  # mlflow_turing_scoring_server package
    path_src: Path = path_app.parent.resolve()  # src package
    path_root: Path = path_src.parent.resolve()  # mlflow-turing-scoring-server project

    # Library environment file
    _path_env_file: Path = path_src.joinpath('.env')
    _env_file: str = str(_path_env_file)

    _conf_prefix: str = None

    tmp_directory: Path = Path(tempfile.gettempdir()).joinpath("mlflow-turing-scoring-server")

    # The Logging Configurations object is instantiated once its use is invoked
    _logging_conf: FileLoggerConf = None
    defaults_logging_conf: Dict = dict(sink=tmp_directory.joinpath(*['logs', "mlflow_turing_scoring_server.log"]))

    # -------------------------------------------------------------------------------------------------

    def __init__(self, env_file: str or Path = None):
        if env_file:
            self.update_conf_mgr(env_file=env_file)
        else:
            self.update_logging_conf()

        logger.info("Configuration Manager initialized")

    # -------------------------------------------------------------------------------------------------

    @property
    def env_file(self) -> str:
        """
        Environment configuration file used in the current configuration
        """
        return self._env_file

    def update_conf_mgr(self, env_file: str):
        """
        Update all the configuration by loading the environment variables from the indicated file.
        """
        self._path_env_file = Path(env_file)
        self._env_file = str(self._path_env_file) if self._path_env_file.exists() else None

        if not self._path_env_file.exists():
            print(f"[WARNING] environment file does not exist: {env_file}")
            return

        self.update_logging_conf(_env_file=env_file)

    # -----------------------------------------------------------------------------------------------------------------
    # --- Logging Configuration
    # -----------------------------------------------------------------------------------------------------------------

    @property
    def logging_conf(self) -> FileLoggerConf:
        """
        :return: Logging configuration of the logs directed to file path outputs.
        """
        if self._logging_conf is None:
            self.update_logging_conf()
        return self._logging_conf

    def update_logging_conf(self, _env_file: str = None, defaults: dict = None):
        """
        Update the LoggingConf configuration by loading the environment variables from the indicated file and
        taking into account the default values
        """
        factory_args = dict(
            _env_file=_env_file or self._env_file,
            prefix='LOGGER',
            defaults=defaults or self.defaults_logging_conf
        )

        self._logging_conf: FileLoggerConf = file_logger_conf_factory(**factory_args)

        if self._logging_conf.enable:
            logger.remove()
            logger.add(**logger_conf_factory(sink=sys.stdout, **factory_args).dict2add)
            logger.add(**logger_conf_factory(sink=sys.stderr, level="ERROR", **factory_args).dict2add)
            logger.add(**self._logging_conf.dict2add)


# ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# ─── ConfManager instance
# ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

conf_mgr = ConfManager()
