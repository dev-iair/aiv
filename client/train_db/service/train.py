class Train:
    def __init__(self, get, post, model_version_id, model_train_version, params=None):

        if (
            model_version_id is None
            or model_version_id == None
            or model_version_id == ""
        ):
            raise Exception("Model version id is required")

        self.get_api = get
        self.post_api = post

        self.model_train_id = None

        res = self.post_api(
            "api/train/",
            {
                "model_version_id": model_version_id,
                "version": model_train_version,
                "status": "ready",
                "params": params,
            },
        )

        if res.status_code != 200:
            raise Exception(res.json()["detail"])
        else:
            res_json = res.json()
            self.model_train_id = res_json["id"]
