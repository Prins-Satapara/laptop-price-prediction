import pandas as pd
import joblib

from .config import MODEL_PATH

pipeline = joblib.load(MODEL_PATH)

import joblib
import pandas as pd

from .config import MODEL_PATH


# Load model once when API starts
pipeline = joblib.load(MODEL_PATH)


def predict_price(laptop):

    try:

        total_storage_capacity = (
            laptop.primary_storage_capacity
            + laptop.secondary_storage_capacity
        )

        total_pixels = (
            laptop.resolution_width
            * laptop.resolution_height
        )

        ppi = (
            (
                laptop.resolution_width ** 2
                + laptop.resolution_height ** 2
            ) ** 0.5
            / laptop.display_size
        )


        input_data = pd.DataFrame([{
            "brand": laptop.brand,
            "Rating": laptop.Rating,
            "processor_brand": laptop.processor_brand,
            "processor_tier": laptop.processor_tier,
            "num_cores": laptop.num_cores,
            "num_threads": laptop.num_threads,
            "ram_memory": laptop.ram_memory,
            "primary_storage_type": laptop.primary_storage_type,
            "primary_storage_capacity":
                laptop.primary_storage_capacity,
            "secondary_storage_type":
                laptop.secondary_storage_type,
            "secondary_storage_capacity":
                laptop.secondary_storage_capacity,
            "gpu_brand": laptop.gpu_brand,
            "gpu_type": laptop.gpu_type,
            "is_touch_screen":
                int(laptop.is_touch_screen),
            "display_size": laptop.display_size,
            "resolution_width":
                laptop.resolution_width,
            "resolution_height":
                laptop.resolution_height,
            "OS": laptop.OS,
            "year_of_warranty":
                laptop.year_of_warranty,

            # Engineered features
            "total_storage_capacity":
                total_storage_capacity,
            "total_pixels":
                total_pixels,
            "ppi": ppi
        }])


        prediction = pipeline.predict(input_data)[0]

        return round(float(prediction), 2)


    except Exception as e:
        raise RuntimeError(
            f"Prediction failed: {str(e)}"
        )