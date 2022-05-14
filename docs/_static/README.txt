information for others:

For some reason, Readthedocs/github/sphinx work in the following manner when trying to display PDFs and Tables:
They can only read these files from _static/_{Institution name}/{PDF or csv filename}

So you will need to make your institutional directory within _static, and a sample file within it (or else 'git push' will delete it)

They cannot read the files from other directories, and I never could figure out why. So all your pdf/csv links need to include a path to your _static/_{institution name}/ directory

for example, hosting a file within /docs/Institutions/UofA/Configurations/ANHA4 that wants to show a table needs to have a path that looks like "../../../../_static/_UofA/MyFile.pdf"

Furthermore, a minor update within the docs folder needs to take place for the config.py file: update
html_static_path = ['_static', '_static/_UofA']

to inclue your institutions:
html_static_path = ['_static', '_static/_UofA', [_static/_{My Institution}']

do the standard 'git add (files/directories)' as well as 'git commit' and then 'git push'. 
