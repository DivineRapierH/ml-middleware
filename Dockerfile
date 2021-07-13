FROM condaforge/mambaforge:4.10.3-1
RUN mkdir /root/ml-middleware && mkdir /root/models
ENV PROJECT_DIR /root/ml-middleware
ENV MODELS_DIR /root/models
WORKDIR $PROJECT_DIR
COPY environment.yml .
COPY requirements.txt .
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "ml-middleware", "/bin/bash", "-c"]
RUN pip install --default-timeout=600 -r requirements.txt
COPY src ./src
EXPOSE 50051
ENTRYPOINT ["conda", "run", "-n", "ml-middleware", "python", "src/main.py"]