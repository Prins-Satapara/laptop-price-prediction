from pydantic import BaseModel, Field


class LaptopInput(BaseModel):
    brand: str
    Rating: float = Field(..., ge=0, le=100)

    processor_brand: str
    processor_tier: str

    num_cores: int = Field(..., gt=0)
    num_threads: int = Field(..., gt=0)

    ram_memory: float = Field(..., gt=0)

    primary_storage_type: str
    primary_storage_capacity: float = Field(..., ge=0)

    secondary_storage_type: str
    secondary_storage_capacity: float = Field(..., ge=0)

    gpu_brand: str
    gpu_type: str

    is_touch_screen: bool

    display_size: float = Field(..., gt=0)

    resolution_width: int = Field(..., gt=0)
    resolution_height: int = Field(..., gt=0)

    OS: str

    year_of_warranty: float | None = Field(
        default=None,
        ge=0
    )


class PredictionResponse(BaseModel):
    predicted_price: float
    currency: str
    message: str