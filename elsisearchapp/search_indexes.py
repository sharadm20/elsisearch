import datetime
from haystack import indexes
from . import models


class CollegeListIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    clg_code = indexes.CharField(model_attr='clg_code')
    college_name = indexes.CharField(model_attr='college_name')
    state = indexes.CharField(model_attr='state')
    address= indexes.CharField(model_attr='address', null=True)
    
    def get_model(self):
        return models.CollegeList

    def index_queryset(self, using=None):
            return self.get_model().objects.all()