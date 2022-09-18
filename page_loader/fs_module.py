from page_loader.app_logger import get_logger
from page_loader.exc import KnownError
import os


def save_data(path, data_to_save, access_mode='w'):
    logger = get_logger(__name__)
    try:
        with open(path, access_mode) as output_file:
            output_file.write(data_to_save)
    except PermissionError as perm_err:
        logger.info('Permission error. Data was not saved')
        raise KnownError() from perm_err


def make_dir(resource_dir_path):
    logger = get_logger(__name__)
    try:
        os.mkdir(resource_dir_path)
        logger.info('The folder is created')
    except FileExistsError:
        logger.info('The folder is already exist')
    except PermissionError as perm_err:
        logger.info(
            'Permission error. Web-page resources will not be saved',
        )
        raise KnownError() from perm_err
