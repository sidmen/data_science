import os
import requests
from requests import session
import logging

parent_url = 'https://www.kaggle.com'
kaggle_username = os.environ['KAGGLE_USERNAME']
kaggle_password = os.environ['KAGGLE_PASSWORD']
login_url = parent_url + '/account/login'
# csv_url = parent_url + '/c/titanic/download/train.csv'

payload = {
    'action': 'login',
    'username': kaggle_username,
    'password': kaggle_password
}


def extract_data(url, file_path):
    with session() as c:
        c.post(login_url, data=payload)
        with open(file_path, 'w') as handle:
            response = c.get(url, stream=True)
            for block in response.iter_content(1024):
                handle.write(block)


def main(project_dir):
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    train_url = parent_url + '/c/titanic/download/train.csv'
    test_url = parent_url + '/c/titanic/download/test.csv'
    raw_data_path = os.path.join(project_dir, 'data', 'raw')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')
    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)
    logger.info('downloaded raw training and test data')


if __name__ == '__main__'
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    main(project_dir)
