import argparse
import sys
import os
from .helper import check_positive, seconds_to_text
from .video import clip_duration, concat_video


parser = argparse.ArgumentParser(
    description='Create loops of a video. Clips are overlapped with fade transition.')
parser.add_argument('file', metavar='FILENAME', type=argparse.FileType('rb'),
                    help='Video file whose loop is required')

parser.add_argument('-o', '--output', metavar='OUTPUT_FILENAME', type=str,
                    help='Output video file name. Default is FILENAME_MINUTES.mp4. WARNING: Overwrites existing file.')

exclusive = parser.add_mutually_exclusive_group(required=True)
exclusive.add_argument('-d', '--duration', metavar='SECONDS', type=check_positive, default=2,
                       help='Fade transition duration')
exclusive.add_argument('-dh', '--duration-half', action='store_true',
                       help='If present then fade transition duration is set to half of clip duration')
exclusive.add_argument('-dq', '--duration-quarter', action='store_true',
                       help='If present then fade transition duration is set to quarter of clip duration')

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
    if clip_d >= (args.time * 60):
        print('Required duration must be greater than clip duration')
        print('Required: {0} {2}\nClip: {1} {2}'.format(
            args.time * 60, clip_d, 'seconds'))
        sys.exit(1)

    # Output file name
    temp = os.path.splitext(args.file.name)
    args.output = args.output if args.output else f'{temp[0]}_{args.time}{temp[1]}'

    # transition duration
    t_duration = int(args.duration)
    if args.duration_half:
        t_duration = int(clip_d // 2)
    elif args.duration_quarter:
        t_duration = int((clip_d + 4 - 1) // 4)

    # Formula is
    # count = (required_duration - transition_duration) / (clip_duration - transition_duration)
    # To get ceiling result,
    # (n + d - 1) /d
    count = int((args.time * 60 - args.duration + clip_d -
                 t_duration - 1) // (clip_d - t_duration))
    if count <= 1:
        print(f'Clip should be concatenated at least twice')
        print(f'Count: {count}')
        print(f'Clip Duration: {clip_d}')
        print(f'Required Duration: {args.time}')
        print(f'Transition Duration: {t_duration}')
        sys.exit(1)

    concat_video(args.file.name, count, t_duration, args.output)
    print(f'Output duration: {seconds_to_text(clip_duration(args.output))}')
    print(f'Clip Duration: {clip_d}\tTransition Duration: {t_duration}')
    sys.exit(0)


if __name__ == '__main__':
    main()
