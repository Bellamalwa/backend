from django.http import JsonResponse
from datetime import datetime, timedelta
from django.shortcuts import render

def get_info(request):
    slack_name = "bella"
    track = "backend"

    current_day = datetime.utcnow().strftime('%A')

    current_utc_time = (datetime.utcnow() + timedelta(minutes=2)).strftime('%Y-%m-%dT%H:%M:%SZ')

    github_repo_url = 'https://github.com/backend/repo'
    github_file_url = f'{github_repo_url}/blob/main/app.py'

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
