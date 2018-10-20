import argparse
import sys
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

parser.add_argument('-d', '--duration', metavar='SECONDS', type=check_positive, default=2,
                    help='Fade transition duration')

required = parser.add_argument_group('required arguments')
required.add_argument('-t', '--time', metavar='MINUTES', required=True, type=check_positive,
                      help='Required duration of the video loop')


def main():
    args = parser.parse_args()
    clip_d = clip_duration(args.file.name)
    if clip_d <= args.duration:
        sys.exit('Transition duration must be less than clip duration')
    if clip_d <= args.time:
        print('Required duration must be greater than clip duration')
        print('Required: {0} {2}\nClip: {1} {2}'.format(
            args.time * 60, clip_d, 'seconds'))
        sys.exit(1)


if __name__ == '__main__':
    main()
