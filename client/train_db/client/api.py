import requests

from ..service.log import Log
from ..service.metric import Metric
from ..service.model import Model
from ..service.artifact import Artifact
from ..service.train import Train


class Client:
    def __init__(self):
        self.base_url = ""
        self.headers = {}

        self.log = None
        self.metric = None
        self.model = None
        self.artifact = None
        self.train = None

        self.model_id = None
        self.model_version_id = None

        self.model_train_id = None

    def set_server(self, url, key):
        self.base_url = url
        self.headers = {"Authorization": f"Bearer {key}"}
        check_health = self.get("api/health")
        if check_health.status_code != 200:
            raise Exception("Server is not healthy")

    def get_models(self):
        res = self.get("api/model/list")
        if res.status_code != 200:
            return Exception("Something went wrong")
        else:
            return res.json()

    def set_model(self, model_name, model_version):
        self.model = Model(self.get, self.post, model_name, model_version)

    def set_train(self, train_version, params=None):
        self.train = Train(
            self.get,
            self.post,
            self.model.model_version_id,
            train_version,
            params=params,
        )

        self.model_train_id = self.train.model_train_id

        self.log = Log(self.get, self.post, self.model_train_id)
        self.metric = Metric(self.get, self.post, self.model_train_id)
        self.artifact = Artifact(self.get, self.post, self.model_train_id)

    def get(self, endpoint, params=None):
        response = requests.get(
            f"{self.base_url}/{endpoint}", headers=self.headers, params=params
        )
        return response

    def post(self, endpoint, data=None):
        response = requests.post(
            f"{self.base_url}/{endpoint}", headers=self.headers, json=data
        )
        return response
