from typing import Annotated
from fastapi import Depends
from utilities.unit_of_work import AbstractUnitOfWork, UnitOfWork


UOWDep = Annotated[AbstractUnitOfWork, Depends(UnitOfWork)]
