from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId

# Create FastAPI app
app = FastAPI()

# MongoDB connection string
mongo_uri = "mongodb+srv://pyfbsdk59:NHd4ZEVmHONPZiYD@mongodb-restful.5xgpkpw.mongodb.net/?retryWrites=true&w=majority&appName=mongodb-restful"

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client["test"]
collection = db["s6r202403"]

# Pydantic model for schema validation
class S6r202403(BaseModel):
  cStockID: str
  cStockName: str
  cNewestSeason: str
  cNewestRev: str
  
  cSign1: str
  cSign2: str
  cSign3: str
  cSign4: str
  cSign5: str
  cSign6: str
  cAverageScore: str
  cLossGain: str
  CreateDate: str

  cRevN: str
  cRev: str
  ca1N: str
  ca2N: str
  ca3N: str
  ca4N: str
  ca5N: str 
  ca6N: str        
  ca7N: str

  cna1: str
  cna2: str
  cna3: str
  cna4: str
  cna5: str
  cna6: str 
  cna7: str
  cna9: str
  cna10: str
  cnewest_Rev_month: str
  cluX: str
  cnluX_MoM: str

  cProfitN: str
  cProfit: str
  cb1N: str
  cb2N: str
  cb3N: str
  cb4N: str
  cb5N: str
  cb6N: str       
  cb7N: str
  cb8N: str

  cb1: str
  cb2: str
  cb3: str
  cb4: str
  cb5: str
  cb6: str 
  cb7: str
  cb8: str
  cb9: str  
  cb10: str
  cb10p: str
  cInvTON: str
  cInvTO: str
  ce1N: str
  ce2N: str
  ce3N: str
  ce4N: str
  ce5N: str
  ce6N: str
  ce7N: str
  ce8N: str
  ce1: str
  ce2: str
  ce3: str
  ce4: str
  ce5: str
  ce6: str
  ce7: str
  ce8: str
  cnewest_Fin_Q: str
      
  cNetIncomeN: str
  cNetIncome: str
  cc1N: str
  cc2N: str
  cc3N: str
  cc4N: str
  cc5N: str
  cc6N: str      
  cc7N: str
  cc8N: str
  cc1: str
  cc2: str
  cc3: str
  cc4: str
  cc5: str
  cc6: str        
  cc7: str 
  cc8: str 
  cc9: str  
  cc10: str
  cc11: str
  cpc9: str 
  cpc10: str
  cpc11: str

  cEPSN: str
  cEPS: str
  cd1N: str
  cd2N: str
  cd3N: str
  cd4N: str
  cd5N: str
  cd6N: str
  cd7N: str
  cd8N: str
  cd1: str
  cd2: str
  cd3: str
  cd4: str
  cd5: str
  cd6: str
  cd7: str
  cd8: str
     
  cCashFlowN: str
  cCashFlow: str
  cf1N: str
  cf2N: str
  cf3N: str
  cf4N: str
  cf5N: str
  cf6N: str       
  cf7N: str
  cf8N: str
  cf1: str
  cf2: str
  cf3: str
  cf4: str
  cf5: str
  cf6: str        
  cf7: str
  cf8: str 
  cf9: str  
  cf10: str


# Routes
@app.get("/s6r202403/{stock_id}")
async def read_item(stock_id: str):
    item = collection.find_one({"cStockID": stock_id})
    return item
''''
@app.post("/items/")
async def create_item(item: Item):
    item_data = item.dict()
    item_id = collection.insert_one(item_data).inserted_id
    return {"item_id": str(item_id)}
''''
