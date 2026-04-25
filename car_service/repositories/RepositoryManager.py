from car_service.repositories.Repositories import *


class RepositoryManager:

    def __init__(self):
        self.position = PositionRepository()
        self.serviceCenter = ServiceCenterRepository()
        self.employee = EmployeeRepository()
        self.client = ClientRepository()
        self.car = CarRepository()
        self.part = PartRepository()
        self.service = ServiceRepository()
        self.repair = RepairRepository()
        self.repairDetail = RepairDetailRepository()
