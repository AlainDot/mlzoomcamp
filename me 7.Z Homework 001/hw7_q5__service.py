print('***** Starting hw5_q5_service.py 18:10 *****')

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


print('** Get mmodel **')
modBnt = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")

print('** Run mmodel **')

modBntRun = modBnt.to_runner()


svc = bentoml.Service("hw7_q5_service", runners=[modBntRun])

@svc.api(input=NumpyNdarray(), output=JSON())

async def classify(UserProfile):
    print('** in classify **')
    print('> UserProfile :' , UserProfile)
    prd = await modBntRun.predict.async_run(UserProfile)
    print('> prd = ' , prd)
    return( { "prediction" : prd  })

"""
def classify(UserProfile):
    print('** in classify **')
    print('> UserProfile :' , UserProfile)
    prd = modBntRun.predict.run(UserProfile)
    print('> prd = ' , prd)
    return( { "prediction" : prd  })
"""
