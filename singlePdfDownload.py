import requests
from pathlib import Path

# import os
# from dotenv import load_dotenv


# load_dotenv()
# cookie = os.getenv("AUTH_COOKIE")

def getPdf(pdfUrl):
    # headers = {
    #     "Cookie": cookie
    # }

    # response = requests.get(pdfUrl, headers=headers)
    response = requests.get(pdfUrl)

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



# if __name__ == "__main__":
#     testUrl = 'https://arxiv.org/pdf/1905.11481'
#     downloadPdf(testUrl)

