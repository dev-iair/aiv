## Install
- Server install
```bash
docker-compose -f docker-compose.prd.yaml up 
```
- Client install
```bash
pip install git+
```
## Sample Code
```python
from train_db import Client

# 인스턴스 생성
client = Client()

# 서버 설정
client.set_server(url="http://api:8000", key="test")

get_models = client.get_models()
print(get_models)

# 모델, 모델 버전 설정
client.set_model(model_name="test", model_version="v0.161")

get_model = client.model.get()
print(get_model)

# 학습 버전 설정
client.set_train(
    train_version="v11111",
    params=[{"test1": "test1"}, {"test2": "test2"}],
)

# 로그 저장
client.log.save(type="info", message="test")
get_log = client.log.get(log_type="info")
print(get_log)

# 메트릭 저장
client.metric.save(epoch=1, step=1, phase="train", name="loss", value=0.1)
get_metric = client.metric.get(name="loss", epoch=1, step=1, phase="train")
print(get_metric)

# 아티팩트 저장
client.artifact.save(
    type="weights",
    file_path="weights.pth",
    file_size=100,
    epoch=1,
    step=1,
    phase="train",
)
get_artifact = client.artifact.get(type="weights")
print(get_artifact)
```

## Architecture
![Architecture Diagram]()

## Database
![Database Diagram]()
