import sys
from ImgTiler.ImageTiler import SplitImage 
from ImgTiler.ImageTiler import CombineTiles

from pkg_resources import get_distribution, DistributionNotFound

try:
    VERSION = get_distribution(__name__).version
except DistributionNotFound: # pragma: no cover
    VERSION = 'unknown'
    
__version__ = VERSION
__all__ = ['SplitImage', 'CombineTiles']

# Import README.md as a docstring, only when generating documentation
if "pdoc" in sys.modules:
    with open("README.md", "r") as fh:
        _readme = fh.read()