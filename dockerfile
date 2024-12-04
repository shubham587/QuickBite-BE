# base image
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# installing packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# creating a directory for app
WORKDIR /usr/src/app

# copy the current project directory
COPY . .

# install the virtual env
RUN python3 -m venv venv

# activate the virtual env and install the req.txt
RUN /bin/bash -c "source venv/bin/activate && pip install -r req.txt"

# RUN pip install -r req.txt

# run the flask app
CMD ["/bin/bash", "-c", "python3 run.py"]
