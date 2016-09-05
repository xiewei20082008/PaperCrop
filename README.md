# PaperCrop

## Introduction

This is a tool for making the acadamic PDF file suitable for e-readers such as Kindle, Kobo and so on. This tool is based on Magick.

You may follow these instructions:
- Crop a PDF file into single-column file.(Briss recommanded.)
- Transform the single-colmn PDF into an integrated PNG file. (Magick recommanded)
  - the magick command: magick convert -quality 100 -transparent white -antialias -resize 718x -density 1200 -colorspace gray -depth 4 -append “Research and Thinking of Smart Home Technology_cropped.pdf” image.png
- Transform the PNG file into multiple PNG files (The step is what this project deals with. It is used for cropping with overlap)
  - the command: 'paperCrop.py p image.png' or 'paperCrop.py l image.png', where 'p' means portrait mode and 'l' means landscape mode.
- Merge all the PNG into a MOBI format. (ChainLP recommanded)
