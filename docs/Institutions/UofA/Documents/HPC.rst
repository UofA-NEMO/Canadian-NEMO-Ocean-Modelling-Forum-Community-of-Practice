HPC system
==========

Currently, we use High Performance Computing systems via Compute Canada, specifically `Graham <https://docs.alliancecan.ca/wiki/Graham>`_ and `Niagara <https://docs.alliancecan.ca/wiki/Niagara>`_. Graham is the HPC that is open to most users while Niagara is via special allocation proposals for massive CPU tasks. There are other HPCs available to our group including Cedar and Narval that is very similar to Graham, but we currently generally work on Graham. The information below will hopefully answer some questions about working on these systems.

Overview
--------

The HPC system is often broken into 2 main components: project and scratch. Your project space (/project/6007519/$USER/ on Graham) is where you should place files that do not get edited or files for longer-term use. Examples would be this is where we compile NEMO, store its source code, and submit our NEMO jobs. The scratch space (/scratch/$USER/) is a location where files are deleted after 2 months of inactivity. Scratch is where we produce the temporary directories where NEMO runs, where we are suppose to save our model output and restarts, and do analysis. Since files are deleted after 2 months of inactivity, we need to remember to tar and store anything on our scratch space that we want to keep. Or transfer to another location like our lab's servers. This brings us to a 3rd component, "nearline", or the tape archive. Nearline is the name for the offline data storage server of Graham (called silo on others) where physical drives are brought online/offline to copy/move data between nearline and scratch/project. As such, nearline is NOT a place to host files to do analysis as it takes a lot of time to read and copy these files between devices.

In general, best practice is to produce things that you require, but won't change, and host them on Project. Scratch is for temporary work to carry out our simulations, produce figures/movies, and so forth- and then to move those important files elsewhere. If they are to be moved to project or nearline, tar and zip them up first as storage space is short. You can always untar/zip them back to scratch to redo analysis.

Modules
-------

HPC systems have a wide variety of modules and software available to its users. Often there are multiple versions of the same software: matlab, ncview, openmpi, etc. This makes things a little complicated as not all versions of one software work correctl with libraries/binaries of another software. NEMO requires multiple forms of software to communicate. If gfortran and perl are working fine together but a library from XIOS doesn't communicate corretly with netcdf/hdf, you may have a model run corretly but crash when producing output. Managing the modules during compilation and running your jobs is crucial and time-consuming to figure out. Good thing is for the most part, we have figured out the correct list of modules to run our usual suite of software. But upgrading to a newer version or installing something new can present these challenges again.

Generally, when users log into Graham, a series of login scripts are executed from their /home/$USER/ directory:
.bashrc runs, even though we do not put anything inside of this
.bash_profile runs, setting up aliases and loading our standard modules, and also runs .login36
.login36 sets up some environmental variables.
The modules loaded (below) was a correct set to compile/run NEMO and various other software as of Oct 2022. This may change in the future, but you often can load previous modules even when the standard environment changes
"
module --force purge
module load StdEnv/2016.4
module load mcr/R2013a
module load openmpi
module load netcdf-mpi/4.4.1.1
module load netcdf-fortran-mpi/4.4.4
module load perl/5.22.2
module load ncview/2.1.7
"

Tinkering with modules
......................

Sometimes you need a module that isn't within the above auto-loading method. I'm going to use matlab as an example. You want to use matlab but do not know how to load the appropriate modules to do so. First thing we want to do is check what our current modules are by using "module list":

gra-login3:~ > module list
  Currently Loaded Modules:
    1) nixpkgs/16.09   (S)      3) gcccore/.5.4.0  (H)   5) ifort/.2016.4.258 (H)   7) StdEnv/2016.4  (S)   9) mcr/R2013a    (t)  11) perl/5.22.2     (t)   13) netcdf-mpi/4.4.1.1       (io)  15) udunits/2.2.24 (t)
    2) imkl/11.3.4.258 (math)   4) icc/.2016.4.258 (H)   6) intel/2016.4      (t)   8) java/1.8.0_121 (t)  10) openmpi/2.1.1 (m)  12) hdf5-mpi/1.8.18 (io)  14) netcdf-fortran-mpi/4.4.4 (io)  16) ncview/2.1.7   (vis)

