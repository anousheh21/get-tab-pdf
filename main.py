import argparse
from getUrls import getUrls
from selectWindow import selectWindow
from singlePdfDownload import downloadPdf

parser = argparse.ArgumentParser()
parser.add_argument('downloadDestination')
args = parser.parse_args()

def main():
    selectedWindow = selectWindow()
    urls = getUrls(selectedWindow)

    for url in urls:
        downloadPdf(url, args)


if __name__ == "__main__":
    main()