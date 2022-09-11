import argparse
import sys
import os
from page_loader.page_loader import download, KnownError


def main():
    """Run page loader."""
    dscr = 'Download web page to any local directory'
    parser = argparse.ArgumentParser(
        prog='page-loader',
        description=dscr,
    )
    parser.add_argument('url_adress', nargs='?')
    parser.add_argument(
        '-o',
        '--output',
        default='{}/'.format(os.getcwd()),
    )
    args = parser.parse_args()
    try:
        html_file_path = download(args.url_adress, args.output)
        print('Web page is saved to:\n{0}'.format(html_file_path))
        sys.exit()
    except KnownError:
        sys.exit(1)


if __name__ == '__main__':
    main()
