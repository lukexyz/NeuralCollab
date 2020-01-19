# Steam Dataset
An data exploration, visualisation, and machine learning project around the [Steam Dataset](https://steam.internet.byu.edu/) (2016)

## Exercise 1: Data Engineering
→ `01SteamGames.ipynb` / `01SteamGames.html`  

Pyspark notebook exploring the Steam Dataset, joining tables and some summary aggregation.

## Exercise 2: Analytics
→ `Mental_Health.twb` / `Mental_Health.png`  
→ `02HealthAnalytics.ipynb` / `02HealthAnalytics.html`  

Data engineering and a Tableau dashboard examining player behaviour. Games are filterable and the top players are 
highlighted along with the percentile distribution and average play-time per user.

The behaviour of the top users needs to be investigated further before any strong conclusions can be made about addictive behaviour. Long hours aren't what define video game addiction, 
it's more about negative behavioural side effects that users experience ([Web-MD](ww.webmd.com/mental-health/addiction/video-game-addiction))

Further analysis could look at the spending behaviour of users, or analyse the profiles of users who are known to have suffered from video game addiction, 
and build behavioural models which can identify problematic behaviour. 

## Exercise 3: Machine Learning
→ `02HealthAnalytics.ipynb` / `02HealthAnalytics.html`  

Using a proxy rating system, a recommendation engine is built to predict games for users.
`Collaborative filtering` is the method used, which assumes if person A has the same taste as a person B on a game,
A is likely to have B’s taste on a different game too. `Pytorch` and `fastai` libraries are used. 

A further `Neural Net Collaborative Filtering` model is trained, which builds on the collab model by passing the output of the embedding layers into a tabular NN before making the final prediction.

</br>

### Further Work:
* Put Collab NN behind the [FastAPI](https://fastapi.tiangolo.com/) wrapper 
```sh
$ uvicorn app:app --reload
```  

* Test with Swagger UI 
```
http://127.0.0.1:8000/docs
```    

* Freeze dependencies and build Dockerfile
```sh
FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 80
COPY . /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
```


* Deploy onto GCP app engine 
```sh
$ gcloud app deploy
```

</br>

#### Work Hours
`Exercise 1 Pyspark:` 2 hours  
`Exercise 2 Tableau:` 2-3 hours  
`Exercise 3 NNCollab:` 6 Hours  

</br>

Luke Woods (January 2020)

