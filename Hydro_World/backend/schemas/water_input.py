from pydantic import BaseModel


class WaterInput(BaseModel):
    pH: float
    turbidity: float
    electrical_conductivity: float
    tds: float
    dissolved_oxygen: float
    temperature: float
    hardness: float
    alkalinity: float
    chloride: float
    sulfate: float
