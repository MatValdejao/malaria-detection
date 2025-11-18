FROM tensorflow/tensorflow:latest:gpu

# install jupyter notebook and fixed dependencies
RUN pip install --upgrade pip notebook matplotlib numpy pandas scikit-learn pillow kagglehub 

# set working directory
WORKDIR /workspace

# expose port
EXPOSE 8888

# add command to run jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root" ]