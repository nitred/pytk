# About
All the things needed for Atom editor

# Snippets
Put the following into a file called snippets.cson and place it inside .atom dir.
```
'.source.python':
  'New Class':
    'prefix': 'classdef'
    'body': 'class $1ClassName(${2:object}):\n\t"""${3:docstring for $1ClassName.}"""\n\n\tdef __init__(self, ${4:arg}):\n\t\t"""${3:Initialize the class.}"""\n\t\tself.arg = arg\n'

  'InitComments':
    'prefix': 'newfile'
    'body': '# !/usr/bin/env python\n# -*- coding: utf-8 -*-\n\"\"\"Docstring for module.\"\"\"\n'

  'Initfile':
    'prefix': 'initinit'
    'body': '# !/usr/bin/env python\n# -*- coding: utf-8 -*-\n"""Initialize module utils."""\n'

  'New Test Class':
    'prefix': 'testclass'
    'body': '# !/usr/bin/env python\n# -*- coding: utf-8 -*-\n"""Docstring for module."""\n\n\nimport unittest\n\n\nclass ${1:ClassName}(unittest.TestCase):\n\t"""docstring for class."""\n\n\tdef setUp(self):\n\t\t"""Setup the class."""\n\t\tpass\n\n\tdef tearDown(self):\n\t\t"""Cleanup the class."""\n\t\tpass\n\n\tdef test_method1(self):\n\t\t"""test_method1."""\n\t\tself.assertEqual(\'a\', \'a\')\n\t\tself.assertTrue(1 == 1)\n'

  'main':
    'prefix': 'main'
    'body': 'if __name__ == \"__main__\":\n\t'

  'futureprint':
    'prefix': 'printf'
    'body': 'from __future__ import print_function\n\t'

  'docs':
    'prefix': 'docs'
    'body': '"""$1."""'

  'log.debug':
    'prefix': 'logd'
    'body': 'logger.debug("$1: {0}".format())'

  'log.info':
    'prefix': 'logi'
    'body': 'logger.info("$1: {0}".format())'

  'log.error':
    'prefix': 'loge'
    'body': 'logger.error("$1: {0}".format())'

```
