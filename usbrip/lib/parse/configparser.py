#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""LICENSE

Copyright (C) 2019 Sam Freeside

This file is part of usbrip.

usbrip is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

usbrip is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with usbrip.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Sam Freeside (@snovvcrash)'
__email__  = 'snovvcrash@protonmail[.]ch'
__site__   = 'https://github.com/snovvcrash/usbrip'
__brief__  = 'Configuration file parser'

import os
from configparser import ConfigParser

from usbrip.lib.core.common import CONFIG_FILE
from usbrip.lib.core.common import print_info
from usbrip.lib.core.common import print_warning


def config_parse():
	conf_parser = ConfigParser(allow_no_value=True)
	conf_parser.optionxform = str

	os.makedirs(CONFIG_FILE.rsplit('/', 1)[0], exist_ok=True)

	if os.path.isfile(CONFIG_FILE):
		conf_parser.read(CONFIG_FILE, encoding='utf-8')
		print_info(f'Configuration loaded: "{CONFIG_FILE}"')

	else:
		print_warning('No configuration file found, creating new one...')

		conf_parser.add_section('history')
		conf_parser.set('history', 'password', 'r1pp3r')

		conf_parser.add_section('violations')
		conf_parser.set('violations', 'password', 'r1pp3r')

		print_info(f'New configuration file: "{CONFIG_FILE}"')

		with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
			conf_parser.write(f)

	return conf_parser
