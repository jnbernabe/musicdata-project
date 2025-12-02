import os
import django
import sys

# Add the project directory to the sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicdata.settings')
django.setup()

from musicinsights.models import Upload
from musicinsights.services.exportify_parser import parse_exportify_file

def fix_data():
    u = Upload.objects.first()
    if u:
        print(f"Reparsing upload: {u.original_file.name}")
        parse_exportify_file(u)
        print("Done reparsing.")
    else:
        print("No upload found.")

if __name__ == "__main__":
    fix_data()
