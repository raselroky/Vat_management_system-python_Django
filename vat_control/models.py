from django.db import models

class VAT(models.Model):
    id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=200)
    customer_number=models.CharField(max_length=20)
    items=models.TextField()
    vat=models.TextField()
    discount=models.TextField()
    total_amount=models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.customer_name
    


