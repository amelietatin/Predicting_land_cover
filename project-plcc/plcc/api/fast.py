import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException, Query
from taxifare.params import *
from taxifare.ml_logic.preprocessor import preprocess_features
from taxifare.ml_logic.registry import load_model
from datetime import datetime
import pytz

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#@app.on_event("startup")
#def startup_event():
app.state.model = load_model()

# define function to convert model to timezone


@app.get("/predict")
def predict(
        pickup_datetime: str,
        pickup_longitude: float,
        pickup_latitude: float,
        dropoff_longitude: float,
        dropoff_latitude: float ,
        passenger_count: int
    ):
    """
    Make a single course prediction.
    Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    """


        # build the feature vector

    X_pred= pd.DataFrame(locals(), index=[0])
    X_pred['pickup_datetime']= pd.Timestamp(pickup_datetime, tz="US/Eastern")

    # preprocess the features to match the model input
    X_processed = preprocess_features(X_pred)

    # make sure the datetime is in the correct format expected by the model
    #df['pickup_datetime'] = df['pickup_datetime'].map(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))

    # predict
    prediction = app.state.model.predict(X_processed)

    # return prediction in JSON format
    return {"fare": float(prediction)}

"""if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)"""

@app.get("/")
def root():
    return {"greeting": "Hello"}
