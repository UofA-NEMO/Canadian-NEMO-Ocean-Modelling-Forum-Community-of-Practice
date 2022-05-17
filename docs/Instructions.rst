Instructions
============

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

2. Request collaborate access to our repository- email pennelly AT ualberta.ca . Let me know your GitHub user name as well as institution so I can send an invite to collaborate (as well as a passcode to push data)

3. Once the request has been accepted, you should be able to clone our repository. Navigate to a part of your local system you want the repository saved to, then issue

* git clone https://github.com/UofA-NEMO/Canadian-NEMO-Ocean-Modelling-Forum-Commuity-of-Practice.git 

4. This may take a few moments depending on how much figures/data we put into the repository.

5. A new directory called 'Canadian-NEMO-Ocean-Modelling-Forum-Commuity-of-Practice' should now appear within your directory. Go inside this

6. Within this directory, there are a few files which should not be edited. head inside the 'docs' directory.

7. There are more files (to not be touched) as well as some directories here. Of note are '_static' and 'Institutions'. The admin should have created a directory within each of these that match your institution. See if those exist- I'll use 'MyInstitution' as an example:

* cd Institutions/MyInstitution/

8. There should be a simple 'index.rst' file here and nothing else. This is the primary workspace for you to create your portion of the website out of. You can use the UofA's institutional directory to give you some sort of idea how things function, but it is up to your group on how you want to design your space on the site!

9. The second important directory is back a bit, head to /docs to find _static

* cd _static

10. Your second and final institutional directory resides here, as _MyInstitution. Here is where some documents (.cdv and .pdf at the least) reside. For some reason, figure images can be saved and viewed fine within normal directories, but .pdf and .csv need to be saved and called from this directory. 

Your First Push and Pull
........................

This might be your first time working with git commands, so this section will briefly describe how things work. Open up your local storage command line and head to your /Institutions/{MyInstitution}/ directory. Create a new directory, lets just call it 'Configurations' since many NEMO users have set up their own configurations

* mkdir Configurations

* cd Configurations/

Each new directory also needs an index.rst file so the website understands how to connect together. Use whatever program you want to make index.rst. Include a line of text "Configurations". Save and exit

Head back one directory into {MyInstitution}

It is now time to add the files/directories to git. First we let git know what should be included, this is a 'git add'

* git add Configurations/*

This will add the Configurations directory and everything within it to push to the github site. Now we need to make a commit with a note:

* git commit -m 'SOME USEFUL NOTE TEXT'

Now git knows we plan to submit a push. Before we do that, lets make sure everything is up to date by checking we have the same files as what is currently within the repository. This is a 'pull'

* git pull

Issues occur when the files you have differ from that at the source, particularly if you are trying to update a file that is different. Keeping up to date via 'git pull' really helps prevent these problems.

Now your current files are the same as the repository, minus the new ones you are about to push. Lets do that:

* git push

Git will then ask for your user name as well as the passcode the admin should have supplied. Enter those and you should get a successful push message

If you head to your github page, you can see the new file and directory. Here you can further modify things and save/commit files much quicker than using the terminal. However, you cannot make new directories from the github page, only from the terminal connection. Use the above method to create new directories. You can also copy files into these directories and 'git add' them as well.
