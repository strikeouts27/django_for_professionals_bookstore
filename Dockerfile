# Pull base image from docker hub. by not specifying a version I tell the hub to pull the latest file. 
FROM python
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /Users/andrewstribling/Desktop/dev/code/ch4-bookstore
# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copy project
COPY . .