# CONTRIBUTING

## How to run the docker file locally

```
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-jwt-extended-rest-api sh -c "flask run --host 0.0.0.0"
```