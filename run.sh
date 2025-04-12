#!/bin/bash

# Build the Charliecloud image directly
#ch-image build -t test-runner -f Dockerfile .

# Create a Charliecloud container

# Run the tests
ch-run -b $(pwd)/data:/data -W -v test-runner -- python /app/test_runner.py /data/unittest --output /data/results/$1_SecPLT_results.json --summary /data/summary/$1_SecPLT_summary.json --test_data $1
echo "Test execution completed!"
