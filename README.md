# NeuralCollab
Recommender system using Neural Collaborative Filtering deployed on GCP via FastAPI


# Google Cloud 
Create instance via `Google CLI` in Ubuntu or `WSL`
```sh
gcloud config set project steam-recommender
```

Wait a few days and update quota for GPU-Global
https://console.cloud.google.com/iam-admin/quotas


```sh
export IMAGE_FAMILY="pytorch-latest-gpu"
export ZONE="us-west1-b"
export INSTANCE_NAME="my-fastai-instance"
export INSTANCE_TYPE="n1-highmem-8"

gcloud compute instances create $INSTANCE_NAME \
        --zone=$ZONE \
        --image-family=$IMAGE_FAMILY \
        --image-project=deeplearning-platform-release \
        --maintenance-policy=TERMINATE \
        --accelerator="type=nvidia-tesla-p100,count=1" \
        --machine-type=$INSTANCE_TYPE \
        --boot-disk-size=200GB \
        --metadata="install-nvidia-driver=True" \
        --preemptible
```

# FastAPI setup

Basic Workflow:
1. Import Packages
2. Create Our Route (/predict)
3. Load our Models and Vectorizer
4. Receive Input From Endpoint
5. Vectorize the data/name
6. Make our predictions
7. Send Result as JSON

```sh
$ pip install fastapi uvicorn
$ git clone https://github.com/lukexyz/NeuralCollab.git

$ cd app  
$ uvicorn app:app --reload  
```
```$ uvicorn (app.py):(app = FastAPI()) --reload```

#### Swagger UI 
```http://127.0.0.1:8000/docs```  
This yields the OpenAPI Swagger UI.  

or Redoc  
```http://127.0.0.1:8000/redoc```  
This uses the Redoc UI with some documentations out of the box.


### `GCloud` CLI

```sh
$ gcloud projects list 
# Show current project  
$ gcloud config get-value project  
$ gcloud config set project [projectname]
```

##### Deploying the app
```sh
$ gcloud app deploy
# Choose location ([15] us-west2)

$ gcloud app browser
# To open your app from the terminal
```










