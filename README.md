# SSLooker

# Install Python3.7
Download version 3.7+ from: https://www.python.org/downloads/
- Best to install for all users and add to PATH during installation (Custom installation)
- Make sure 'pip --version' points at python3 installation
- Make sure python3 is on your PATH (option during installation)

# Install Pywin32
Download version 224+ from: https://github.com/mhammond/pywin32/releases
- It must detect the python3 version installed in the previous steps

# Install tesseract
Download version 5+ from: https://digi.bib.uni-mannheim.de/tesseract/
- Add tesseract to your PATH

# Install python-modules
- pip install pytesseract
- pip install pillow

# Configuration
Configure all settings in
'./SSLooker/env.json'

# Image quality fixes

https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality

# Usage

./python3 main.py
