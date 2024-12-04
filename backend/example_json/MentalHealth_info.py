from pydantic import BaseModel, Field

class MentalHealthPredictionModel(BaseModel):
    Age: int = Field(..., example=35)
    Marital_Status: str = Field(..., example="Married")
    Education_Level: str = Field(..., example="Bachelor's Degree")
    Number_of_Children: int = Field(..., example=2)
    Smoking_Status: str = Field(..., example="Non-smoker")
    Physical_Activity_Level: str = Field(..., example="Active")
    Employment_Status: str = Field(..., example="Employed")
    Income: float = Field(..., example=60000.0)
    Alcohol_Consumption: str = Field(..., example="Moderate")
    Dietary_Habits: str = Field(..., example="Healthy")
    Sleep_Patterns: str = Field(..., example="Good")
    History_of_Substance_Abuse: str = Field(..., example="No")
    Family_History_of_Depression: str = Field(..., example="Yes")
    Chronic_Medical_Conditions: str = Field(..., example="No")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "Age": 35,
                "Marital_Status": "Married",
                "Education_Level": "Bachelor's Degree",
                "Number_of_Children": 2,
                "Smoking_Status": "Non-smoker",
                "Physical_Activity_Level": "Active",
                "Employment_Status": "Employed",
                "Income": 60000.0,
                "Alcohol_Consumption": "Moderate",
                "Dietary_Habits": "Healthy",
                "Sleep_Patterns": "Good",
                "History_of_Substance_Abuse": "No",
                "Family_History_of_Depression": "Yes",
                "Chronic_Medical_Conditions": "No"
            }
        }
