PyConUK 2018 : Kubernetes Workshop
https://kubernetes.io/docs/reference/kubectl/cheatsheet/

- Kubernetes atom is a pod that contains any amount of containers. (1-1 / 1-many relationship between pods and containers)
- Needs a container, not necessary to use Docker
-pod: contain mul containers, kube's atom which holds containers (can have 1-1 rel)


# Setup:
- Create VM with RAM 2048MB
- Linux Ubuntu 64-bit

VM Network settings:
Adapter advance : Port forwarding
host port : 2222
guest port: 22

- start VM and use terminal:
ssh osboxes@127.0.0.1 -p 2222
pw : osboxes.org 


### Kubernetes
$ kubectl 

kubectl get pods --all-namespaces
kubectl delete deployment--all
kubectl delete servies --all

FLASK_APP ./hello.py


## Docker
- Create dockerfile
- docker build -t hello:local (-t to tag it by name)
- docker images | grep hello (get list of images)
- run the image: docker run -d --net host hello:local (-d for detached mode)
- bg (unix command: run in background)
- curl localhost:5000
- docker logs -f <image id>
- lsof -i:5000 (to check port)

## 

$ipython
import code
console = code.InteractiveConsole()
console.push("a=5")
console.push("print(a)")




## Step1
- webconsole.py:
contextlib takes over ip/op for Interactive console


## Step2 : Kubernetes
- Step2 : run ./build.sh
master node connects to the indv kub api

$ kubectl run webconsole \
--image pycon...:step2
--port 5000
--replicas 2 (run two instances)
--expose
--dry-run
-o yaml (output format)
(webconsole: name of object to create aka containers (in this case is docker))

    [
        service/webconsole created
        deployment.apps/webconsole created
    ]   


--> Randomize pods being used, so variables defined in one pod is inaccessible in others.. this is the problem for assignment #2


$ kubectl get pods

$ kubectl get services
$ export WEBCONSOLE_IP=$(kubectl get service webconsole -o go-template="{{ .spec.clusterIP }}")
$ echo $WEBCONSOLE_IP
$ipython
>>import requests
>>requests.post(f'http://{os.environ["WEBCONSOLE_IP"]}:5000/api/ali/run', json={'input': 'print("Helloworld")'}).json() 

$ kubectl scale deployment webconsole --replicas 5
$ kubectl delete pods <pod id>
(replicas will ensure it will always run that amount of instances, even if nodes goes down, it will restart another one)
(master can have a replica as well)


### Kube Manifesto:
example.yaml file

Job Object
- different from kube podsgi cause it will exit/end when specified instead of re-creating new pod as specified by number of replicas
- runs into completion


## Step3
kubectl delete deployment webconsole
kubectl delete service wbconsole
./build.sh
kubectl apply -f step3/consolehub/deployment.yaml

kubectl get jobs

--> Don't SSH into prod pod, can create a debug pod to play around with it instead of actual prod pod


## Step4

ConfigMap : pass configurations to application (name + data)
e.g: env
list the references to the configmap file


### DOcker and kubernetes integration:
minicube

kubernetes ingress - expose to the internet

production - e.d: use service google cloud