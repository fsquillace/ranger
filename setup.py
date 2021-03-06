#!/usr/bin/env python
# Copyright (C) 2009, 2010, 2011  Roman Zimbelmann <romanz@lavabit.com>
# This software is distributed under the terms of the GNU GPL version 3.

import distutils.core
import ranger

if __name__ == '__main__':
	distutils.core.setup(
		name='ranger',
		description='Vim-like file manager',
		long_description=ranger.__doc__,
		version=ranger.__version__,
		author=ranger.__author__,
		author_email=ranger.__email__,
		license=ranger.__license__,
		url='http://savannah.nongnu.org/projects/ranger',
		scripts=['ranger/data/ranger'],
		data_files=[('share/man/man1', ['doc/ranger.1'])],
		package_data={'ranger': ['data/*', 'defaults/rc.conf',
			'defaults/rifle.conf']},
		packages=('ranger',
		          'ranger.api',
		          'ranger.colorschemes',
		          'ranger.container',
		          'ranger.core',
		          'ranger.defaults',
		          'ranger.ext',
		          'ranger.fsobject',
		          'ranger.gui',
		          'ranger.gui.widgets'))
