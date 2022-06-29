py -m venv .venv

Ctrl+Shift+P => Python: Select Interpreter 

---------------------------------------------------------------------
docker build --tag python-docker-daint .

docker tag python-docker-daint:latest python-docker-daint:v1.0.0

docker run -d -p 8000:5000 python-docker-daint

docker run -d python-docker-daint

docker container logs python-docker-daint

docker rmi python-docker-daint