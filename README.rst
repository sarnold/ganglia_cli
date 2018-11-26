=======
Ganglia
=======

A library to send metric to Ganglia in python.
Supports UDP, multicast, group and spoofing.

Installing
==========

To install this update, clone this repository, cd into it and run::

  $ python setup.py install

To install the upstream package::

  $ pip install ganglia

Note this version may collide with other python modules named ``ganglia``.


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
