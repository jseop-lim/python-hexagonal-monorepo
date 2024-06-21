from abc import ABC, abstractmethod
from modules.loan_application.application.port.inbound.dtos import (
    LoanApplicationCreationOutputData,
)


class LoanApplicationCreationUseCase(ABC):
    @abstractmethod
    def execute(self) -> LoanApplicationCreationOutputData:
        raise NotImplementedError
