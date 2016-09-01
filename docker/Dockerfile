FROM continuumio/anaconda3

RUN git clone https://github.com/tiagoantao/data-science-teaching.git
RUN /opt/conda/bin/conda install -y jupyter dask pandas pytables scipy biopython
RUN /opt/conda/bin/conda config --add channels r
RUN /opt/conda/bin/conda config --add channels bioconda
RUN /opt/conda/bin/conda install -y bioconductor-biobase


WORKDIR /data-science-teaching/notebooks

ENTRYPOINT /opt/conda/bin/jupyter-notebook --no-browser --ip=*

EXPOSE 8888
