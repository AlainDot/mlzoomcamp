print('***** Starting hw7_q6_service.py 17:41 *****')

import numpy as npy

import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray

from pydantic import BaseModel

print('** Import completed**')

class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float


print('** Get model **')

# for coolmodel.bentomodel Q5
#modBnt = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")

# for coolmodel2.bentomodel Q6
modBnt = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

print('** Run mmodel **')

modBntRun = modBnt.to_runner()


svc = bentoml.Service("hw7_q6_service", runners=[modBntRun])

@svc.api(input=NumpyNdarray(), output=JSON())

async def classify(UserProfile):
    print('** in classify **')
    print('> UserProfile :' , UserProfile)
    prd = await modBntRun.predict.async_run(UserProfile)
    print('> prd = ' , prd)
    return( { "prediction" : prd  })


