Getting Start
=============

Link
----
    * GitHub: `   https://github.com/Mirio/amazonstoreprice/tree/master <https://github.com/Mirio/amazonstoreprice/tree/master>`_
    * Documentation: `http://amazonstoreprice.readthedocs.org/ <http://amazonstoreprice.readthedocs.org/>`_
    * PYPI: `https://pypi.python.org/pypi/amazonstoreprice <https://pypi.python.org/pypi/amazonstoreprice>`_


Badge
-----

.. image:: https://travis-ci.org/Mirio/amazonstoreprice.svg?branch=0.1
    :target: https://travis-ci.org/Mirio/amazonstoreprice

.. image:: https://img.shields.io/pypi/dm/amazonstoreprice.svg
    :target: https://pypi.python.org/pypi/amazonstoreprice

.. image:: https://img.shields.io/github/downloads/mirio/amazonstoreprice/total.svg
    :target: https://github.com/Mirio/amazonstoreprice/tree/master

.. image:: https://readthedocs.org/projects/amazonstoreprice/badge/?version=latest
    :target: http://amazonstoreprice.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/Mirio/amazonstoreprice/badge.svg?branch=0.1
    :target: https://coveralls.io/github/Mirio/amazonstoreprice?branch=0.1

Features
--------
    * Easy to find the price without using the Amazon API
    * Easy to use
    * Python 3.x +
    * Unittest
    * Custom Errors


Installation via Pip
--------------------

.. code-block:: bash
    :name: installation

    pip install amazonstoreprice


Installation from Source
------------------------

.. code-block:: bash
    :name: installation_source

    git clone https://github.com/Mirio/amazonstoreprice.git
    cd amazonstoreprice
    python setup.py install


Uninstall via Pip
-----------------

.. code-block:: bash
    :name: installation

    pip uninstall amazonstoreprice


Basic usage
-----------

Code:

.. code-block:: python
    :name: code

    from amazonstoreprice import AmazonStorePrice

    url = "http://www.amazon.it/Inside-Out-Ronnie-Del-Carmen/dp/B016LMC90O/" \
      "ref=sr_1_1?ie=UTF8&qid=1455389197&sr=8-1&keywords=inside+out"
    pricelib = AmazonStorePrice()
    print(pricelib.getprice(url, retry_ontemp=True))

Output:

.. code-block:: bash
    :name: code

    $ python example_getprice.py
    15.99

