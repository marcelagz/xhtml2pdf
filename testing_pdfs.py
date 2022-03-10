import os
import shutil
import sys
from pathlib import Path

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from xhtml2pdf import pisa

sys.path.append(".")
sys.path.append("..")

os.chdir("test")

dir_temp = "../test_working/"
path_dir_temp = Path(dir_temp)
if path_dir_temp.is_dir():
    shutil.rmtree(path_dir_temp)
path_dir_temp.mkdir()


def convert_to_pdf_file(name, filename):
    from default import DEFAULT_CSS

    font_config = FontConfiguration()
    css = CSS(string=DEFAULT_CSS, font_config=font_config)
    HTML(name, encoding="utf-8").write_pdf(dir_temp+"weasy-" + filename, stylesheets=[css])

    with open(dir_temp + filename, "wb") as arch:

        with open(name, "r", encoding="utf-8", errors="ignore") as source:
            pisa.CreatePDF(source, arch, show_error_as_pdf=True)
            html_name = filename.replace(".pdf", ".html")

            with open(dir_temp+html_name, "w") as writer:
                source.seek(0)
                writer.write(source.read())

def testing_pdfs():

    dir = "."

    for path, dirc, files in os.walk(dir):
        for name in files:
            if name.endswith(".html"):
                filename = name.replace(".html", ".pdf")
                convert_to_pdf_file(name, filename)


if __name__=="__main__":
    pisa.showLogging()
    testing_pdfs()
    #convert_to_pdf_file("test-unicode-japanese.html", "test-unicode-japanese.pdf")