# Sukasa

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip)
[![Build Status](https://travis-ci.com/O1sims/Sukasa.svg?branch=master)](https://travis-ci.com/O1sims/Sukasa)

## Overview

Sukasa is a Python-based web application that analyses current house prices to detect and report price imperfections. This application provides prospective house-buyers a way to investigate whether the houses they are purchasing are incorrectly valued based on social, economic, and geographic characteristics such as current wage levels, the price of similar houses in neighbouring areas, nearby amenities such as schools and shops, and the estate agent selling the house. The aim is to give more information &mdash; and therefore sovereignty &mdash; to potential consumers, or even just to help current homeowners overcome buyers remorse.

## Technology stack

The web application uses [Django](https://www.djangoproject.com/) as the backend framework and [Angular](https://angular.io/) as the frontend framework. Documentation of the RESTful API service is handled by [Swagger](https://swagger.io/). Development is done with [Docker](https://www.docker.com/) and run on [Google Kubernetes](https://cloud.google.com/python/django/kubernetes-engine). We use [ElasticSearch](https://www.elastic.co/) as our main database and [Kibana](https://www.elastic.co/products/kibana) as the data visualisation GUI. [`R`](https://www.r-project.org/) is the language of choice for any statistical research.

## Building the application

We use Docker in the development of Sukasa to make it easy to build, run and share. The following instructions show how it's built and run in Docker:
```
git clone https://github.com/O1sims/Sukasa.git
cd Sukasa
docker build -t sukasa:latest .
docker-compose up
```
By default, the main Sukasa application will run on port `8000`, the ElasticSearch database is accessible on port `9200` and Kibana is on port `5601`. The `docker-compose.yml` can be altered to allow these services to run on different ports. Swagger API documentation can be found at `localhost:8000/swagger/`.

Environmental variables for the application can be changed in the `docker-compose.yml` file.

## Contact

The best way to troubleshoot or ask for a new feature or enhancement is to create a Github [issue](https://github.com/O1sims/Sukasa/issues). However, if you have any further questions you can contact [me](mailto:sims.owen@gmail.com) directly.
