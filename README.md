<h1 align="center">
	<img
		width="300"
		alt="The Lounge"
		src="https://avatars.githubusercontent.com/u/40245164?s=400&u=11bf153e3271d4434e3eed5d22623541eaee6ac0&v=4">
</h1>

<h3 align="center">
	Car Parking Support System
</h3>

[//]: # (<p align="center">)
[//]: # (	<strong>)
[//]: # (		<a href="">Website</a>)
[//]: # (		•)
[//]: # (		<a href="">Docs</a>)
[//]: # (		•)
[//]: # (		<a href="">Demo</a>)
[//]: # (	</strong>)
[//]: # (</p>)


<p align="center">
	<a href="https://github.com/alexsmith2910/CarParkingSupportSystem"><img
        alt="GitHub"
        src="https://img.shields.io/github/license/alexsmith2910/CarParkingSupportSystem?&style=flat-square">
    </a>
    <a href="https://github.com/alexsmith2910/CarParkingSupportSystem"><img
        alt="GitHub code size in bytes"
        src="https://img.shields.io/github/languages/code-size/alexsmith2910/CarParkingSupportSystem?color=red&label=Size&style=flat-square">
    </a>
	<a href="https://github.com/alexsmith2910/CarParkingSupportSystem/graphs/commit-activity"><img
        alt="GitHub commit activity"
        src="https://img.shields.io/github/commit-activity/m/alexsmith2910/CarParkingSupportSystem?color=blue&style=flat-square">
    </a>
</p>

## Overview

- **University Project:** An assignment given to us for our *Software Design* module. Our task was to create requirements analysis, documenting requirements, documenting design, development phases and finally software design artefacts.
- **Programming:** I decided to program this project based on the documents produced for the assignments.
- **Additional Programming:** I also wanted to improve the project where necessary to enhance my ability to program at a high level of understanding.
- **Programming language:** I chose to do this in Python due to working with **Python3** for many years now. I also chose Python because this system is mainly data oriented.
- **Why?** To be truthful, I was bored and thought it would be a great project for a portfolio and a fun challenge too. 

## Context

***This is the document provided to us.***

> Holborn Car Par Services is a small company that owns a few car parks
in Greater London. For some time they have been using a small software
system for administration, but the actual car park operation has simply
been based on a pay-and-display system. Management currently has access
to overall financial data (e.g. how much money was put in the machines per
car park per day) but no detailed information such as average time each car
stays, average car park occupancy and what times the car parks are used the
most. To have more information to help them optimise their operations (and
have more control of payments), it has been decided to replace the pay-anddisplay with a barrier controlled system. Thus, it is necessary to produce
software to support this change and provide more detailed information about
the car parks’ usage to management.

**List of features identified by management for the project:**

- The new system must control how much to **charge** each car park user
depending on how much **time the car was parked** and the **customer
type**
- It should be possible to see **how many cars are in a specific car park**
at any given time
- **“Happy hour”** - there should be a way to raise the barriers and let
customers in for no charge at the manager’s discretion for given periods
of time
- The system will need to allow **managers** to select a period of time and
will be able to **produce a report** showing the data for the relevant car
park usage and graphs representing this information
- The system will **produce reports at regular (and configurable) intervals** - 
the configuration will allow the user to specify what types of metrics 
are shown in the report from a list including average/maximum/minimum
cars in the park per hour, time spent by car and car park occupancy

## Installation and usage

You can download the all the files and run a couple of commands for it to work.

1. Download the files.
2. Open a new terminal > Navigate to the download folder > Type <br>
    `pip install -r requirements.txt`<br>
    or <br>
    `python -m  pip install -r requirements.txt`
3. Install a [Mongo Community Server](https://www.mongodb.com/try/download/community) >
   follow the steps and install [MongoDB Compass](https://www.mongodb.com/try/download/compass)
   to view the database easily.
4. Then you can run the program `main.py` in terminal or open the file manually.

