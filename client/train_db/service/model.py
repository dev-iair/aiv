class Model:
    def __init__(
        self,
        get,
        post,
        model_name,
        model_version,
    ):
        self.get_api = get
        self.post_api = post

        self.model_id = None
        self.model_version_id = None

        if (
            model_name is None
            or model_name == None
            or model_name == ""
            or model_name == " "
        ):
            raise Exception("Model name and version is required")

        res = self.post_api(
            "api/model/", {"name": model_name, "version": model_version}
        )

        if res.status_code != 200:
            raise Exception(res.json()["detail"])
        else:
            res_json = res.json()
            self.model_id = res_json["model"]["id"]
            self.model_version_id = res_json["model_version"]["id"]

    def get(self):
        res = self.get_api("api/model/", {"model_id": self.model_id})
        if res.status_code != 200:
            raise Exception(res.json()["detail"])
        else:
            return res.json()

    def get_trains(self):
        res = self.get_api("api/train/", {"model_version_id": self.model_version_id})
        if res.status_code != 200:
            raise Exception(res.json()["detail"])
        else:
            return res.json()
