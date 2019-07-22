import google.oauth2.credentials as cr
import google_auth_oauthlib.flow as fl
from config import config as cfg
from apiclient.discovery import build
from httplib2 import Http


def get_oauth_url(state):
    try:
        flow = fl.Flow.from_client_secrets_file(
            cfg.SECRET, cfg.SCOPES, redirect_uri=cfg.R_URI)
        url, state = flow.authorization_url(
            access_type='offline', state=state, include_granted_scopes='true')
        return {'status': 'success', 'url': str(url)}
    except:
        return {'status': 'failure', 'message': 'failed to return a URL'}


def get_credentials(redirectUrl):
    try:
        url = ''.join(redirectUrl)
        flow = fl.Flow.from_client_secrets_file(
            cfg.SECRET, None, redirect_uri=cfg.R_URI)
        flow.fetch_token(authorization_response=url)
        credentials = flow.credentials

        return {'status': 'success', 'credentials': {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes,
            'id_token': credentials.id_token
        }}
    except:
        return {'status': 'failure', 'message': 'unauthorized for some reason'}


def get_service(credentials_dict):
    credentials = cr.Credentials(token=credentials_dict['token'],
                                 refresh_token=credentials_dict['refresh_token'],
                                 id_token=credentials_dict['id_token'],
                                 token_uri=credentials_dict['token_uri'],
                                 client_id=credentials_dict['client_id'],
                                 client_secret=credentials_dict['client_secret'],
                                 scopes=credentials_dict['scopes'])

    # Build the service object.
    service = build('analytics', 'v3', credentials=credentials)

    return service


def get_v4_service(credentials_dict):
    credentials = cr.Credentials(token=credentials_dict['token'],
                                 refresh_token=credentials_dict['refresh_token'],
                                 id_token=credentials_dict['id_token'],
                                 token_uri=credentials_dict['token_uri'],
                                 client_id=credentials_dict['client_id'],
                                 client_secret=credentials_dict['client_secret'],
                                 scopes=credentials_dict['scopes'])

    # Build the service object.
    service = build('analytics', 'v4', credentials=credentials,
                    discoveryServiceUrl="https://analyticsreporting.googleapis.com/$discovery/rest")

    return service
