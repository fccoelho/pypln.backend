# coding: utf-8
#
# Copyright 2012 NAMD-EMAP-FGV
#
# This file is part of PyPLN. You can get more information at: http://pypln.org/.
#
# PyPLN is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyPLN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyPLN.  If not, see <http://www.gnu.org/licenses/>.

import cPickle

import nltk
from collections import defaultdict
from pypelinin import Worker
import MySQLdb

SPHINX_HOST = "127.0.0.1"
SPHINX_PORT = 9306
SPHINX_INDEX = 'pypln_realtime'


class Sphinxsearch(Worker):
    """Insert a document into a RT index in sphinsearch"""
    requires = ['text', '_id']
    connection = MySQLdb.connect(hostname=SPHINX_HOST, port=SPHINX_PORT)
    cursor = connection.cursor()

    def process(self, document):
        ID = int('0x'+str(document['_id']), 16)
        self.cursor().execute("INSERT INTO {} (id, text) values ({}, {})".format(SPHINX_INDEX, ID, document['text']))


