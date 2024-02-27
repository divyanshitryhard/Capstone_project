# Capstone_project
Capstone_project
Project 1:
1.	Create a requirement file with Django==2.2.5 so that it will be installed with pip and passing file as argument
2.	Install Django using command pip install -r requirements.txt
3.	Create a new project Capstone using Django command
a.	django-admin startproject Capstone_kube
4.	Run and verify if Django homepage is visible on localhost:8000
 
5.	Create a docker file which installs ubuntu, and pip
6.	Copy all files in current path to container path
7.	Expose port 8000 and run Django
8.	Build the docker file using command docker build -t python-django-app
9.	Run the docker image locally and verify if website is reachable using command 
docker run -p 80:8000 python-django-app
  
 
10.	Install minikube from official page
11.	Execute command minikube start and wait until created
 
12.	Push the docker image to docker repository
13.	Package is available as divsgup/djangokubernetesproject:latest
14.	Create a deployment file to use image divsgup/djangokubernetesproject:latest and expose container port 8000
 
15.	Create a service to access the webpage
 
16.	Access the webpage using the port of service
  
17.	Install the required plugin docker pipeline, kuberenetes on Jenkins.
18.	Add git credentials to Jenkins
19.	Add the following stages in pipeline
a.	Git checkout GitHub - divyanshitryhard/Capstone_project: Capstone_project
b.	Create docker image
c.	Push image to repository
d.	Deploy the pod and service using Kubernetes 
e.	Create the test by doing curl
 

20.	Run the pipeline
 

21.	Check minikube metrics
 
 
 
 

 
