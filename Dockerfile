# define base image
FROM python:3.8

# set a directory for the app
WORKDIR /app

# copy all files to the container WORKDIR
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port for web app
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]
#CMD ["flask", "run"]
