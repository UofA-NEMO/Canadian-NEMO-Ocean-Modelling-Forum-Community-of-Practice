HPC system
==========

Currently, we use High Performance Computing systems via Compute Canada, specifically `Graham <https://docs.alliancecan.ca/wiki/Graham>`_ and `Niagara <https://docs.alliancecan.ca/wiki/Niagara>`_. Graham is the HPC that is open to most users while Niagara is via special allocation proposals for massive CPU tasks. There are other HPCs available to our group including Cedar and Narval that is very similar to Graham, but we currently generally work on Graham. The information below will hopefully answer some questions about working on these systems.

Overview
--------

The HPC system is often broken into 2 main components: project and scratch. Your project space (/project/6007519/$USER/ on Graham) is where you should place files that do not get edited or files for longer-term use. Examples would be this is where we compile NEMO, store its source code, and submit our NEMO jobs. The scratch space (/scratch/$USER/) is a location where files are deleted after 2 months of inactivity. Scratch is where we produce the temporary directories where NEMO runs, where we are suppose to save our model output and restarts, and do analysis. Since files are deleted after 2 months of inactivity, we need to remember to tar and store anything on our scratch space that we want to keep. Or transfer to another location like our lab's servers. This brings us to a 3rd component, "nearline", or the tape archive. Nearline is the name for the offline data storage server of Graham (called silo on others) where physical drives are brought online/offline to copy/move data between nearline and scratch/project. As such, nearline is NOT a place to host files to do analysis as it takes a lot of time to read and copy these files between devices.

In general, best practice is to produce things that you require, but won't change, and host them on Project. Scratch is for temporary work to carry out our simulations, produce figures/movies, and so forth- and then to move those important files elsewhere. If they are to be moved to project or nearline, tar and zip them up first as storage space is short. You can always untar/zip them back to scratch to redo analysis.

Submission Script
-----------------
Regardless of the HPC you are working on, tasks generally require a submission of a job script: to run NEMO, matlab code, ARIANE, other fortran code, etc. The scheduling system requires some information that we place at the top of the submission script:
"
#!/bin/ksh
#SBATCH -J {NAME_OF_JOB}
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --mem-per-cpu=4000
#SBATCH -t 00-02:00        ## 0 day, 2 hour, 0 minutes
#SBATCH -o slurm-mem-%j.out
#SBATCH -e slurm-mem-%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user={EMAIL ADDRESS}
#SBATCH --account={ALLOCATION (dev/rrg name)}
"
|
Afterwhich you should load your modules and the associated code you want to carry out. For a matlab job, the following lines might look like this:
"
date
module --force purge
module load nixpkgs/16.09
module load matlab/2018a
matlab -nodisplay -singleCompThread -r "CheckVosaline"
matlab -nodisplay -singleCompThread -r "CheckVotemper"
date
"
|

Interactive Jobs
----------------

Sometimes you need to debug something or test some code out that requires more time/CPU than the login-node provides. We are allowed to use the login nodes for short simple tests (like compiling NEMO and ncviewing files), but the admin has limits on what they want done on these login-nodes. So maybe you want to write/debug some matlab code to run analysis on ANHA4 output. To get the code ready, you should open an `interactive job <https://docs.alliancecan.ca/wiki/Running_jobs#Interactive_jobs>`_. Below is a short example on how to do that for a matlab job:
1:enter the interactive job information (example 20 minute job, 4000m memory, 1 cpu)
salloc --time=0:20:0 --ntasks=1 --account={rrg/dev allocation} --mem=4000M
2: Wait for the interactive node to spin your job up, it can take a minute or 2 depending on what you ask for
3: You are now in the job- it currently does not share the same environmental variables as your regular login space. So load whatever modules and set variables as you require:
module load nixpkgs/16.09
module load matlab/2018a
4: Matlab requirements are now set, you should be able to open matlab without a GUI (as we didn't forward X11)
matlab -nodisplay
5: Do your matlab debugging/work.
|
Notes: keep interactive jobs to a duration no more than 3 hours- anything longer can take a long time to open up. 3 hours or less should open quickly (unless you request a lot of ntasks)

More to come.

