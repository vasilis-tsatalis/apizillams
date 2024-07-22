# Start from the official Python base image.
FROM python:3.9

# Set the current working directory
WORKDIR /apizilla

# Copy the file with the requirements to the /apizilla directory
COPY ./requirements.txt /apizilla/requirements.txt

# Install the package dependencies in the requirements file
# The --no-cache-dir is only related to pip, it has nothing to do with Docker or containers
RUN pip install --no-cache-dir --upgrade -r /apizilla/requirements.txt

# Copy the . directory inside the /apizilla directory
COPY . /apizilla

# Set the command to use fastapi run, which uses Uvicorn underneath
CMD ["fastapi", "run", "main.py", "--port", "8000"]