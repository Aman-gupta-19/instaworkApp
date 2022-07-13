# instaworkApp

Name: Aman Ajay Gupta
Email: aman.a.gupta19@gmail.com
LinkedIn: http://www.linkedin.com/in/aman-gupta-b140991a8


Installation:
-	In order to run this project exactly as intended we need to keep few things in mind which are as follows:
    o	Python version 3.9.7
    o	Django version 4.0.4
    o	Pipenv version 2022.7.4
    o	Not a must but I good to install debug toolbar as I have integrated it within project for ease of development (pip install django-debug-toolbar_
        -In order to start this debug toolbar you will have to uncomment line 137 in settings.py 
        -# "127.0.0.1" -> this line


Getting Started:
    -	In this application user will be able to see all the added members in the list page(main page), 
    we can access this using url “localhost:myApp/ListPage”.

    -	We have two more pages in addition to this, add page and edit page. Clicking the “+” sign on list page would take you to the add page or you can use url “localhost:myApp/AddPage” to directly access this page and to access edit page we have to click on any of the member listed on main page and it will take you to the edit page or else you can use “localhost:myApp/EditPage/?id=’some_id’” to directly access this page.


    -	With add page you can add a new member with his information and role and with edit page we can edit the existing member with the updated information/role and save it or else delete that particular record as well from this page.


Testing:
Following testing were carried on at unit level as well application as a whole:
      o	Adding new members
      o	Edit page loads user’s previous automatically
      o	Edit page updates data at the same ID to prevent duplication
      o	Deleting record from edit page
      o	Member count on top of list page
      o	Database working as intended
      o	CSS loading properly
      o	URls redirecting to intended page
      o	No breakdown at any stage of using application
      
      
Work breakdown:

      o Brainstorming/Gathering Requirements  --	1 Hour
      o Setting things up  --	1 Hour
      o Revising Django framework(learning)  --	3-4 Hours
      o Developing main page  --	2-3 Hours
      o Developing add page  --	1-2 Hours
      o Developing edit page  --	3-4 Hours
      o Applying CSS  --	0.5 Hour
      o Final touch up  --	1 Hour
      o Total time spent on Integrated testing  --	1 Hour
        Note: Unit testing time was included in the development itself.

