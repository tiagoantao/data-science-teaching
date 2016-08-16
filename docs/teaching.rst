**************
Teaching notes
**************

These are my notes about content that needs to be discussed as we
go across the course. As used in a pratical session.


- Environment preparation
  - nbviewer vs docker vs manual
  - Do the manual part
    - conda
    - package install
    - Starting jupyter
    -

- Introduction to the dataset
  - Mosquito genomics
  - WGS
  - Ag1000 description

- Downloading data (Download_Data)
  - File sizes
  - continue download if aborted (``wget -c``, ``rsync``)
  - partial download
  - indexing
  - Montana specific: data size comparison
    - **recover info on Anopheles data**

- Metadata exploration (Metadata)
  - Pandas
    - R-like data frame
    - columns
    - group by
    - describe
    - series creation
  - Matplotlib
    - A subplot example with style!
  - Pandas
    - more group by examples
    - **do a query example**

- Basic data exploration (Basic Exploration)
  - Reference genome
    - Biopython
    - gzip read
  - Using HDF5. State the code will not be explained at this stage
  - Exploration
    - Maximum chromosome position sequenced
    - Sample names
    - Number of markers
    - Example annotation per marker
    - Number of alternate alleles
    - Singletons and doubletons
      - ``*zip(*maf_count.items())``

- VCF vs HDF5 performance ( HDF5_VCF_Speed_Comparison)
  - Before we start:
    - 0 vs 1 indexing
  - VCF format
    - Present the anopheles case
  - HDF5 format
    - vitables
  - HDF5 performance
    - in memory
    - disk read (?)
  - VCF performance
    - no no no!
  - Less than a minute versus days (weeks really)
  - Why is VCF so slow?
    - Compression and line reading?
    - Parsing
  - Converting with vcfnp
    - cluster ready

- General comments on data compression
  - Particular case:
    - FASTQ/SAM --> FASTQ.GZ/BAM -> VCF.GZ -> PLINK
  - Geeky compression
  - Note to self: do compression notebooks

- Parallel computing
  - Parallel, concurrent and ditributed
  - Local execution (sequencial and parallel) vs clusters
  - Python
    - GIL
    - GIL release

- Converting VCF to HDF5 (VCF_Processing_Parallel)
  **not complete**
  **on big server, do not live-code**
  - sequencial example
  - dask
  - comment on chromosome split

- Performance (Performance)
  - Load a massive dataset into memory (or not)
  - Get the shape
  - Reshape
  - Transpose (view and copy)
  - Get a subset
  - Memory hierarchy
    - CPU cache and starvation
    - Read a column vs a row
    - Show (Performance_CPU)
    - Fortran vs C
  - High performance computing
    - Naïve matrix multiplication
    - Partial Vectorization
    - Full vectorization
    - Cython
      - naïve
      - pseudo-smart
      - Properly annotated
      - Wheels off!
    - Numba
    - Future: CUDA (Numba) and compare libaries (BLAS et al)

- Generators (HDF5_Filtering_Generators_extra)
  - refer python2 range vs xrange
  **TBD**

- Filtering (HDF5_Filtering)
  - partial function application 
  - subsampling
  - filter chainning
  - filter order
  Refer LD, scikit-allel


- Notes on computing the median (HDF5_Filtering_Mean_extra)
  - mean vs median
  - data properties (distribution...)
  - memory cost
  - Alternative approaches
    - subsampling
    - hash table
    - approximation

- Accessing R via Python
  - RPy2
  - pandas as intermeddiate format
  - where objects are (python vs R namespace)

- Galaxy
  - See results on the web inteface
  - Get your api key
  - FTP for upload
  - getpass
  
