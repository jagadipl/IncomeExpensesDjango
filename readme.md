Virtual Environment [virtualenv]
- virtualenv is a python tool that allows you to create isolated environment. 
- It is useful for managing different project on same computer.
- With virtual env you can have multiple seprate env with their own dependencies and libraries.

- Dependency Management: Package Management [Pipy] of different version
- Avoid Conflict: By Isolating dependencies
- Reproduce Easy: Other Can use your project easily.
- Safe: Risk of breaking system or other projects.


--- How to Create Virtual Env
pip install virtualenv
Create virtualenv
virtualenv <yourname>

 .\jagadip\Scripts\activate

For MAC and Linux
source envname/bin/activate

Deactivate Virtual Environment
deactivate

To Export All the Packages
pip freeze > requirements.txt


To import All the packages
pip install -r requirements.txt

For Django
pip install Django
pip install djangorestframework
