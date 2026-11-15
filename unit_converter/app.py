from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict, StrictInt

from decimal import Decimal
from .domain import convert
class Conversion(BaseModel):
    model_config=ConfigDict(allow_inf_nan=False)
    kind:str;value:Decimal;source:str;target:str
def create_app():
    app=FastAPI(title='Unit converter')
    @app.get('/status')
    def status():return {'status':'ok'}
    @app.post('/convert')
    def run(p:Conversion):
        try:return convert(p.kind,p.value,p.source,p.target)
        except ValueError as exc:raise HTTPException(400,str(exc)) from None
    return app
app=create_app()
