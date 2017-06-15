#!/usr/bin/python
# download_file.py

#------------------------------------------------------------------------------
# This script will download a file using a provided URL
#------------------------------------------------------------------------------

# imports
import requests
try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    bundled = True
except:
    import urllib3
    from urllib3.exceptions import InsecureRequestWarning
    bundled = False


# -----------------------------------------------------------------------------
# download_file
# -----------------------------------------------------------------------------
def download_file(url, verify=True):
    if not verify:
        if bundled:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        else:
            urllib3.disable_warnings(InsecureRequestWarning)

    local_filename = url.split('/')[-1]
    try:
        r = requests.get(url, stream=True, verify=verify)
    except:
        print("Connection to server failed.")
        exit()

    if r.status_code != 200:
        print("Uh oh, something went wrong with the web request.")
        print("Error code:" + str(r.status_code))
        r.close()
        exit()

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
               f.write(chunk)
    return local_filename

if __name__ == "__main__":
    #--------------------------------------------------------------------------
    # get argument
    #--------------------------------------------------------------------------
    from sys import argv
    try:
        script, url = argv
    except:
        print("Usage: This script takes a URL as an argument and downloads " +\
                "the file at that URL.")
        exit()

    local_filename = download_file(url, verify=True)
