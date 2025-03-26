from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Voter(models.Model):
    STAGE_OPTIONS = (
    ('Y1S1','Year1Sem1'),('Y1S2','Year1Sem2'),
    ('Y2S1','Year2Sem1'),('Y2S2','Year2Sem2'),
    ('Y3S1','Year3Sem1'),('Y3S2','Year3Sem2'),
    ('Y4S1','Year4Sem1'),('Y4S2','Year4Sem2'),
    )


    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    stage = models.CharField(max_length=20,choices=STAGE_OPTIONS)

class Deligate(models.Model):
    POSITION_OPTIONS = (
        ('MR','Male representative'),
        ('FR','Female representative'),
        ('AR','Academic representative'),
    )


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100,choices=POSITION_OPTIONS)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    reg_no = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    vote = models.IntegerField(default=0)

    def get_full_name(self):
        return f"{self.first_name } {self.last_name}"
    
