Converting the VCF file to an efficient (HDF5) format
*****************************************************

.. note::
  Notebooks:

  * HDF5_VCF_Speed_Comparison_

.. warning::
  This chapter assumes some knowledge of parallel processing frameworks,
  notably IPyrhon Parallel. When you read the following you are expected to
  have minimal experience with that library. You can check the original
  `IPython Parallel`_ documentation, or for example, the last chapter of
  my `Bioinformatics book`_ (You can get a `github notebook`_ with all the code
  for free).

In this chapter we are going to scafold the code to convert a VCF file into
a HDF5 representation. As you recall from the previous chapter traversing the
complete VCF file can take days or even weeks so a typical big data workflow
starts by converting this format to something that we can manipulate more
easily for analysis. In our case we will concentrate on understanding a general
framework to convert big data in a fast and reliable way. We are not worried
with the intricacies of converting VCF files, but in providing the gist
of the strategy to do data preparation.

As a sequential operation takes a lot of time we will start by breaking
breaking the genome into smaller pieces and do concurrent processing. This
problem is not completely trivial because all of our small computation programs
will need to write to shared data structure and while concurrent reads are trivial
against HDF5 files, concurrent writes are difficult at best.

So we will make each process write a small HDF5 per computation and then a
*single* final procedure will collect all the small HDF5 files and create
a single HDF5 file. Note that this single procedure will be much faster as
it will read data not from a VCF file, but from a HDF5 file.


ipcluster start -n 4

Careful with the number of processors

.. _`Bioinformatics book`: http://www.amazon.com/Bioinformatics-Python-Cookbook-Tiago-Antao/dp/1782175113
.. _`github notebook`: http://nbviewer.jupyter.org/github/tiagoantao/bioinf-python/blob/master/notebooks/08_Advanced/IPythonParallel.ipynb
.. _HDF5_VCF_Speed_Comparison: http://nbviewer.jupyter.org/github/tiagoantao/data-science-teaching/blob/master/notebooks/002_HDF5_VCF_Speed_Comparison.ipynb
.. _`IPython Parallel`: https://ipython.org/ipython-doc/3/parallel/
