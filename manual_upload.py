import os
import django
from django.core.files import File
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicdata.settings')
django.setup()

from musicinsights.models import Upload
from musicinsights.services.exportify_parser import parse_exportify_file

csv_path = Path(r'e:\Projects\musicdata-project\Your_Top_Songs_2024.csv')

with open(csv_path, 'rb') as f:
    upload = Upload.objects.create(original_file=File(f, name=csv_path.name))
    parse_exportify_file(upload)
    print(f"Upload created with ID: {upload.id}")
