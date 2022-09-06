"""Some description."""
import argparse
import sys
import os
from page_loader.page_loader import download


class KnownError(Exception):
    pass


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
    print(
        'Web page is saved to:\n{0}'.format(
            download(args.url_adress, args.output),
        ),
    )


if __name__ == '__main__':
    try:
        main()
        sys.exit()
    except KnownError:
        sys.exit(1)
