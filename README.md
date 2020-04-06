# Django-Blog
A Blog Application integrated with WYSIWYG. Add, Edit, Delete and Update Blog Posted. This web interface provides ****Client-Side**** integration of WSYIWYG ( [Summernote](https://summernote.org/) ).

## **Requirements**
- Django==3.0.4
- django_summernote==0.8.11.6
- innovative_mind==1.0.1 (kidding)

## **Setup**
* Clone the repository using : <br/>
`git clone https://github.com/dmcrobin/Django-Blog.git`<br/>
`cd Django-Blog/`

* Create A Superuser : <br/>
`python manage.py createsuperuser` <br/>
Enter the username and password for the admin panel.

* Run Migration : <br/>
`python manage.py makemigrations`<br/>
`python manage.py migrate`<br/>

* All Done, Now Launch : <br/>
`python manage.py runserver`</br>
Visit [Localblog](http://127.0.0.1:8000/) and start writing your own blog, Enjoy!
