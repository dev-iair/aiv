class Metric:
    def __init__(self, get, post, model_train_id):
        self.get_api = get
        self.post_api = post
        self.model_train_id = model_train_id

    def save(self, epoch, step, phase, name, value):
        res = self.post_api(
            "api/metric/",
            {
                "model_train_id": self.model_train_id,
                "epoch": epoch,
                "step": step,
                "phase": phase,
                "name": name,
                "value": value,
            },
        )
        if res.status_code != 200:
            return Exception("Something went wrong")
        else:
            return res.json()

    def get(self, name=None, epoch=None, step=None, phase=None):
        params = {"model_train_id": self.model_train_id}
        if name:
            params["name"] = name
        if epoch:
            params["epoch"] = epoch
        if step:
            params["step"] = step
        if phase:
            params["phase"] = phase
        res = self.get_api("api/metric/", params)
        if res.status_code != 200:
            return Exception("Something went wrong")
        else:
            return res.json()
