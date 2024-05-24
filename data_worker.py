import io
from importer import im
import subprocess
requests=im("requests")

zipfile=im("zipfile")
def download_githab(url):
    return requests.get(url)

def repack(data, dir):
    with zipfile.ZipFile(data, 'r') as zip_ref:
        zip_ref.extractall(dir)

def repackFromgit(url, dir):
    response = download_githab(url)
    if response.status_code == 200:
        io_data = io.BytesIO(response.content)
        print(dir)
        repack(io_data, dir)
        print("End")
    else:
        print("Failed to download the file. Status code:", response.status_code)
def run(exe):
    subprocess.Popen(exe)
