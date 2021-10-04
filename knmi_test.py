import requests
from datetime import datetime, timedelta
import urllib

# API URL
api_url = 'https://api.dataplatform.knmi.nl/open-data/v1/datasets/Actuele10mindataKNMIstations/versions/2/files'

# Headers
api_key = 'eyJvcmciOiI1ZTU1NGUxOTI3NGE5NjAwMDEyYTNlYjEiLCJpZCI6ImNjOWE2YjM3ZjVhODQwMDZiMWIzZGIzZDRjYzVjODFiIiwiaCI6Im11cm11cjEyOCJ9'
headers = dict()
headers['Authorization'] = api_key

date = datetime.utcnow() - timedelta(minutes=60)
start_time_hour = date.strftime('%Y%m%d%H')
start_time_minute = (int(date.strftime('%M')) // 10) * 10
if start_time_minute == 0:
    start_time_minute = '00'

start_time = f'{start_time_hour}{start_time_minute}'

params = dict()
params['maxKeys'] = 10
params['startAfterFilename'] = f'KMDS__OPER_P___10M_OBS_L2_{start_time}'


response = requests.get(api_url, headers=headers, params=params)
response = response.json()
filename = response['files'][-1]['filename']

api_url = f'https://api.dataplatform.knmi.nl/open-data/v1/datasets/Actuele10mindataKNMIstations/versions/2/files/{filename}/url'
response = requests.get(api_url, headers=headers)
download_url = response.json()['temporaryDownloadUrl']

urllib.request.urlretrieve(download_url, f'C:\\Users\\arjan\\Downloads\\{filename}')
