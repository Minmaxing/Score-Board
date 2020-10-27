# Final Project, Mark Dzoljic

## General information, screenshots and info

### General information

- Name of student: Mark Dzoljic
- Name of mentor: Julia
- Name of the project: MEC Scoreboard
- Deadline: 2020-10-01
- Summary:
    Make a webapplication that keeps track of scores and allow users to add/amend points. Webapp generates dynamic tables to show the intermittent scores.

### Problem Statement

Myrdinn Emrys College ([MEC](https://www.meclarp.com/)) is a Harry Potter inspired 4-day Live Action Role-playing event ([LARP](https://en.wikipedia.org/wiki/Live_action_role-playing_game)) during the summer holidays in Belgium. During the LARP, teachers give out housepoints to each of the five houses. The organization of the LARP keeps track of given points through the use of paper forms, which teachers fill in during the breaks. When all forms are filled out, the organization manually calculates the rankings with the help of a calculator and then manually brief all participants. This process usually is quite tedious and takes a lot of time, since all calculations have to be done manually and all scores are compromised when a form is missing or a teacher has neglected to hand in the form.

### Proposed solution

*Teachers inform the organization of given points through the use of a webapplication which automatically calculates the ranking between the houses.*

Note: I came up with this idea on my own, and took initiative myself. I am not paid/rewarded in any way by the organization to make this. I have informed the organization that I am making this website, but that I am making it for the course, and that it is up to them to decide whether to use it. It is important to note that the requirements  are *not* set by a third-party. This is in line with the [project-requirements](doc/Project_Requirements.md).

### Screenshots

Below are a number of screenshots of the finalized product.
![sc1](doc/screenshot1.png)
![sc2](doc/screenshot2.png)
![sc3](doc/screenshot3.png)

### Screencast

Please follow the Youtube Link below:
[Here](https://youtu.be/dIkBUvk-Pnk)

## How to Install

- Execute ```pip3 install -r requirements.txt```
- Execute ```python3 app/mecboard/manage.py makemigrations```
- Execute ```python3 app/mecboard/manage.py migrate```
- Execute ```python3 app/mecboard/manage.py createsuperuser``` and follow instructions.
- Execute ```python3 app/mecboard/manage.py runserver``` in a terminal. Visit ```127.0.0.1:8000``` for the application and ```127.0.0.1:8000/admin``` for the adminscreen.

## Features of the application and sketches

### Minimum viable product

- allow for an admin account to make teacher accounts
- allow teachers to log in and hand out points to houses
- allow teachers to edit their own old 'hand-out entries'
- produce a dynamic table containing the ranking between the houses visible to all visitors
- allow admin account to edit individual teacher handout entries and to reset the points database when the LARP is over
- Produce a dynamic table containing the points given by individual teachers to each house, visible only to the admin
- User interface must be clear, intuitive and aimed at mobile devices
- The website must be safe to use, and prevent SQL-injections.

### optional features

- allow admin to upload student database, which includes their real name, their In-Game name and their house.
- allow admin to manually edit individual student entries if a participant changes house throughout the LARP.
- allow teachers to give points to individual students. The application matches their name to their house and allocates points appropriately.
- allow visitors to see rankings *inside of* a house, to see which members gathered the most/least points of each individual house.
- allow a modified user interface for the Admin, who will likely be using a PC.
- allow admin to download all hand-out entries as an Excel-file for administration and safe-keeping.
- allow for automatic back-ups to another location after 5 entries.

### Sketches of the Webapplication

This schematic was made in the early design process of the app and is not a legitimate representation of the app. See the [Design Document](DESIGN.md) for more information on design choices in the early process.

- ![visual of several html pages aimed at mobile devices. It displays rhe ranking of five houses with the option to login and a procedure to add points to the houses](doc/Prototype_schematic_ver_0.1.png)

## Prerequisites and challanges

- For testing and data sources, a fictional database will be used. One option is to make that myself, another is to use the participant-list from last year which was made public in a PDF-file. The data would have to be transformed manually so it can be used by the webapplication.
- External components are needed to make this webapplication. Primarily Bootstrap, Flask, Django and sqlalchemy. The base of the application will be build on Django. Javascript is optional, but preferred.
- There are numerous *other options*, but they have their disadvantages. The organization could use a cloud-based Excel/Google-table file and share that amongst teachers. But it would mean that teachers can also view/change other teachers entries, and it isn't exactly user/mobile friendly. Instead of easy clicking, the teacher would have to manually type the name and house each time. There are work-arounds for this by using excel programming; but using a intuitive, well designed webapplication still triumphs that.
- Hardest parts:
    1. User Interface specifically aimed at mobile devices. This may require me to do more prototyping and asking several students for feedback whether they feel the UI is intuitive enough.
    2. The SQL programming, and allowing the admin to quickly reset the SQL table may prove a bit of a challange. I do deem it ought to be possible.

## Sanity Check

**Done**. All Project Requirements are met.

### Proposal accepted
