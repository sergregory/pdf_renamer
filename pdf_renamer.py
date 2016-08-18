#! /usr/bin/python


import re
name_format = re.compile("([\d]{4})?-.*-.*\.pdf")


def process_directory(directory):
    '''
    lists all the files in a directory a performs processing via
    call to the process_one_file
    '''
    from pathlib import Path
    from os import path
    p = Path(directory)
    if not p.is_absolute():
        p = Path(path.abspath('.')).joinpath(p)
    fnames = list(p.glob('**/*.pdf'))
    for fname in fnames:
        process_one_file(p.joinpath(fname).resolve())


def process_one_file(pdf_file):
    '''
    extract metadata from the pdf document and rename it
    '''
    from PyPDF2 import PdfFileReader
    from shutil import move

    if name_format.match(pdf_file.name):
        return
    else:
        print(pdf_file.name)

    with pdf_file.open(mode="rb") as f:
        pdf = PdfFileReader(f)
        pdf_info = pdf.getDocumentInfo()
    author = pdf_info.get('/Author', "")
    if "/CreationDate" in pdf_info:
        year = pdf_info['/CreationDate'][2:6]
    else:
        year = ""
    title = pdf_info.get('/Title', "")
    if not author and not year and not title:
        return
    new_name = "{year}-{author}-{name}.pdf".format(year=year,
                                                   author=author,
                                                   name=title)
    new_name = new_name.replace(":", " ")
    if new_name != pdf_file.name:
        if not pdf_file.with_name(new_name).exists():
            move(str(pdf_file),
                 str(pdf_file.with_name(new_name)))
        else:
            pdf_file.unlink()
    # full_new_name = path.join(path.dirname(pdf_file_name), new_name)
    # move(pdf_file_name, full_new_name)

if __name__ == "__main__":
    from sys import argv
    process_directory(argv[1])
