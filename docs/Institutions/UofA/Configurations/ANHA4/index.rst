ANHA4
=====

ANHA is our acronym for the Arctic and Northern Hemisphere Atlantic configuration of the NEMO model. It covers the entire Arctic and Northern Atlantic Ocean, and a portion of the Southern Atlantic. The ANHA configuration has open boundaries across Bering Strait in the Arctic, as well as in the Southern Atlantic Ocean across the 20 degree south latitude. ANHA was designed to be a subset of the ORCA global grid, allowing us to use a regional configuration to use much less computing resources (RAM + CPU time) to carry out our research and development purposes.

Here we show the 1/4 degree resolution ANHA configuration (ANHA4)

.. figure:: ./ANHA4_horzgrid.png

ANHA4 is our low resolution regional configuration that affords us a low-cost, eddy-permitting simulation. Such simulations are particularly useful for any sensitivity studies since we can finish a multi-decade simulation within a month or so. ANHA4 has been a very productive configuration. Its fast simulation time allows us to test all sorts of new model development, parameter testing, coupled systems. Here is our incomplete listing of our ANHA4 simulations with some useful information:

test1

.. csv-table:: ANHA4 Simulation List
   :file: ./simulation_table.csv
   :widths: 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 2 
   :header-rows: 1

test2

.. list-table:: ANHA4 Simulation list
   :widths: 5 5 5 5 5 5 5 5 5 5 5 20 22
   :header-rows: 1

   * - Simulation Name
     - NEMO Version
     - Integration Period
     - Sea Ice Model
     - Initial Conditions
     - Open Boundary Conditions
     - Atmospheric Forcing
     - Runoff Product
     - CPP keys
     - Output frequency
     - Special Notes
     - Local Output Location
     - HPC output Location
   * - ANHA4
     - NEMO 3.4
     - 2002-2018
     - LIM2
     - GLORYS2V3
     - GLORYS2V3
     - CGRF
     - Monthly w/ Greenland melt
     - some keys
     - 5 day average
     - Second ANHA12 run
     - local: /mnt/storage3/xhu/NEMO/ANHA12-EXH006
     - graham: /project/6007519/ANHA/ANHA12-EXH006-S
     
test3 
 
.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSnXVJj1gTVGrTGVz2FyvTV6v_JrjBDhL7TzCpwWvjBm0h9iTUlohEyLgN8tmuhnoHLN-KDZqkuVJvc/pubhtml"></iframe>
     
