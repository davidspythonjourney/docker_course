# Use Python 3.11-slim as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your application files to the container
COPY first_flask.py /app/
COPY config.json /app/
COPY requirements.txt /app/


# Install any required dependencies (if needed)
# For example, if your project needs Flask, add the following:
# RUN pip install flask
RUN pip install -r requirements.txt

EXPOSE 80
# Run the application (modify the command as per your Flask setup)
CMD ["python", "first_flask.py"]
