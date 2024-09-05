# Introduction

Pipeline for quantifying cell numbers in gels.
Written by Damian Dalle Nogare at the BioImage Analysis Infrastruture Unit of the National Facility for Data Handling and Analysis at Human Technopole, Milan. Licenced under BSD-3.

# Installing the pipeline

1. Make a folder to store the pipeline files
2. Navigate to that folder in a terminal window
3. Initialize a git repository by typing `git init`
4. Pull the latest version of the pipeline using the command `git pull https://github.com/nobias-fht/erdmann-cell-counting`
5. Create a conda environment by typing `conda env create -f environment.yml`


# Running the pipeline

Before running, ensure that you have the latest version of the script by running the terminal command "git pull" from the folder you have the scripts installed in.

1. Activate the environment by typing `conda activate cell_counting`
2. Run the command `python3 count_cells.py`
3. Follow the prompts to select the folder with the input files and the location to store the output files



