import os, signal
import time
from subprocess import Popen

from pkg_resources import resource_filename

import mlflow_turing_scoring_server


class NginxProcessService:

    def manage_custom_nginx(self):
        print("Managing custom nginx processes.")
        self.reload_nginx_process()

    def reload_nginx_process(self):
        # nginx_conf = resource_filename(
        #    mlflow_turing_scoring_server.__name__, "scoring_server/nginx.conf"
        #)
        nginx_conf = "/miniconda/lib/python3.9/site-packages/mlflow/models/container/scoring_server/nginx.conf"
        print("Location of the new nginx conf file:")
        print(nginx_conf)
        Popen(["sed", "-i", "'s/invocations/invocations|turing/g'", "/", nginx_conf])
        time.sleep(1)
        Popen(["nginx", "-s", "reload", "-c", nginx_conf, "-t"])
