# qr-file-share
Share small files from an offline source using only a QR code!

## Why?

Imagine: You want to share a file with a friend nearby. You want to share from a source that does not have internet access - you just want to beam the file directly to your friend. This system lets you _embed_ your file into a QR code that loads as an actual file download on your friend's device. Try it out here if you're feeling brave! The image that is downloaded by scanning this QR code **is not hosted on any server, it only lives _inside_ the QR code**.

![QR code with file embedded](.docs/wtf2.png_qr.png)

## Usage

To generate one of these QR codes, you can either:
1. use the [web app](https://dupontgu.github.io/qr-file-share/) (this can be saved to your computer to run offline).
2. use the included [python script](./generate_qr.py).