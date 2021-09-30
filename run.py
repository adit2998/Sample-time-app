from logging import currentframe
from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def return_time():
    
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    return str(current_time)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)

# docker build -t aditkotwal/sample-time-app:latest .
# docker run --name sample-time-app -p 8080:8080 -it aditkotwal/sample-time-app:latest
# docker push aditkotwal/sample-time-app:latest
# Remove an existing container : docker rm name_of_container
# docker run -p 8080:8080 aditkotwal/sample-time-app:latest
# kubectl create deployment sample-time-app --image=docker.io/aditkotwal/sample-time-app:latest
# kubectl expose deployment/sample-time-app --type="NodePort" --port 8080
# kubectl get services