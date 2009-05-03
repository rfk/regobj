#
#  This is the regobj setuptools script.
#  Originally developed by Ryan Kelly, 2009.
#
#  This script is placed in the public domain.
#

from distutils.core import setup

import regobj
VERSION = regobj.__version__

NAME = "regobj"
DESCRIPTION = "Pythonic object-based access to the Windows Registry."
LONG_DESC = regobj.__doc__
AUTHOR = "Ryan Kelly"
AUTHOR_EMAIL = "ryan@rfk.id.au"
LICENSE = "LGPL"
KEYWORDS = "windows registry"

setup(name=NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_descrition=LONG_DESC,
      license=LICENSE,
      keywords=KEYWORDS,
      modules=MODULES,
     )

