Converting the VCF file to an efficient (HDF5) format
*****************************************************

.. TODO::
    Relate with HPC part

.. note::
  Notebooks:

  * VCF_Processing_Parallel_

.. info::
    This chapter is presented for instructional purposes mosly on map-reduce
    strategies. If you really want to convert a VCF file into numpy arrays or
    HDF5 files, I recommend using Alistar Miles' vcfnp_ (see previous chapter).



In this chapter we are going to scafold the code to convert a VCF file into
a HDF5 representation. As you recall from the previous chapter traversing the
complete VCF file can take days or even weeks so a typical big data workflow
starts by converting this format to something that we can manipulate more
efficiently for analysis. In our case we will concentrate on understanding a general
framework to convert big data in a fast and reliable way. We are not worried
with the intricacies of converting this specific VCF file, but in providing the gist
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




.. info::
  There are many many framekworks for parallel processing (there will be a chapter on this).
  Here I will note only `IPython Parallel`_ which comes from the same project
  as Jupyter Notebooks that we are using for pratical examples. If you are interested
  you can get lots
  of documentation on the ipyarallel site and also check the last chapter of
  my `Bioinformatics book`_ (You can get a `github notebook`_ with all the code
  for free).


.. _`Bioinformatics book`: http://www.amazon.com/Bioinformatics-Python-Cookbook-Tiago-Antao/dp/1782175113
.. _`github notebook`: http://nbviewer.jupyter.org/github/tiagoantao/bioinf-python/blob/master/notebooks/08_Advanced/IPythonParallel.ipynb
.. _`IPython Parallel`: https://ipython.org/ipython-doc/3/parallel/
.. _VCF_Processing_Parallel: http://nbviewer.jupyter.org/github/tiagoantao/data-science-teaching/blob/master/notebooks/003_VCF_Processing_Parallel.ipynb
.. _vcfnp: https://github.com/alimanfoo/vcfnp
