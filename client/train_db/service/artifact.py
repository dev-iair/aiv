class Artifact:
    def __init__(self, get, post, model_train_id):
        self.get_api = get
        self.post_api = post
        self.model_train_id = model_train_id

    def save(self, type, file_path, file_size, epoch, step, phase):
        data = {
            "type": type,
            "file_path": file_path,
            "file_size": file_size,
            "epoch": epoch,
            "step": step,
            "phase": phase,
            "model_train_id": self.model_train_id,
        }
        res = self.post_api("api/artifact/", data)
        if res.status_code != 200:
            raise Exception("Failed to save artifact")
        return res.json()

    def get(self, type=None, metric_name=None, epoch=None, step=None, phase=None):
        params = {
            "model_train_id": self.model_train_id,
        }
        if type:
            params["type"] = type
        if metric_name:
            params["metric_name"] = metric_name
        if epoch:
            params["epoch"] = epoch
        if step:
            params["step"] = step
        if phase:
            params["phase"] = phase

        res = self.get_api("api/artifact/", params)
        if res.status_code != 200:
            raise Exception("Failed to get artifact")
        return res.json()
