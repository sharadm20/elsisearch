# from elasticsearch_dsl.connections import connections
# from elasticsearch_dsl import DocType, Text, Index, fields
# from elasticsearch.helpers import bulk
# from elasticsearch import Elasticsearch
# from .models import CollegeList

# connections.create_connection()

# class CollegeListIndex(DocType):
#     clg_code = Text()
#     college_name = Text()
#     state = Text()
#     address = Text()

#     class Meta:
#         model=CollegeList
#         index = 'collegelist-index'

# def bulk_indexing():
#     CollegeListIndex.init()
#     es= Elasticsearch()
#     bulk(client=es, actions=(b.indexing() for b in
#     CollegeList.objects.all().iterator()))
