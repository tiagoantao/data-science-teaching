**************
Introduction
**************

Target audience
===============

There are two potential target audiences for this course:

* A programmer or statistician with no background in life sciences. In this
  case you are strongly recommended to read the chapter on Genomics. You need
  to have a basic understanding on genetics and genomic structure and the
  chapter provides that. Do not worry, the level needed is introductory and
  you might even know most of the content anyway.

* Biologists with *a lot* programming experience. In this case you can skip most
  of the chapter on genomics. That being said, you are recommended to read the
  part on mosquito genomics just for information. Nothing more than a couple of
  paragraphs.

.. info::
  This is not a course about biology. The material is about data processing
  and analysis using genetics as the example.


Course material
===============

This is a data science course based on bioinformatics. It has the motivational
advantage of being completely hands-on and based on a real, concrete problem.
But the downside is that
it will only cover materials that are relevant to biological analysis,
fortunately that still allows to cover a lot of terrain. But do not expect
to find, for example natural language processing techniques here.
Sometimes we will extend the material a bit, in order to explain a point
better, for example we might use a simpler dataset to explain a concept
that would be too hard with the genomic data that we have.

We will mostly use genetic data from the mosquito that transmits malaria,
but every now and then we might use human genetic data.


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

.. info::
  While I have written a technical book in the past and am myself a avid book
  reader (of non-techincal stuff), I strongly believe that the book format
  is not appropriate for transmiting techincal knowledge. The core of this
  course is a set of Jupyter notebooks which you are stronly encouraged to tinker
  and change (learning via hands-on experience). In this text you can find
  supporting notes to help you understand the code and the theory behind it
  (along with suggestions of alternative options). In the future there will
  also be videos and presentations if I find that these will be helpful.

How to use the Notebooks
==========================

The easiest and absolutely **not recommended** way to use this material is
to only read it on `Jupyter viewer`_ (or even github_). This is bad in many ways as the fundamental premise
of the notebooks.

Online systems for notebooks (mybinder or SageMathCloud) are problably not a
good idea because our notebooks need *a lot* of disk space and compute power.

Now lets look at the more realistic options...

.. important::
  Allocate 100GB of disk space for the data that you will need to download.

  Have a good Internet connection. You will download ~50GB of data.

  We will be using Python 3. Legacy versions are not supported. Part of
  the code will require at least 3.5.

  All the text assumes that you used one of the options below to access the
  material. While you can just read as specified above, this material is
  intended for you to hack and tweak.

  Finally this is *not* introductory material.

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

A note about visualization
==========================

It goes without saying that many options underlying this course are open for
discussion. From the programming language of choice, to the selected material
and its organization. There are pleny of alternatives in terms of technologies,
course structuring that are worthwhile considering. But there is one that
I feel it worthwhile to talk about.

The browser in itself is a very powerful computing platform, with well
optimized JavaScript virtual machines which can run plenty of programming
languages. We spent most of our time working on browsers, and tools like
the Jupyter Notebook make the browser a feasible environment for exploratory
data anaylysis and development of experimental algorithms.

While there are plenty of amazing Python-based charting libraries (Matplotlib,
Bokeh...) that interact well with the browser they cannot give you the
flexibilty on in-browser based programming for visualization.

Thus, while we will use Matplotlib for simple charting, I believe that we will
have to bite browser-side programming for really insightful approaches to
visualization. Note that browser-side programming does not have to mean
Javascript. There are many alternatives to it. Personal recommendations would
be Brython_ (Python on the browser!), ClojureScript_ and Elm_.

Because this is a Python based course, we will *sometimes* use Brython instead of
Javascript.

If you want to know more
========================

I will be providing some links to external reading. If you want to go deeper
in some concepts where I do not provide links, then your suggested first port
of call should be Wikipedia. Be aware that while the Engish version of Wikipedia
provides high-quality versions of articles, other versions might be lacking.
Read the English version first.

.. _Anaconda Python: https://www.continuum.io/downloads
.. _Brython: http://www.brython.info/
.. _ClojureScript: https://github.com/clojure/clojurescript
.. _Dockerfile: https://github.com/tiagoantao/data-science-teaching/blob/master/docker/Dockerfile
.. _Elm: http://elm-lang.org/
.. _github: https://github.com/tiagoantao/data-science-teaching
.. _Jupyter viewer: http://nbviewer.jupyter.org/github/tiagoantao/data-science-teaching/blob/master/notebooks/000_Download_Data.ipynb
.. _Kitematic: https://kitematic.com/
