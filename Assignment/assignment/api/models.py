from django.db import models

# Create your models here.
class Invoice(models.Model):
    Date = models.DateField()
    CustomerName = models.CharField(max_length = 255)

    def __str__(self):
        return self.CustomerName
class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name = 'details', on_delete = models.CASCADE)
    description = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice Detail for {self.invoice.id}"
    


