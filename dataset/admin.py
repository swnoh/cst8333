from django.contrib import admin
from .models import Dataset

"""
File: admin.py
Modified By: Seungwan Noh
Modifed On: Dec 3, 2017
Description: Database admin registers Dataset from models.py. 
"""
# Set Dataset object that has an admin object.
admin.site.register(Dataset)