# scraping adobe converter site

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/selenium) ![PyPI - Version](https://img.shields.io/pypi/v/selenium) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/selenium) ![GitHub repo size](https://img.shields.io/github/repo-size/OneCbyte/scraping_adobe)

**scraping_adobe** - this is a script written in Python using the [Selenium web driver](https://pypi.org/project/selenium/) for testing, to automatically convert a PDF file to XLSX format using the [Adobe website](https://www.adobe.com/acrobat/online/pdf-to-excel.html)

## Installation

Install the current version with [PyPI](https://pypi.org/project/selenium/):

```bash
pip install selenium
```

## Usage


### How and where to use it?

You can use this in your projects, for example, in my [telegram bot](https://t.me/excelifybot), written to simplify work with documents, this function is used to the maximum

To install the output file in the directory you need, specify it (in place of ```r"your_location"```)

```bash
def conversion(url, file_path):
    # adding settings for saving to the desired directory
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": r"your_location"
    })
```

On average, the conversion takes less than a minute, and most importantly, the conversion occurs at a high level; Adobe can even cope with complex, multi-page and tabular PDF files.

It is completely free and has no usage restrictions, unlike the [Adobe Acrobat API](https://developer.adobe.com/document-services/apis/pdf-services/), where there is a limit of 500 calls per month.
___

<h2 align="center">Thanks for using my software!❤️</h2>
