FROM python:3.9-slim

# Set environment variables for better Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Copy test runner script
COPY test_runner.py /app/
#COPY utils/SecPLT_unittest_fail.json /app/

#RUN apt-get install -y python-paramiko libffi-dev && python -m pip install paramiko
RUN apt-get update && \
    apt-get install -y libpq-dev python3-dev gcc && \
    rm -rf /var/lib/apt/lists/*
RUN pip install jsonlines
RUN pip install tqdm
RUN pip install requests
RUN pip install ldap3
RUN pip install defusedxml database_connection 
RUN pip install paramiko pyyaml numpy
# Make script executable
RUN chmod +x /app/test_runner.py

