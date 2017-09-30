# Cuotiben

Features:

Uploading problems:
- For questions and solutions: upload image file or input plain text 
- Tool to screenshot image directly 
- Can have a way for students to also upload image of how they solved the problem 
- Option to tag categories based on the class, type (e.g. exam, hw, dis) and topic (e.g. probability, transforms, etc)
- Set sharing options: private, specific people, public
-> Give the problem a title   

Viewing problems:
- Toggle solution when necessary (by default not shown)
- Recommend similar questions (from those student has access to including public)
- Way to make notes or comments, or also show work they've done on it so far

Dashboard:
-> View of all the problems uploaded, can by default sort by when uploaded 
-> Something visual to be able to see what the problem is easily 
-> By default, show own images. Sidebar or option to view shared problems (could specifically select account name of other students who have shared)

Global section:
-> Place to find public questions by searching based on tags or title 
-> Need to direct when clicked on a problem to a page for that question

Bonus machine learning features:
predict score
suggest tags by looking at questions 

Dashboard:
- uploads button

Uploading problems page:
Receive:
- current tags of the user
- groups user is in 
Send to backend:
- problem and solution (could be in the form of image or plain text)
- title 
- comments 
- tags
- (optional) description 
- sharing option (public, private, if community: group-name)

View problems page:
- ordered squence of problems from filtered results 
- all information sent to backend earlier about each problem 

Community page:
Receive:
- list of groups user is in with link to group pages

Group page:
- similar to personal problem page but with only group's problems
- add user button 
- remove self from group 
- link to upload problems page



