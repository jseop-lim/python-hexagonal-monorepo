from pydantic import BaseModel


class LoanApplicationCreationResponse(BaseModel):
    id: int
