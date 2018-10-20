import argparse
from .video import clip_duration


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "Positive number is required. %s is invalid" % value)
    return ivalue


parser = argparse.ArgumentParser(
    description='Create loops of a video. Clips are overlapped with fade transition.')
parser.add_argument('file', metavar='FILENAME', type=argparse.FileType('rb'),
                    help='Video file whose loop is required')

parser.add_argument('-d', '--duration', metavar='SECONDS', type=check_positive,
                    help='Fade transition duration')

required = parser.add_argument_group('required arguments')
required.add_argument('-t', '--time', metavar='MINUTES', required=True, type=check_positive,
                      help='Required duration of the video loop')


def main():
    args = parser.parse_args()
    print(args.file.name)
    clip_duration(args.file.name)


if __name__ == '__main__':
    main()
