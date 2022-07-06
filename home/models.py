from django.db import models

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.TextField()
    doc_department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors/')
    def __str__(self):
        return self.doc_name

class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_email=models.EmailField()
    p_phone=models.CharField(max_length=100)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField() 
    booked_on=models.DateTimeField(auto_now_add=True)