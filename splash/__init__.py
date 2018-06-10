__version__ = '3.2'
from PyQt5.Qt import qVersion

from distutils.version import LooseVersion
version_info = tuple(LooseVersion(__version__).version)
pyqt_version = qVersion()
__all__ = ['__version__', 'version_info']
