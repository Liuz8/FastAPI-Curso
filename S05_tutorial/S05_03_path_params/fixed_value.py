from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resent = 'resent'
    lenet = 'lenet'

app = FastAPI()

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'Model_name': model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNC all the images'}
    
    return {'model_name': model_name, 'message': 'Have some residuals'}