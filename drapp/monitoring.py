import google.auth
from googleapiclient.discovery import build

class GoogleSearchConsole:
    def __init__(self):
        credentials, _ = google.auth.default()
        self.service = build('searchconsole', 'v1', credentials=credentials)

    def get_search_analytics(self):
        return self.service.searchanalytics().query(
            siteUrl='https://yourdomain.com',
            body={
                'startDate': '2023-01-01',
                'endDate': '2023-12-31',
                'dimensions': ['query', 'page']
            }
        ).execute()