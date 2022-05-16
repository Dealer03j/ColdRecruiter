import argparse

def getArgs():
    parser = argparse.ArgumentParser(description='Gets list of new followers for website')
    parser.add_argument('-p', help='instagram password', dest='password', required=True)
    parser.add_argument('-u', help='instagram username', dest='username', required=True)
    parser.add_argument('-url', help='url to the instagram page you would like to keep track of', dest='url', required=True)

    args = parser.parse_args()
    return args


def main():
    args = getArgs()
    print(args.password)

    #to do, figure out what mvp is in this case and how to get it


if __name__ == "__main__":
    main()