============
Installation
============

.. contents::
   :depth: 3


-----------------
Official releases
-----------------
Official releases are available from `PyPI`_.

.. _`PyPI`: https://pypi.python.org/pypi/twentytab-customadmin/


Install via pip
===============
The easier way to install ``customadmin`` is via `pip`_. Enter this command::

    pip install twentytab-customadmin

...and the package will install automatically.

.. _`pip`: https://pypi.python.org/pypi/pip/


Install via source code
=======================
Alternatively, you can download the .gz distribution file available from `PyPI`_ and unpack it. Inside there is a script named ``setup.py``. Enter this command::

    python setup.py install

...and, again, the package will install automatically.

.. _`PyPI`: https://pypi.python.org/pypi/twentytab-customadmin/

--------------------
Development versions
--------------------
If you prefer, you can get the latest source from our `github`_ repository::

   git clone https://github.com/20tab/twentytab-customadmin.git

Add the resulting folder to your `PYTHONPATH`_ or symlink the ``twentytab-customadmin`` directory
inside it into a directory which is on your PYTHONPATH, such as your Python
installation's ``site-packages`` directory.

You can verify that the application is available on your PYTHONPATH by
opening a Python interpreter and entering the following commands::

   >>> import customadmin
   >>> customadmin.VERSION
   (0, 7, '+dev')

When you want to update your copy of the source code, run ``git pull``
from within the ``twentytab-customadmin`` directory.

.. caution::

   The development version may contain bugs which are not present in the
   release version and introduce backwards-incompatible changes.

   If you're tracking master, keep an eye on the recent `Commit History`_
   before you update your copy of the source code.

.. _`github`: https://github.com/20tab/twentytab-customadmin
.. _`PYTHONPATH`: http://docs.python.org/tut/node8.html#SECTION008110000000000000000
.. _`Commit History`: https://github.com/20tab/twentytab-customadmin/commits/master
