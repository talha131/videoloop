import argparse

parser = argparse.ArgumentParser(
    description='Create loops of a video. Clips are overlapped with fade transition.')
parser.add_argument('file', metavar='FILENAME',
                    help='Video file whose loop is required')

requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-t', '--time', metavar='MINUTES', required=True,
                           help='Required duration of the video loop')


def main():
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
