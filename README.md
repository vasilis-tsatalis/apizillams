# apizillams
Containerization Microservices based on Python Fastapi

# Run the Fastapi live srver
$ fastapi dev main.py

# Build the Docker Image
$ docker build -t apizilla .

# Start the Docker Container
$ docker run -d --name apizilla_container -p 8443:80 apizilla

# Run Docker Compose (d: detached)
$ docker-compose up -d

