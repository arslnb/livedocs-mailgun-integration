import google.oauth2.credentials
import google_auth_oauthlib.flow as fl
from config import config as cfg
from connect import get_v4_service as gs
from datetime import datetime
from datetime import date
from datetime import timedelta
from apiclient.errors import HttpError
import json


def get_bouncerate(args):
    try:
        service = gs(args['service_auth'])
        view_id = args['view']

        today = datetime.today().strftime('%Y-%m-%d')
        _yd = date.today() - timedelta(days=1)
        yesterday = _yd.strftime('%Y-%m-%d')

        report = service.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': view_id,
                        'dateRanges': [{'startDate': yesterday, 'endDate': today}],
                        'metrics': [{'expression': 'ga:bounceRate'}]
                    }]
            }
        ).execute()

        first_value = report['reports'][0]['data']['totals'][0]['values'][0]
        return {'status': 'success', 'data': {
            'returned_val': first_value
        }}
    except Exception as error:
        message = json.loads(error.content)['error']['message']
        return {'status': 'failure', 'error': message}
