# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search_indexes import CollegeListIndex


class CollegeList(models.Model):
    clg_code = models.CharField(unique=True, max_length=6, blank=True, null=True)
    college_name = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=114, blank=True, null=True)
   
    def indexing(self):
        obj = CollegeListIndex(
            meta={'id': self.id},
            clg_code=self.clg_code,
            college_name=self.college_name,
            state=self.state,
            address=self.address,
         
        )
        obj.save()
        return obj.to_dic(include_meta=True)

    def __unicode__(self):
            return self.college_name

    class Meta:
        managed = False
        db_table = 'college_list'

