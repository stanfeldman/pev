from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "pev",
    version = "0.1.0",
    author = "Stanislav Feldman",
    description = ("Python EVenter library"),
    url = "https://github.com/stanislavfeldman/pev",
    keywords = "eventer pubsub publish subscribe",
    packages=['pev'],
    classifiers=[
        "Topic :: Software Development"
    ],
)
