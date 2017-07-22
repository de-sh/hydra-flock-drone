#!/usr/bin/env python

from distutils.core import setup

setup(name='hydra-flock-drone',
      version='0.0.1',
      description='A simulation for HYDRA: Drone API',
      author='W3C HYDRA development group',
      author_email='public-hydra@w3.org',
      url='https://github.com/HTTP-APIs/hydra-flock-demo',
      install_requires=['aniso8601==1.2.1',
                        'appdirs==1.4.3',
                        'click==6.7',
                        'Flask==0.11',
                        'Flask-Cors==3.0.3',
                        'Flask-RESTful==0.3.6',
                        'httplib2==0.10.3',
                        'isodate==0.5.4',
                        'packaging==16.8',
                        'persisting-theory==0.2.1',
                        'psycopg2==2.7.1',
                        'pyparsing==2.2.0',
                        'python-dateutil==2.6.0',
                        'pytz==2017.2',
                        'rdflib==4.2.2',
                        'six==1.10.0',
                        'SQLAlchemy==1.1.10',
                        'thespian==3.5.2',
                        'uritemplate==3.0.0',
                        'uWSGI==2.0.13.1',
                        'Werkzeug==0.12.2',
                        'rdflib-jsonld==0.4.0',
                        'requests==2.18.1']
)
