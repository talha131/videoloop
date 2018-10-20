import argparse
import sys
from .video import clip_duration, concat_video


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
        print('Transition duration must be less than clip duration')
        print('Transition: {0} {2}\nClip: {1} {2}'.format(
            args.duration, clip_d, 'seconds'))
        sys.exit(1)
    if clip_d <= args.time:
        print('Required duration must be greater than clip duration')
        print('Required: {0} {2}\nClip: {1} {2}'.format(
            args.time * 60, clip_d, 'seconds'))
        sys.exit(1)

    # Formula is
    # count = (required_duration - transition_duration) / (clip_duration - transition_duration)
    # To get ceiling result,
    # (n + d - 1) /d
    count = int((args.time * 60 - args.duration + clip_d -
                 args.duration - 1) // (clip_d - args.duration))
    concat_video(args.file.name, count, args.duration)


if __name__ == '__main__':
    main()
