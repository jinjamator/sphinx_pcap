=================
Sphinx PCAP
=================

A Sphinx_ plugin that allows the inclusion of pcap files.

Prerequisites
=============

Working installation of thshark (wireshark cli)

Installation
============

The Sphinx CSV filter plugin is available as a pip_ package.

To install, run::

    $ pip install sphinx_pcap

To update, run::

    $ pip install -U sphinx_pcap

Set Up
======

To include the extension, add this line to ``config.py`` in
your Sphinx project::

    extensions = ['sphinx_pcap']

If you're using other extensions, edit the existing list, or add this::

    extensions.append('sphinx_pcap')

Use
===

This plugin adds the include_pcap directive.

