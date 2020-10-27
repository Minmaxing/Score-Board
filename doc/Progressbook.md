# Processbook

## Voorbereidende Milestones

- Submit proposal(20-08)
Done. No problems or issues noted. Proposal accepted.

- Submit an expanded design (22-08)
Done. No problems or issues noted. Design accepted.

- Make Processbook (22-08)
Done. This file.

- Build prototype (23-08)
Alright, first big choices/considerations were made here.

 1. Ditch flask! I can do everything I need to with Django, including the webserver. Minimize overhead, reduce unneccessary components.
 2. Many of the first problems I came across are because I need to get used to the Django Framework. Different Settings/Different templating language/ SQLite3 instead of SQl alchemy. There was a lot of looking at documentation!
 3. Pre-writing your database is a godsend! It makes things during modeling so much easier. Wish I had done this earlier during Pizza.
 4. Ditching all knowledge of Raw SQL commands and fully utilize DB.Model of Django and AdminModel to properly show data.
 5. Alright, a sort offish prototype is made. It doesn't work completely, but a large sketch is done. It does look extremely ugly and not all data is parsed well. I'll leave it here until then.

 ## Alpha Version

 1. System is working now, but inefficient. I have waaay too many views then neccessary; and I could improve on the UI. I also have a few bugs. It's not perfect yet
 
 2. Django, when understood; can be an amazing system.

 ## Beta Version

 1. Quality of life improvements
 - search can now be used with only one letter, and it will give all the results.
 - Points are now correctly added up.

## Final version

- Database models now linked and give sum of points per team and per teacher.
- Points displayed per team on index page
- Allow teachers to display
- Bootstrap and CSS improvements to the website
- JS added?