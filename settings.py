from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin

# авторизация stage
ADMIN_LOGIN = '+79000000000'
ADMIN_PASSWORD = 'LUmfegXc33vJ'
KMP_API_STAGE_AUTH = HTTPBasicAuth(ADMIN_LOGIN, ADMIN_PASSWORD)
KMP_API_STAGE_ACCOUNT = HTTPBasicAuth(ADMIN_LOGIN, ADMIN_PASSWORD)
BETWEEN_SMS_CODE_REQUEST_TIMEOUT = 15

# дефолтные форматы даты и времени
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE_WITH_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# адрес сервиса backend kmp
BASE_URL = 'https://stage-keyauto.spider.ru/api/'

# настройки postgresql
STAGE_HOST = '193.168.49.9'
STAGE_PORT = 5432
STAGE_SERVER = STAGE_HOST + ':' + str(STAGE_PORT)
STAGE_LOGIN = 'keyauto'
STAGE_PASSWORD = 'Oon8eeshieg9'

# подключение к БД через SQLAlchemy
BASE_CONNECT_URL = f'postgresql+psycopg2://{STAGE_LOGIN}:{STAGE_PASSWORD}@{STAGE_SERVER}/'

KMP_DB_TWO_URL = BASE_CONNECT_URL + 'keyauto'

ACCOUNT_PATH = urljoin(BASE_URL, 'account/')
NOTIFICATION_SUMMARY_URL = urljoin(ACCOUNT_PATH, 'notification_summary/')
PROFILE_URL = urljoin(ACCOUNT_PATH, 'profile/')
PROFILE_RECOVERY_URL = urljoin(PROFILE_URL, 'recovery/')
USER_INFO_TESTING_URL = urljoin(ACCOUNT_PATH, 'user_info_testing/')

AUTH_PATH = urljoin(BASE_URL, 'auth/')
GET_TOKEN_URL = urljoin(AUTH_PATH, 'get-token/')
LOGOUT_URL = urljoin(AUTH_PATH, 'logout/')
SEND_SMS_URL = urljoin(AUTH_PATH, 'send-sms/')
CARS_URL = urljoin(AUTH_PATH, 'cars/')

# статус - коды
SUCCESS = 200
CREATED = 201
NO_CONTENT = 204
BAD_REQUEST = 400
NOT_FOUND = 404
