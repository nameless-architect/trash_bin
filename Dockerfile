#Download Python from DockerHub and use it
FROM python:3.9.0

#Set the working directory in the Docker container
WORKDIR /code

#Copy the dependencies file to the working directory
COPY requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the Flask app code to the working directory
COPY src/ .

EXPOSE 5000 

ENTRYPOINT [ "python" ]
#Run the container
CMD [ "app.py" ]    