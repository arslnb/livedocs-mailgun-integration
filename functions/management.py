import google.oauth2.credentials
import google_auth_oauthlib.flow as fl
from config import config as cfg
from connect import get_service as gs


def get_accounts(args):
    try:
        service = gs(args['service_auth'])
        # Use service object to pull list of accounts
        accounts = service.management().accounts().list().execute()

        cleaned_accounts = []

        for account in accounts['items']:
            cleaned_accounts.append({
                'text': account['name'],
                'value': account['id']
            })
        return {'status': 'success', 'data': {'entries': cleaned_accounts}}
    except Exception as error:
        return {'status': 'failure', 'error': error}


def get_properties(args):
    try:
        service = gs(args['service_auth'])
        account_id = args['accounts']

        # Use account ID to get properties
        properties = service.management().webproperties().list(
            accountId=account_id).execute()

        cleaned_props = []

        for prop in properties['items']:
            cleaned_props.append({
                'text': prop['name'],
                'value': prop['id']
            })
        return {'status': 'success', 'data': {'entries': cleaned_props}}
    except Exception as error:
        return {'status': 'failure', 'error': error}


def get_views(args):
    try:
        service = gs(args['service_auth'])
        account_id = args['accounts']
        property_id = args['properties']

        views = service.management().profiles().list(
            accountId=account_id,
            webPropertyId=property_id).execute()

        cleaned_views = []

        for view in views['items']:
            cleaned_views.append({
                'text': view['name'],
                'value': view['id']
            })
        return {'status': 'success', 'data': {'entries': cleaned_views}}
    except Exception as error:
        return {'status': 'failure', 'error': error}
