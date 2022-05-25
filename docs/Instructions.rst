User Guide
==========

For groups/institutions/users who would like to join this community, the following instructions will come in handy. 

Requirements
............

* A GitHub account
* A local storage/system to push/pull code/documents/etc
* An understanding of boundaries

This website is built from documents saved onto the GitHub account which ReadTheDocs.org then produces into a website. For others to collaborate, we all work off of the cloned repository. Each user/institution only works within their assigned directory space so we do not interfere with the documents of other groups. Since the repository is cloned, all groups are synced to each other: any file we upload onto this repository then is downloaded and accessible by the other groups. As such, don't upload anything you wouldn't be willing to share, and don't modify anything outside your designated directories. There is a storage limit to how much we can store in the repository- please host large files (videos) elsewhere, only push small files.

A Walkthough
............

1. Each instruction needs to create a GitHub account and activate it accordingly. You will need to set up git on your local system- I cannot explain it here since each system may vary, but it entail setting up your git user name and email to the local system. 

2. Request collaborate access to our repository- email pennelly AT ualberta.ca and/or pmyers AT ualberta.ca . Let me know your GitHub user name as well as institution so I can send an invite to collaborate (as well as a passcode to push data) and setup some backend material.

3. Once the request has been accepted, you should be able to clone our repository. Navigate to a part of your local system you want the repository saved to, then issue

* git clone https://github.com/UofA-NEMO/Canadian-NEMO-Ocean-Modelling-Forum-Commuity-of-Practice.git 

4. This may take a few moments depending on how much figures/data are put into the repository.

5. A new directory called 'Canadian-NEMO-Ocean-Modelling-Forum-Commuity-of-Practice' should now appear within your directory. Go inside this

6. Within this directory, there are a few files which should not be edited. Head inside the 'docs' directory.

7. There are more files (please do not touch) as well as some directories here. Of note are '_static' and 'Institutions'. The admin should have created a directory within each of these that match your institution. See if those exist and investigate each- I'll use 'MyInstitution' as an example:

* cd Institutions/MyInstitution/

8. There should be a simple 'index.rst' file here and nothing else. This is the primary workspace for you to create your portion of the website out of. You can use the UofA's institutional directory to give you some sort of idea how things function, but it is up to your group on how you want to design your space on the site!

9. The second important directory is back a bit, head to /docs to find _static

* cd _static

10. Your second and final institutional directory resides here, as _MyInstitution. Here is where some documents (.csv and .pdf at the least) reside. For some reason, figure images can be saved and viewed fine within normal directories, but .pdf and .csv need to be saved and called from this directory. 

|
Your First Push and Pull
........................

This might be your first time working with git commands, so this section will briefly describe how things work. Open up your local storage command line and head to your /Institutions/{MyInstitution}/ directory. Create a new directory, lets just call it 'Configurations' since many NEMO users have set up their own configurations and want to share/document them. I'll document how things appear on a Linux OS, windows/mac may have some differences

* mkdir Configurations

* cd Configurations/

Each new directory also needs an index.rst file so the website understands how to connect together. Use whatever program you want to make index.rst. Include a line of text "Configurations". Save and exit.

Head back one directory into {MyInstitution}

It is now time to add the files/directories to git. First we let git know what should be included, this is a 'git add'. We will use an asterix to add everything within the directory:

