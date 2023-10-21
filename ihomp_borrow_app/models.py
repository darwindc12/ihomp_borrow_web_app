from django.db import models


STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_description


class Peripheral(models.Model):
    peripheral_id = models.AutoField(primary_key=True)
    peripheral_description = models.CharField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    unique_number = models.CharField(max_length=2000, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.peripheral_description


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_description = models.CharField(max_length=2000)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_description



class Borrow(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    borrower_name = models.CharField(max_length=2000)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    peripheral = models.ForeignKey(Peripheral, on_delete=models.PROTECT)
    unique_number = models.CharField(max_length=2000, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.borrower_name




