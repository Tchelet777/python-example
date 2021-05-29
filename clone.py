import argparse
import subprocess

parser = argparse.ArgumentParser(description="clone repository")
parser.add_argument('-v', '--verbose',  action='store_true', required=False, default='', help='Run verbosely. Does not affect the reporting of progress status to the standard error stream.')
args = parser.parse_args()

def main(verbose):
    postfix = ''
    if verbose:
        postfix = '--verbose'
    print(postfix)
    subprocess.call('git clone https://github.com/Tchelet777/python-example.git ' + postfix, shell=True)

if __name__ == '__main__':
    main(verbose=args.verbose)
