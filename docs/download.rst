Downloading the data
********************

.. note::
  Notebooks:

  * Download_


To download the data, execute the Download notebook (notebooks related to the text will be
shown on the top of each chapter). Note that this will
get approximately 50 GB of data. You will need sufficient disk space and
and good internet connection.

The data will be stored in the ``raw`` directory along the ``notebooks`` directory.

Open a shell and have a look at the vcf file, use a tool like ``zless`` as
the file is compressed. Do not uncompress it.

We download:

* A VCF file with the complete 3L chromosome.
* The index for the VCF file
* A small subset of the same VCF file using ``tabix``. Note that partial
downloads of VCF files are possible
* An equivalent HDF5 file

Indexing
==========

Talk about indexing the partial file.

HDF5 files
==========

vitables

.. _Download: http://nbviewer.jupyter.org/github/tiagoantao/data-science-teaching/blob/master/notebooks/000_Download_Data.ipynb
