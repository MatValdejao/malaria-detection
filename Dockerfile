FROM tensorflow/tensorflow:latest-gpu

# copy dependencies
COPY requirements.txt .

# install jupyter notebook and fixed dependencies
RUN pip install -r requirements.txt

# set working directory
WORKDIR /workspace

# expose port
EXPOSE 8888

# add command to run jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]