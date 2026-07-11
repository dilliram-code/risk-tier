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

# create bmi: computed field
@computed_field
@property
def bmi(self) -> float:
  return self.weight / (self.height**2)

# create lifestyle_risk: computed field
@computed_field 
@property 
def lifestyle_risk(self) -> str:
  if self.smoker and self.bmi > 30:
    return "high"
  elif self.smoker and self.bmi > 27:
    return "medium"
  else: 
    return "low"