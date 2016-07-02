FROM continuumio/anaconda3

RUN git clone https://github.com/tiagoantao/data-science-teaching.git
RUN /opt/conda/bin/conda install jupyter dask pandas pytables scipy -y

WORKDIR /data-science-teaching/notebooks

ENTRYPOINT /opt/conda/bin/jupyter-notebook --no-browser --ip=*

EXPOSE 8888
