
Official Installation Of Matplotlib

Matplotlib releases are available as wheel packages for macOS, Windows and Linux on PyPI. Install it using pip:

>>  python -m pip install -U pip

>>  python -m pip install -U matplotlib


more instructions please visit : https://matplotlib.org/stable/users/installing/index.html


About Errors :

I received the same error and I'm also in Python 3.6.0 ...

[AttributeError: 'version_info' object has no attribute '__version__']

If you want to dig a little more, you can type this in your console and detect which package is using this dependency.

>>   pip show pyparsing

In my case the output was something like this, indicating that packaging:

Name: pyparsing
Version: 2.4.7
Summary: Python parsing module
License: MIT License
Location:
Requires:
Required-by: packaging

To fix it, you can go with the suggestion from PaulMcG

pip install pyparsing==2.4.7