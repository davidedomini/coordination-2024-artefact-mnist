FROM python:latest
RUN mkdir /experiment
WORKDIR /experiment
COPY plotter.py ./
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python plotter.py