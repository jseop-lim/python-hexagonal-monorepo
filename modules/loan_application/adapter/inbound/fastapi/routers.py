from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from loan_application.adapter.inbound.fastapi.schemas import (
    LoanApplicationCreationResponse,
)
from loan_application.application.port.inbound.dtos import (
    LoanApplicationCreationOutputData,
)
from loan_application.application.port.inbound.use_cases import (
    LoanApplicationCreationUseCase,
)  # NOTE: adapter.inbound.fastapi.schemas.LoanApplicationCreationResponse


router = APIRouter()


@router.post("/loan-applications", status_code=201)
@inject
async def create_loan_application(
    use_case: LoanApplicationCreationUseCase = Depends(
        Provide["loan_application_creation_use_case"]
    ),
) -> LoanApplicationCreationResponse:
    output_data: LoanApplicationCreationOutputData = use_case.execute()
    return LoanApplicationCreationResponse(id=output_data.id)
