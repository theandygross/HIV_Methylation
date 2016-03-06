
# README

This repository contains all of the analysis notebook required for the reproduction of the manuscript __Methylome-wide analysis of chronic HIV infection reveals five-year increase in biological age and epigenetic targeting of HLA__.  

This is a fairly complex analysis pipeline, with many steps.  If you are planning of running the entire pipeline starting from raw data, this should be possible with the attached code, but I highly recomend you contact me (the.andrew.gross AT gmail DOT com) for assistance. Its probably not going to run straight though. Some steps in this process have relatively specialized requirements such as high memory machines or use of a compute cluster. 

In addition, I have also tried to make available a number of intermediate files which should allow for targeted re-analysis of the data or testing of new hypotheses. 

Finally all of the analyses done here are represented in IPython notebooks.  This was meant to allow for __high level inspection__ of the analysis logic done for this study. I have done my best to document this such that it can be understood __without running the actual code__.  If you are interesting in reproducing this study, or conducting a similar study I highly recomend __looking before you leap__ into trying to get code to run.  

<b>For step by step running instructions see [Guide to Running](./Guide_to_Running.ipynb)</b>

## Main Data Analysis

Here is where I do the main data analysis for the manuscript.   
* [__Unsupervised Age HIV Analysis__](./Unsupervised_Age_HIV_Analysis.ipynb)   
Unsupervised analysis of age associated probes with the aim of showing a shared influence of age and HIV on the methylome. This contains the code for the generation of Figure 1. 
* [__HIV Age Advancment__](./HIV_Age_Advancement.ipynb)  
Here I read in the data and run the methylation age models.  
* [__HIV Age Advancement: Confounders__](./HIV_Age_Advancement_Confounders.ipynb)  
Here I am looking at confounding from patients' blood composition as well as association of age advancment with other clinical variables that we have available. 
* [__Figure 2__](./Figure2.ipynb)  
Generation of Figure 2 for the manuscript. 
* [__Validation_figure__](./Validation/Validation_Figure.ipynb)   
Generation of Figure 3 of the manuscript. 
* [__Figure 3__](./Figure3.ipynb)   
Generation of Figure 4 for the manuscript. Figure 3 got added in revisions, so I'm keeping the name consistent to not lose the version control. 
* [__Figure 5_top__](./new_fig_5_top.ipynb)  
Generation of Figure 5a and 5b for the manuscript. Also includes a look at general disorder in response to age and HIV as well as some post-hoc analysis on the HLA and sourounding regions. 
* [__Figure_5_bottom__](./Validation/new_fig_5_bottom.ipynb)   
Generation of Figure 5c-f for the manuscript.



## Dependencies

This code uses a number of features in the scientific python stack as well as a small set of standard R libraries. Thus far, this code has only been tested in a Linux enviroment, it may take some modification to run on other operating systems.

I highly recomend installing a scientific Python distribution such as [Anaconda](http://continuum.io/) or [Enthought](https://www.enthought.com/) to handle the majority of the Python dependencies in this project (other than rPy2 and matplotlib_venn).  These are both free for academic use.

### Python Dependencies 

* [Numpy and Scipy](http://www.scipy.org/), numeric calculations and statistics in Python 
* [matplotlib](http://matplotlib.org/), plotting in Python
* [Pandas](http://pandas.pydata.org/), data-frames for Python, handles the majority of data-structures  
* [statsmodels](http://statsmodels.sourceforge.net/), used for statstics  
* [scikit-learn](http://scikit-learn.org/stable/), used for supervised learning
* [rPy2](http://rpy.sourceforge.net/rpy2.html), communication between R and Python  
  * __NOT IN DISTRIBUTIONS__  
  * I recommend installing with `pip install rpy2`  
  * Needs R to be compiled with shared libraries  
* [seaborn](http://stanford.edu/~mwaskom/software/seaborn/index.html) 
  * __NOT IN DISTRIBUTIONS__  
  * I recommend installing with `pip install seaborn` 


### My Internal Package Dependencies

These are Python packages that I use internally for things such as statistics and visualization. They are all available on [my Github page](https://github.com/theandygross), I recomend downloading them and installing them with `python setup.py install`.  I appoligize for the generic names, I am hoping to develop these a bit more and make them into proper packages up to spec in my next code refactor.   

* [Figures](https://github.com/theandygross/Figures) 
  * Code for better figure generation, mainly using Pandas data-structures 
  * I am slowly phasing this out and replacing with the very nice [seaborn](http://stanford.edu/~mwaskom/software/seaborn/index.html) library  
  
* [Stats](https://github.com/theandygross/Stats)  
  * Contains two packages, __Stats__ and __Helpers__ 
  * __Stats__ has a number of helper functions that wrap calls to R or scipy statistics functions and allow them to play nicer with Pandas data-structures  
  * __Helpers__ has a number of common tasks that I envoke to make code a bit more readable 
  
* [NotebookImport](https://github.com/theandygross/NotebookImport) 
  * Utility for importing IPython notebooks as modules
  * Code taken from [MinRK's Gist](http://nbviewer.ipython.org/gist/minrk/6011986)

### R Dependencies 
* [minfi](http://bioconductor.org/packages/release/bioc/html/minfi.html) 
    * Used for normalization of Illumina 450k methylation arrays 
* [IlluminaHumanMethylation450kanno.ilmn12.hg19](http://bioconductor.org/packages/release/data/annotation/html/IlluminaHumanMethylation450kanno.ilmn12.hg19.html)
    * Used for methylation probe annotations 
* [FlowSorted.Blood.450k](http://bioconductor.org/packages/release/data/experiment/html/FlowSorted.Blood.450k.html) 
    * Used in normalization of whole blood for varying cellular composition  
* [WGCNA](http://labs.genetics.ucla.edu/horvath/CoexpressionNetwork/Rpackages/WGCNA/) 
    * Used in the normalization pipeline for Steve Horvath's aging model
