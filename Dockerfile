FROM tensorflow/tensorflow:latest-jupyter

# copy dependencies
COPY requirements.txt .

# install jupyter notebook and fixed dependencies
RUN pip install --upgrade pip && \ 
    pip install -r requirements.txt

# install git lfs
RUN apt-get update && \
    apt-get install -y git curl && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y git-lfs && \
    git lfs install && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install ipykernel for the container
RUN python -m ipykernel install \
    --name container-kernel \
    --display-name "Python (Container)" \
    --prefix /usr/local

# need to run code-server for vscode in docker
RUN curl -fsSL https://code-server.dev/install.sh | sh

# set working directory
WORKDIR /workspace

# expose port
EXPOSE 8888
EXPOSE 8080

# add command to run jupyter notebook
CMD bash -c "\
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token = 'myToken' & \"
    code-server --bind-addr=0.0.0.0:8080 --auth password --password='mytoken'
