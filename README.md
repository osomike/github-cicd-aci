# Weather App

This repository contains a Python application that retrieves live weather data from OpenWeatherMap for a given latitude
 and longitude on the globe and store the data in a PostgreSQL database.

The application also includes modules to retrieve the coordinates from a tuple city and country using data stored in a
 in the PostgreSQL database.

To run the application locally, clone the repository and run the following command:
```
python app.py --city XX --country YY.
```

For more information about the parameters, you can also run:
```
python app.py --help
```


Notes:
1. To run it locally, make sure the environmental variable ```PYTHONPATH``` includes the this root folder.
2. You will need the API keys as environmental variables.
3. It is also possible to define the environmental variables ```COUNTRY_TARGET``` and ```CITY_TARGET``` to execute the 
program.

## Infrastructure
The infrastructure folder contains Terraform code to deploy the infrastructure in Azure. The infrastructure consists of a Container Instance, Data Factory, a PostgreSQL database, and a container registry.

## Application
The ```app/main.py``` file is the main entry point for the Python application.
It retrieves live weather data from OpenWeatherMap using the latitude and longitude coordinates passed as arguments.

The ```app/mylyb/cities.py``` module is used to retrieve the latitude and longitude coordinates from the PostgreSQL 
database using the city and country data.

## Docker
The Dockerfile is used to containerize the Python application.
The Docker image is automatically built and pushed to a container registry as part of the CICD process.

You can also run the image locally. But you to build it you will the credentials for the API and for the Database.

## CICD
The CICD process is implemented using GitHub workflows. The workflows include:
1. Testing.
2. Code linting.
3. Security scanning using CodeQL.
4. Building and tagging the application.
5. Pushing the Docker image to the container registry.