* git add Configurations/*

This will add the Configurations directory and everything within it to push to the github site. Now we need to make a commit with a note:

* git commit -m 'SOME USEFUL NOTE TEXT'

Now git knows we plan to submit a push. Before we do that, lets make sure everything is up to date by checking we have the same files as what is currently within the repository. This is a 'pull'

* git pull

Issues occur when the files you have differ from that at the source, particularly if you are trying to update a file that is different. Keeping up to date via 'git pull' really helps prevent these problems. 

Now your current files are the same as the repository, minus the new ones you are about to push. Lets do that:

* git push

Git will then ask for your user name as well as the passcode the admin should have supplied. Enter those and you should get a successful push message. 

If you head to the github page, you can see the new file and directory. Here you can further modify things and save/commit files much quicker than using the terminal. However, you cannot make new directories from the github page (but you can make new files), only from the terminal/GUI connection. Use the above method to create new directories. You can also copy files into these directories and 'git add' them as well.

|
Some samples
............

I spent a lot of time sorting out how to illustrate various aspects on this site. I'll try to make all of our lives easier and document it here so you do not have to repeat my frustrations. One major thing I learned is that leading whitespace is important, I'll explain shortly.

Figures
^^^^^^^

Displaying figures isn't that tricky. Simply put the figure file into the directory where you want it to be shown. For example, our eORCA025 data figure should reside within the Configurations/eORCA025/ directory. Copy it into this position, git add, git commit, git pull, and git push the figure. Now that it appears on our github page we can call it inside the index.rst file (or {OtherRstFile}.rst, they can be called something else) using the following code:

.. code-block:: RST
   :linenos:
   
   .. figure:: ./eORCA025_data_Figure.png
      eORCA025 data figure caption text
   

An empty trailing and leading line around the figure block appears important, as well as the three empty spaces that indent the figure caption test, the empty lines associate this with the thing we are trying to do (in this case a figure)

Embedded content
^^^^^^^^^^^^^^^^

The internet is great and a lot of content can be produced and embedded elsewhere. Good examples of this that we have used on this website include but are not limited to Google Documents, YouTube videos, Google Calendar, etc. The process to add each of these is functionally the same- we call an HTML object which allows itself to be embedded. And since the object is hosted outside of our GitHub page, you do not need to push a new file like we did with the figure above. The .rst code looks sort of like the following for a youtube video:

.. code-block:: RST
   :linenos:
   
   .. raw:: html
      <iframe width="740" height="200" src="EMBEDDED WEBSITE URL;single=true&amp;widget=true&amp;headers=false"></iframe>
   
Embedding other objects likely will have text that differs, but the use of ".. raw:: html" should stay the same. The easiest way is to find each object's embed code (often found if there is a 'share'/publish button), and copy that. You can modify the width/height so it displays the size you are interested in.

Tables
^^^^^^

Tables are tricky. I've checked out two different paths. One used a google sheet with the embed method above. This lets us modify the table on the fly and have it updated relatively quickly on the website. The other method was using a .csv file you need to push to github. Once on GitHub, you can edit the csv file, but the csv reader isn't spectacular. In my opinion, the google sheets method is far easier and more friendly. For that, just 'publish' your sheet so you can get the embed code, and use that with the technique above.

As for the csv reader, you need to copy your .csv file into your _static/_MyInstitution/ directory. Git add, git commit, git pull, and git push it to github. Then on your .rst file where you want the table hosted, use the following

.. code-block:: RST
   :linenos:
   
   .. csv-table:: Table Title
      :file: FileName
      :widths: 30, 70
      :header-rows: 1
   
This will load FileName.csv which has 2 columns. Column 1 has a width that is 30% of the table while column 2 has a width that is 70% of the table. There is a single row of headers. There could be many rows but only 2 columns. Since cell width can vary significantly depending on the text within, this method is rather cumbersome in my experience. The filename does not require the full path since csv-table reads files contained within the _source directory as outline within our config.py code in /docs. The admin should have added your directory to be included, contact them if this method fails you as other media will likely also fail (PDF/PPT).

Weblinks
^^^^^^^^

Setting up links is relatively straitforward. Include something along the lines of the following withing your .rst file:

.. code-block:: RST
   :linenos:
   
   `Sample Link Text <FULL URL HERE>`_
   Example:
   `NEMO website <https://www.nemo-ocean.eu/>`_


PDFs
^^^^

Hosting PDFs is also possible, although I've only figure out how to make them viewable on their own site, not popup/displayed as an embeded document. Add the PDF to your _static/_MyInstitution/ directory, git add, git commit, git pull, and git push it to github. In the .rst file where you want the PDF to be viewed, make a link:

.. code-block:: RST
   :linenos:
   
   `Sample Link Text <https://canadian-nemo-ocean-modelling-forum-commuity-of-practice.readthedocs.io/en/latest/_static/_{MyInstitutionName}/<MyPDFfile}.pdf>`_

PowerPoint
^^^^^^^^^^

Hosting a powerpoint presentation works the same as PDFs above: the files need to be pushed to github from your _static/_MyInstitution/ directory. Just as I was not able to figure out how to make the PDF embedded in the site, I could not figure the same for a powerpoint presentation. Instead we use a link to download the presentation to your computer/ internet browser. Set your .rst file to include a weblink to where the files are found:

.. code-block:: RST
   :linenos:
   
   `Sample Link Text <https://canadian-nemo-ocean-modelling-forum-commuity-of-practice.readthedocs.io/en/latest/_static/_{MyInstitutionName}/<MyPPTfile}.pptx>`_



