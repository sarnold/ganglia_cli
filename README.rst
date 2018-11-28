===========
Ganglia_cli
===========

.. image:: https://img.shields.io/github/license/sarnold/ganglia_cli.svg
    :target: https://github.com/sarnold/ganglia_cli
    :alt: License

.. image:: https://badge.fury.io/gh/sarnold%2Fganglia_cli.svg
    :target: https://badge.fury.io/gh/sarnold%2Fganglia_cli
    :alt: Version

.. image:: https://travis-ci.org/sarnold/ganglia_cli.svg?branch=master
    :target: https://travis-ci.org/sarnold/ganglia_cli
    :alt: Build Status

.. image:: https://codeclimate.com/github/sarnold/ganglia_cli/badges/gpa.svg
    :target: https://codeclimate.com/github/sarnold/ganglia_cli
    :alt: Code Climate

.. image:: https://img.shields.io/github/issues/sarnold/ganglia_cli.svg
    :target: https://github.com/sarnold/ganglia_cli/issues?q=is:issue+is:open
    :alt: Issues

.. image:: https://img.shields.io/github/issues-pr/sarnold/ganglia_cli.svg
    :target: https://github.com/sarnold/ganglia_cli/issues?q=is:open+is:pr
    :alt: Pull Requests

A small Python library to send metrics to Ganglia from your Python code.
Supports UDP, multicast, group and spoofing.

Installing
==========

To install this update, clone this repository and::

  $ git clone https://github.com/sarnold/ganglia_cli
  $ cd ganglia_cli
  $ python setup.py install

To install the (original) upstream package::

  $ pip install ganglia

Note the upstream package may collide with other python modules named ``ganglia``.


Usage
=====

Sending metric over UDP::

  ganglia_cli = GMetric("udp://127.0.0.1")
  ganglia_cli.send(
      name='hits',
      units='req/sec',
      type='uint8',
      value=200,
      tmax=60,
      dmax=300,
      group='web'
  )


.. note:: This is an update of the last version on pypi:
          https://pypi.org/project/ganglia/
