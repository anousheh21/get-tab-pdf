# import argparse
import os
import requests

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
cookie = os.getenv("AUTH_COOKIE")

# parser = argparse.ArgumentParser()
# parser.add_argument('downloadDestination')
# args = parser.parse_args()

# Remove this eventually as it will come automated
# pdfUrl = 'https://learn.lboro.ac.uk/pluginfile.php/2137213/mod_resource/content/10/25COC102_W1Lec2-Tools.pdf'

def getPdf(pdfUrl):
    headers = {
        "Cookie": cookie
    }

    response = requests.get(pdfUrl, headers=headers)

    return response



def checkUrlContentType(response):
    if response.status_code != 200:
        raise ValueError("None 200 Response: ", response.status_code)
    
    contentType = response.headers.get("Content-Type")
    return contentType



def checkValidDestination(args):
    path = Path.home() / args.downloadDestination.lstrip("/")

    if not path.is_dir(): 
        raise NotADirectoryError("Invalid directory")
    
    return path



def downloadPdf(url, args):
    response = getPdf(url)
    contentType = checkUrlContentType(response)
    downloadDir = checkValidDestination(args)

    if not contentType.lower() or contentType.split(";", 1)[0].strip().lower() != "application/pdf":
        # raise TypeError("Incorrect Content Type")
        return

    content_disposition = response.headers.get("Content-Disposition")
    filename = None
    
    if content_disposition:
        filename = content_disposition.split("filename=")[-1].strip('""')
    else:
        filename = "download.pdf"

    filePath = downloadDir / filename

    counter = 1

    while filePath.exists():
        filePath = downloadDir / f"{Path(filename).stem} ({counter}){Path(filename).suffix}"
        counter += 1

    filePath.write_bytes(response.content)

    print("File downloaded successfully!")



if __name__ == "__main__":
    testUrl = 'https://learn.lboro.ac.uk/pluginfile.php/2137213/mod_resource/content/10/25COC102_W1Lec2-Tools.pdf'
    downloadPdf(testUrl)

