from fastapi import FastAPI 
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Optional, Annotated
import pickle 
import pandas as pd 

# import ml model
with open("model.pkl", 'rb') as f:
  model = pickle.load(f)

app = FastAPI()

# pydantic model to validate input data
class UserInput(BaseModel):
  age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')] 
  weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
  height: Annotated[float, Field(..., gt=0, le=2.5, description='Height of the user')] 
  income_lpa: Annotated[float, Field(..., gt=0, description='Income of the user')] 
  smoker: Annotated[bool, Field(..., description='Smoking: Yes or No')] 
  city: Annotated[str, Field(..., description='City of the user')] 
  occupation: Annotated[Literal['','',''], Field(..., description='Occupation of the user')] 