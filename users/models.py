from django.db import models

# Create your models here.

class teamMember(models.Model):
    name = 'tm'
    firstName = models.CharField(max_length = 64)
    lastName = models.CharField(max_length = 64)
    phone = models.CharField(max_length = 12)
    emailId = models.CharField(max_length = 96)
    role = models.CharField(max_length = 8)

    def __str__(self):
        return f"First Name: {self.firstName}\nLast Name: {self.lastName}\nPhone Number: {self.phone}\nEmail: {self.emailId}\nRole: {self.role}\n"
