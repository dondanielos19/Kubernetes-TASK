## Kubernetes task 2
## TASK
Open simple Vote-app in minikube. Apps need work like image saple architecture_VOTE_APP.png in folder. Using this steps:
1. Download files from this repository /task2/
2. Create images in docker from folders: result, vote, worker. They had dockefile inside
3. Tag your images and push to your dockerhub repository
4. Create kubernetes files:
 voting-app-service.yaml ( type: LoadBalancer, port: 80)   voting-app-deploy.yaml ( 1 replica, using ur image from dockerhub create from /vote/)
 result-app-service.yaml (type: LoadBalancer, port: 80)
 result-app-deploy.yaml ( 1 replica, using ur image from dockerhub created form /worker/)
 postgres-service.yaml ( type: ClusterIP, port: 5432)
 postgres-deploy.yaml ( 1 replica, image: postgres, env:- name: POSTGRES_USER  value: "postgres", name: POSTGRES_PASSWORD 
 value: "postgres", name: POSTGRES_HOST_AUTH_METHOD  value: trust)
 redis-service.yaml ( type: ClusterIP, port: 6379)
 redis-deploy.yaml (  1 replica, image: redis)
5. Create all deployments and services
6. Check your Vote-app is working.

## Answer
1. Use command:```git clone https://github.com/dondanielos19/Kubernetes-TASK.git```
2. Go to folder task2
3. In folder /task2/vote use ``` docker build . -t vote``` next ``` docker tag vote username/image:tag ```
 after ``` docker push username/image:tag```
Do same steps to folder /result/ and /worker/
4. Wrtie all deployments and service yaml files in 1 folder ## u can check my files in folder /kubernetesfile/
5. Use commend ``` kubectl create -f .
6. Next ```kubectl get all``` or ```kubectl get serivce```
7. Write ```kubectl minikube service your_service_name_with_vote_app``` & ```kubectl minikube service your_service_name_with_result```
