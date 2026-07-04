import subprocess

def getUrls(selectedWindow):
    selectedWindowUrls = subprocess.run(
        ["osascript", "getUrls.applescript", selectedWindow],
        capture_output=True,
        text=True
    )

    urls = []

    for selectedWindowUrl in selectedWindowUrls.stdout.splitlines():
        urls.append(selectedWindowUrl)
    
    return urls



if __name__ == "__main__":
    selectedWindow = "AppleScript Beginner Tutorial"
    urls = getUrls(selectedWindow)
    print(urls)