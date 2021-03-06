"""Contains all the global configuration variables."""
# -*- coding: utf-8 -*-

# Copyright (c) 2008
#       Rafael Cunha de Almeida <almeidaraf@gmail.com>. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    3. The name of the author may not be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import os.path
import sys

from Config import Config

# global variables setup
if os.system('mkdir -p ~/.gmailreader'):
    sys.stderr.write('Unable to create ~/.gmailreader\n')
    raise SystemExit, 1

DRAFT = os.path.expanduser('~/.gmailreader/draft')
if not os.path.isfile(DRAFT):
    open(DRAFT, 'w').close()
TMP = os.path.expanduser('~/.gmailreader/tmp')
if not os.path.isfile(TMP):
    open(TMP, 'w').close()

_conf = Config(os.path.expanduser('~/.gmailreader/config'))

EDITOR = os.getenv('EDITOR')
if not EDITOR:
    EDITOR = _conf.get('editor', lambda: 'vi')

READER = os.getenv('READER')
if not READER:
    READER = _conf.get('reader', lambda: EDITOR)
