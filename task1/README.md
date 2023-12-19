## Kubernetes task:   
1. Write simple application in "flask" with 2 environment variables. 
2. Write dockerfile, container app and send to dockerhub.
3. Create YAML deployment file. The deployment should run a Docker container using our image, and it should create 3 replicas of the container.
4. Create a Service: Write a YAML file to define a Service resource that exposes port 5000.
5. Create a ConfigMap and Secret: Write YAML files to define a ConfigMap and Secret resource, storing environment variables and sensitive information respectively.
6. Eploy the resources to a Kubernetes cluster, and open create app.



## Answer
1. Take app named: app.py from my github repository
2. Take dockfile from my github
   
   Write commends:
   ```
   docker build -t my-app . #build image
   ```
   ```
   docker tag my-app user/repository:tag              # tag ur app
   ```
   ```
   docker push user/repository:tag #push image to dockerhub
   ```
3-6. Take YAML files from my github repository        # change direction image in deployment.yaml

   Write commends:
   ```
   kubectl create -f .                                # create all yaml files
   ```
   kubectl get all                                    # check all paramets are working
   ```
   minikube service app-service # take url and check app



   

   
   
















