# -*- coding: utf-8 -*-

import unittest

from ganglia_cli import GMetric

ignore = ('E501',)


class TestGMetric(unittest.TestCase):
    def setUp(self):
        self.gmetric = GMetric("udp://127.0.0.1")

    def test_packing(self):
        metric = {
            'slope': 'both',
            'name': 'foo',
            'value': 'bar',
            'tmax': 60,
            'units': '',
            'dmax': 0,
            'type': 'string'
        }

        meta, data = self.gmetric.pack(metric)
        self.assertEqual(meta, b"\000\000\000\200\000\000\000\000\000\000\000\003foo\000\000\000\000\000\000\000\000\006string\000\000\000\000\000\003foo\000\000\000\000\000\000\000\000\003\000\000\000<\x00\x00\x00\x00\x00\x00\x00\x00")

    def test_missing_keys(self):
        for key in ('name', 'value', 'type'):
            metric = {'name': 'foo', 'value': 'bar', 'type': 'string'}
            del metric[key]
            self.assertRaises(KeyError, self.gmetric.pack, metric)

    def test_allowed_types(self):
        for kind in ('string', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'float', 'double'):
            metric = {'name': 'foo', 'value': 'bar', 'type': kind}
            try:
                self.gmetric.pack(metric)
            except TypeError:
                self.fail("Raised TypeError for type {0}".format(kind))
        self.assertRaises(TypeError, self.gmetric.pack, {'name': 'foo', 'value': 'bar', 'type': 'int'})

    def test_spoofing(self):
        try:
            metric = {'name': 'foo', 'type': 'uint8', 'value': 'bar', 'spoof': 1, 'hostname': 'host'}
            self.gmetric.pack(metric)
            metric = {'name': 'foo', 'type': 'uint8', 'value': 'bar', 'spoof': True, 'hostname': 'host'}
            self.gmetric.pack(metric)
        except Exception:
            self.fail("This should not raise an exception!!")

    def test_group(self):
        metric = {'name': 'foo', 'type': 'uint8', 'value': 'bar', 'group': 'test'}
        meta, data = self.gmetric.pack(metric)
        self.assertEqual(meta, b"\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x03foo\x00\x00\x00\x00\x00\x00\x00\x00\x05uint8\x00\x00\x00\x00\x00\x00\x03foo\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00<\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05GROUP\x00\x00\x00\x00\x00\x00\x04test")
