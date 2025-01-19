class Log:
    def __init__(self, get, post, model_train_id):
        self.get_api = get
        self.post_api = post
        self.model_train_id = model_train_id

    def save(self, type, message):
        res = self.post_api(
            "api/log/",
            {
                "model_train_id": self.model_train_id,
                "type": type,
                "message": message,
            },
        )
        if res.status_code != 200:
            return Exception("Something went wrong")
        else:
            return res.json()

    def get(self, log_type=None):
        params = {"model_train_id": self.model_train_id}
        if log_type:
            params["type"] = log_type
        res = self.get_api("api/log/", params)
        if res.status_code != 200:
            return Exception("Something went wrong")
        else:
            return res.json()
