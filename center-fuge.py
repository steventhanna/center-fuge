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

# Handle command line arguments
def main(docopt_args):
    if docopt_args["decrypt"]:
        decrypt()
    elif docopt_args["encrypt"]:
        encrypt()
    elif docopt_args["generate"]:
        generate()
    else:
        print "Invalid Entry"

# Decrypt the keys
def decrypt():

# Encrypt the keys
def encrypt():

# Generate hash
def generate():



if __name__ == "__main__":
    arguments = docopt(__doc__, version='center-fuge 1.0')
    print arguments
    main(arguments)
    # main()
