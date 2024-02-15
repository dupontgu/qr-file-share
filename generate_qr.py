import sys
import base64
import qrcode
import urllib.parse

# Change this if you want to use decoding file hosted elsewhere
WEB_URL_PREFIX = "https://dupontgu.github.io/qr-file-share/dl.html"

if len(sys.argv) > 1:
    in_filename = sys.argv[1]
    out_filename = in_filename if len(sys.argv) == 2 else sys.argv[2]
else:
    print("Usage: python generate_qr.py inputfile [optional output filename]")
    exit(-1)

with open(in_filename, "rb") as f:
    file_data = f.read()
     
b64_file_data = base64.b64encode(file_data).decode('ascii')
url_file_data = urllib.parse.quote_plus(b64_file_data)
full_url = f"{WEB_URL_PREFIX}?f={out_filename}#{url_file_data}"
print("encoded url:", full_url)
qr_img = qrcode.make(full_url)
qr_img.save(f"{out_filename}_qr.png")
