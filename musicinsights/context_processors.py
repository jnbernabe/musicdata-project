import os
from .models import Upload

def recent_uploads(request):
    # Fetch all uploads, ordered by newest first
    uploads = Upload.objects.order_by('-created_at')
    
    dashboard_list = []
    for u in uploads:
        # Use the filename as the dashboard name
        name = os.path.basename(u.original_file.name)
        dashboard_list.append({
            'id': u.id,
            'name': name,
            'date': u.created_at
        })
        
    return {'recent_uploads': dashboard_list}
