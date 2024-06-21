from abc import ABC, abstractmethod

from modules.loan_application.domain.entities import LoanApplication


class LoanApplicationPersistencePort(ABC):
    @abstractmethod
    def create(self, loan_application: LoanApplication) -> None:
        raise NotImplementedError
