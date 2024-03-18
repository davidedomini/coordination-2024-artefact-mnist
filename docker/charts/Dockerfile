FROM python:latest
RUN mkdir /experiment
WORKDIR /experiment
COPY docker/charts/plotter.py ./
COPY docker/charts/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python plotter.py mnist && python plotter.py fashion
