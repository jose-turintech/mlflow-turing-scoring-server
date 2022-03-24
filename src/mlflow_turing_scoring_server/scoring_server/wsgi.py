import os
from mlflow_turing_scoring_server import scoring_server
from mlflow_turing_scoring_server.services.nginx_process_service import NginxProcessService
from mlflow.pyfunc import load_model

try
    print("Starting Turing custom scoring server.")
    print("Managing nginx processes:")
    service: NginxProcessService = NginxProcessService()
    service.manage_custom_nginx()
except BaseException:
    print("Some error happened, coninuing")

app = scoring_server.init(load_model(os.environ[scoring_server._SERVER_MODEL_PATH]))
