def recent_uploads(request):
    # Fetch history from session
    history = request.session.get('history', [])
    
    # Reverse to show newest first
    dashboard_list = list(reversed(history))
        
    return {'recent_uploads': dashboard_list}
