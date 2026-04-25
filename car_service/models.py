from django.db import models


# 1
class Position(models.Model):
    idPosition = models.AutoField(primary_key=True)
    positionName = models.CharField(max_length=45)

    class Meta:
        db_table = 'position'
        managed = False

    def __str__(self):
        return self.positionName


# 2
class ServiceCenter(models.Model):
    idServiceCenter = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phoneNumber = models.CharField(max_length=13)

    class Meta:
        db_table = 'service_center'
        managed = False

    def __str__(self):
        return f"{self.name} ({self.address})"


# 3
class Employee(models.Model):
    idEmployee = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    idPosition = models.ForeignKey(Position, db_column='idPosition', on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=13)
    email = models.CharField(max_length=45, null=True)
    idServiceCenter = models.ForeignKey(ServiceCenter, db_column='idServiceCenter', on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'
        managed = False

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


# 4
class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    phoneNumber = models.CharField(max_length=13)
    email = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'client'
        managed = False

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


# 5
class Car(models.Model):
    idCar = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    yearOfRelease = models.PositiveSmallIntegerField()
    vin = models.CharField(max_length=45)
    licensePlate = models.CharField(max_length=45)

    class Meta:
        db_table = 'car'
        managed = False

    def __str__(self):
        return f"{self.brand} {self.model} ({self.licensePlate})"


# 6
class Part(models.Model):
    idPart = models.AutoField(primary_key=True)
    partName = models.CharField(max_length=45)
    manufacturer = models.CharField(max_length=45)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'part'
        managed = False

    def __str__(self):
        return self.partName


# 7
class Service(models.Model):
    idService = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    baseCost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'service'
        managed = False

    def __str__(self):
        return self.serviceName


# 8
class Repair(models.Model):
    idRepair = models.AutoField(primary_key=True)
    idCar = models.ForeignKey(Car, db_column='idCar', on_delete=models.CASCADE)
    idClient = models.ForeignKey(Client, db_column='idClient', on_delete=models.CASCADE)
    idServiceCenter = models.ForeignKey(ServiceCenter, db_column='idServiceCenter', on_delete=models.CASCADE)
    acceptenceDate = models.DateField()
    completionDate = models.DateField(null=True)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'repair'
        managed = False

    def __str__(self):
        return f"Repair #{self.idRepair} - {self.status}"


# 9
class RepairDetail(models.Model):
    idRepairDetail = models.AutoField(primary_key=True)
    idRepair = models.ForeignKey(Repair, db_column='idRepair', on_delete=models.CASCADE)
    idService = models.ForeignKey(Service, db_column='idService', null=True, on_delete=models.CASCADE)
    idPart = models.ForeignKey(Part, db_column='idPart', null=True, on_delete=models.CASCADE)
    count = models.IntegerField()
    additionalCost = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'repair_detail'
        managed = False

    def __str__(self):
        return f"RepairDetail #{self.idRepairDetail} (Repair {self.idRepair.idRepair})"
