#Copyright 2017 MathWorks, Inc.
import warnings
from matlab.engine import pythonengine

def _get_async_or_background_argument(kwargs):
    if 'async' in kwargs and 'background' in kwargs:
        raise KeyError(pythonengine.getMessage('EitherAsyncOrBackground'))
    background = False
    if 'async' in kwargs:
        background = kwargs.pop('async', False)
        if not isinstance(background, bool):
            raise TypeError(pythonengine.getMessage('AsyncMustBeBool'))
        warnings.warn(pythonengine.getMessage('AsyncWillDeprecate'), DeprecationWarning)

    if 'background' in kwargs:
        background = kwargs.pop('background', False)
        if not isinstance(background, bool):
            raise TypeError(pythonengine.getMessage('BackgroundMustBeBool'))

    if kwargs:
        raise TypeError((pythonengine.getMessage('InvalidKwargs', list(kwargs.keys())[0].__repr__())))

    return background