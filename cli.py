import argparse
from post_fetcher import fetch_posts


def get_posts(args):
    posts = fetch_posts(args.posts)


def check_value_within_range(value):
    iValue = int(value)
    if iValue < 1 or iValue > 100:
        raise argparse.ArgumentTypeError("%s is outside the accepted range. Choose a number between 1-100" % value)
    return iValue


def main():
    parser = argparse.ArgumentParser(
        prog='hackernews',
        description='A command line utility to fetch the top posts from Hacker News.'
    )
    parser.set_defaults(func=get_posts)

    parser.add_argument(
        '--posts',
        type=check_value_within_range,
        default=10,
        help='The number of posts to fetch. The default value is 10.'
    )

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
