**************
Introduction
**************

Tutorial components
====================

This tutorial is composed of

* A set of videos
* Presentations
* Notebooks
* A Docker container with the notebooks
* This text

The fundamental content is this text and the Notebooks. In the text you will
find the explanations and in the notebooks the running code.

The videos gives you an introduction to the material and the presentations
are mostly used by myself when teaching this content. You might want to have
a look at them, especially at the very beginning


How to use the Notebooks
==========================

The easiest and absolutely **not recommended** way to use this material is
to only read it on github_. This is bad in many ways as the fundamental premise
of the notebooks.

Online systems for notebooks (mybinder or SageMathCloud) are problably not a
good idea because our notebooks need *a lot* of disk space and compute power.

Now lets look at the more realistic options...

.. important::
  Allocate 100GB of disk space for the data that you will need to download.

  Have a good Internet connection. You will download ~50GB of data.

  We will be using Python 3. Legacy versions are not supported.

  All the text assumes that you used one of the options below.

The easiest way to install the notebooks is via Docker.

On Linux:

.. code:: bash

    docker pull tiagoantao/data-science-teaching
    docker run -p 8888:8888 tiagoantao/data-science-teaching

And then point your browser to ``http://localhost:8888``

On Windows/Mac:

Install Kitematic_ from the Docker toolbox, find
``tiagoantao/data-science-teaching`` and run it. Point your browser
to the exposed HTTP port

The "manual" installation procedure is to get the notebooks from github
on a local installation. The usage of `Anaconda Python`_ is strongly
recommended. Not only it includes all the Python packages but also
all the R content that we will be using here. You can have an idea of
the necessary packages by looking at our Dockerfile_ (check the ``conda install`` lines).

.. _github: https://github.com/tiagoantao/data-science-teaching
.. _Kitematic: https://kitematic.com/
.. _Anaconda Python: https://www.continuum.io/downloads
.. _Dockerfile: https://github.com/tiagoantao/data-science-teaching/blob/master/docker/Dockerfile
