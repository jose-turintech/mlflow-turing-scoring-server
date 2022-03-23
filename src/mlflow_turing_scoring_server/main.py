"""
This module contains the main process
"""
# ────────────────────────────────────────── imports ────────────────────────────────────────── #
from datetime import datetime
from time import sleep

from loguru import logger

from mlflow_turing_scoring_server.conf.conf_manager import conf_mgr


# ───────────────────────────────────────────────────────────────────────────────────────────── #

def print_conf():
    logger.info("Configuration Manager")
    logger.info(f" - path_root : {conf_mgr.path_root}")
    logger.info(f" - path_src  : {conf_mgr.path_src}")
    logger.info(f" - path_app  : {conf_mgr.path_app}")
    logger.info(f" - path_conf : {conf_mgr.path_conf}")
    logger.info(f" - env_file  : {conf_mgr.env_file}")


def main():
    while True:
        sleep(5)
        logger.info(datetime.now())


if __name__ == '__main__':
    print_conf()
    main()
