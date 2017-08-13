# Project: Movie Trailer Website
A demo web page for viewing movies trailers built as a part of the Udacity full-stack Nanodegree program. This project demonestrate the use of a movie object class in python to generate a static webpage which display and play list of movies trailers from youtube.

## Requirement and setup
Require Python 2.7 to run this project. Download and details of installation and setup can be found at:
https://www.python.org/download/releases/2.7/

## Table of Contents
1. Demo
2. Download
3. File structure

## Demo

## Download 
Project files may be downloaded at 
or clone the repo @ https://github.com/dthinley/movie_trailer.git

## File Structure and documentations
This project contained following files:
# 1. media.py:
Media.py has the object class that provides the data structure which consisted of four class variables, a simple constructor method, and a class medthods for playing the videos.

# 2. media_center.py:
In this file, the content of movies information is stored and created. The constructor method is called when a new movie object is added. This file include following aguments like, title, years, poster_url, and trailer_url.

# 3. fresh_tomatoes.py:
This file is like a template of the website, editing this file will change the outlook of the website. The file contains html, CSS and javascript. In this project css and javascript file are seperated and store in seperate folder. Just editing this file wouldn't bring any changes to the fresh_tomatoes.html. media_center.py file have to run after editing the fresh_tomatoes.py to bring the changes in layout. 


Movie Trailer Website/


    ├──css--main.css
    ├──image--------social-icons.jpg
    ├──js--------main.js
    ├──media.py
    ├──media_center.py
    ├──fresh_tomatoes.py
    ├──fresh_tomatoes.html
    └──README.md