This shows us what we currently have loaded 16 modules. We can learn about any of these by using "module spider":

gra-login3:~ > module spider ncview/2.1.7
  ncview: ncview/2.1.7
    Description:
      Ncview is a visual browser for netCDF format files. Typically you would use ncview to get a quick and easy, push-button look at your netCDF files. You can view simple movies of the data, view along various dimensions, take a
      look at the actual data values, change color maps, invert the data, etc.

We should do the same for matlab, lets see what the Graham system states:

gra-login3:~ > module spider matlab
  matlab:
    Description:
      MATLAB is a high-level language and interactive environment that enables you to perform computationally intensive tasks faster than with traditional programming languages such as C, C++, and Fortran.
     Versions:
       matlab/2014a
       matlab/2016b
( and many more versions including matlab/2022a)

Lets try to activate the most recent version since that might have the toolbox we are interesting in:

gra-login3:~ > module spider matlab/2022a
  matlab: matlab/2022a
    Description:
      MATLAB is a high-level language and interactive environment that enables you to perform computationally intensive tasks faster than with traditional programming languages such as C, C++, and Fortran.
    Properties:
      Tools for development / Outils de développement
    You will need to load all module(s) on any one of the lines below before the "matlab/2022a" module is available to load.
      StdEnv/2020
( and some more information that isn't important)

The last line here, stating we need to load StdEnv/2020, is key. That module must be loaded to active the 2022a matlab module. It may also have its own requirements/dependencies, but we would get an error if that is the case when we load it up:

gra-login3:~ > module load StdEnv/2020
  Inactive Modules:
    1) hdf5-mpi/1.8.18     2) java/1.8.0_121     3) mcr/R2013a     4) ncview/2.1.7     5) netcdf-fortran-mpi/4.4.4     6) netcdf-mpi/4.4.1.1     7) perl/5.22.2     8) udunits/2.2.24
  The following have been reloaded with a version change:
    1) StdEnv/2016.4 => StdEnv/2020     2) gcccore/.5.4.0 => gcccore/.9.3.0     3) imkl/11.3.4.258 => imkl/2020.1.217     4) intel/2016.4 => intel/2020.1.217     5) openmpi/2.1.1 => openmpi/4.0.3

No errors (but plenty of module deactivation/changes) means it was a success! Now lets load the matlab 2022a module

gra-login3:~ > module load matlab/2022a
  Activating Modules:
    1) java/13.0.2

That forced the java module to be re-activated and updated. We should now be able to run matlab. You can check which matlab binary you would be running by using 'which'

gra-login3:~ > which matlab
   /cvmfs/restricted.computecanada.ca/easybuild/software/2020/Core/matlab/2022a/bin/matlab

And you see it is indeed the 2022a matlab version. Success! You should be able to follow this sort of procedure for any module/software you would like to use.

|
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

1:enter the interactive job information using salloc (example 20 minute job, 4000m memory, 1 cpu). NOTE the hypens (-) below are double(- -) but this website prints as a single 

gra-login3:~ > salloc --time=0:20:0 --ntasks=1 --account={rrg/dev allocation} --mem=4000M

2: Wait for the interactive node to spin your job up, it can take a minute or 2 depending on what you ask for

3: You are now in the job- it currently does not share the same environmental variables as your regular login space. So load whatever modules and set variables as you require:

gra-login3:~ > module load nixpkgs/16.09

gra-login3:~ > module load matlab/2018a

4: Matlab requirements are now set, you should be able to open matlab without a GUI (as we didn't forward X11 via salloc)

gra-login3:~ > matlab -nodisplay

5: Do your matlab debugging/work.

Notes: keep interactive jobs to a duration no more than 3 hours- anything longer can take a long time to open up. 3 hours or less should open quickly (unless you request a lot of ntasks). 

More to come.

