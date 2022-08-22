"""Some description."""
import argparse
import sys
import os
import logging
from page_loader.page_loader import download
from page_loader.app_logger import get_logger


def main():
    """Run page loader."""
    logger = get_logger(__name__)
    dscr = 'Download web page to any local directory'
    parser = argparse.ArgumentParser(
        prog='page-loader',
        description=dscr,
    )
    parser.add_argument('--output')
    parser.add_argument('url_adress', nargs='?')
    args = parser.parse_args()
    logging.info('Web page is saved to:\n{0}'.format(
        download(args.url_adress, args.output),
    ),)


if __name__ == '__main__':
    try:
        main()
        sys.exit()
    except KnownError:
        sys.exit(1)
