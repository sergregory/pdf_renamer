# PDF renamer

This small tools allows its user automatically rename pdf files that contain metadata to the specified format.
The default format is `<year>-<author>-<title>.pdf`
Run it as following:
```
pdf_renamer.py <dir_name>
```
where `<dir_name>` is a directory, containing your pdfs

# Dependencies

- python 3
- PyPDF2

# TODO

- Check all prohibited symbols in a file name (only ':' is checked now)
- Check linux state
- Try to get info from the pdf text in case if metadata is unavailable
