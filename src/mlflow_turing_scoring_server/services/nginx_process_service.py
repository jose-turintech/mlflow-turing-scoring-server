import os, signal
from subprocess import Popen

from pkg_resources import resource_filename

import mlflow_turing_scoring_server


class NginxProcessService:

    def manage_custom_nginx(self):
        print("Managing custom nginx processes.")
        result = self.kill_running_nginx()
        if result:
            self.start_nginx_process()
        else:
            print("No nginx process found running.")


    def kill_running_nginx(self) -> bool:
        # Ask user for the name of process
        name = "nginx"
        return_value = False
        try:
            Popen(["nginx", "-s", "stop"])
            print("Processes Successfully terminated")
            return_value = False
        except:
            print("Error Encountered while running script")
        return_value = False
        return return_value

    def start_nginx_process(self):
        nginx_conf = resource_filename(
            mlflow_turing_scoring_server.__name__, "scoring_server/nginx.conf"
        )
        print("Location of the new nginx conf file:")
        print(nginx_conf)

        Popen(["nginx", "-c", nginx_conf])
