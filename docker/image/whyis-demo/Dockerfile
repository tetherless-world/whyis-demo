ARG WHYIS_IMAGE_TAG=latest

# Multi-stage
# Build .js bundle
#FROM node:12-alpine as build-js
#COPY static /static
#WORKDIR /static
#RUN npm install
#RUN npm run build

# Deployment image
FROM tetherlessworld/whyis:$WHYIS_IMAGE_TAG

# Copy Python source
COPY --chown=whyis:whyis . /apps/whyis-demo
RUN pip3 install -e /apps/whyis-demo

# Copy built .js bundle
#COPY --from=build-js --chown=whyis:whyis /static/js/whyis_demo_bundle.js* /apps/whyis-demo/static/js/

COPY /docker/image/load-data.sh /

CMD ["tail", "-f", "/dev/null"]
