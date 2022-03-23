import os
from mlflow_turing_scoring_server import scoring_server
from mlflow.pyfunc import load_model

print("Here we go jarey second attemp.")
app = scoring_server.init(load_model(os.environ[scoring_server._SERVER_MODEL_PATH]))
