# center-fuge.py
# Steven T Hanna

"""center-fuge
A CLI to keep your deployment keys safe in open source projects

Usage:
    center-fuge.py generate
    center-fuge.py encrypt
    center-fuge.py decrypt

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt


if __name__ == "__main__":
    arguments = docopt(__doc__, version='center-fuge 1.0')
    

    # main()
