#!/bin/bash

WHYIS_DEMO_IMAGE="${1:-tetherlessworld/whyis-demo:latest}"

docker run $WHYIS_DEMO_IMAGE bash -c "python3 manage.py test"

# mkdir -p test-results/py
# docker run $WHYIS_DEMO_IMAGE bash -c "python3 manage.py test --ci &>/dev/null && tar cf test-results-py.tar test-results/py && cat test-results-py.tar" >test-results-py.tar
# tar xf test-results-py.tar

# if [ "$(grep -c 'failure ' test-results/py/results.xml)" -ge 1 ]; then
#    exit 1
#else
#    exit 0
#fi
