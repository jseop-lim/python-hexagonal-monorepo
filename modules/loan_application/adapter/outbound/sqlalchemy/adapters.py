from sqlalchemy.orm import Session
from modules.loan_application.domain.entities import (
    LoanApplication as LoanApplicationEntity,
)
from loan_application.adapter.outbound.sqlalchemy.models import (
    loan_applications,
)
from loan_application.application.port.outbound.ports import (
    LoanApplicationPersistencePort,
)


class SQLAlchemyLoanApplicationPersistenceAdapter(LoanApplicationPersistencePort):

    def __init__(self, session: Session):
        self.session = session

    def create(self, loan_application: LoanApplicationEntity) -> None:
        self.session.execute(
            loan_applications.insert().values(
                id=loan_application.id,
            )
        )
        self.session.commit()
