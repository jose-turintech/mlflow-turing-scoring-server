import os, signal
from subprocess import Popen

from pkg_resources import resource_filename

import mlflow_turing_scoring_server


class NginxProcessService:

    def manage_custom_nginx(self):
        result = self.kill_running_nginx()
        if result:
            self.start_nginx_process()

    def kill_running_nginx(self) -> bool:
        # Ask user for the name of process
        name = "nginx"
        return_value = False
        try:

            # iterating through each instance of the process
            for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
                fields = line.split()

                # extracting Process ID from the output
                pid = fields[0]

                # terminating process
                os.kill(int(pid), signal.SIGKILL)
            print("Process Successfully terminated")
            return_value = True
        except:
            print("Error Encountered while running script")
        return_value = False
        return return_value

    def start_nginx_process(self):
        nginx_conf = resource_filename(
            mlflow_turing_scoring_server.__name__, "scoring_server/nginx.conf"
        )

        Popen(["nginx", "-c", nginx_conf])
