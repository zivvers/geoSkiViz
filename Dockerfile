FROM python:3.7-buster

RUN mkdir /usr/src/geo
WORKDIR /usr/src/app

RUN pip install rasterio
RUN pip install numpy

# /Users/zivdreyfuss/Music/Music/Media.localized/Automatically\ Add\ to\ Music.localized
# docker run -v "/Users/zivdreyfuss/Repos/geoTiff/:/usr/src/geo" -v "/Users/zivdreyfuss/Repos/pyMusic:/usr/src/app" -it /bin/bash