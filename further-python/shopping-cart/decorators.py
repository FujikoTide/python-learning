from functools import wraps
from config import FEATURE_FLAGS, FeatureFlags


def feature_flag(flag_name):
    """Applies the wrapped function only if the feature flag is enabled in settings."""
    if FEATURE_FLAGS.get(flag_name, False):
        decorators = {
            FeatureFlags.DEBUG: debug_decorator,
            FeatureFlags.DEFAULT: default_decorator,
            FeatureFlags.PRINT_OUTPUT: print_output,
        }

        return decorators.get(flag_name, decorators[FeatureFlags.DEFAULT])
    else:
        return dummy_decorator


def print_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        print(output)
        return output

    return wrapper


# arbitrary for sake of example
def dummy_decorator(func):
    print("Dummy Decorator !!!")
    return func


# arbitrary for sake of example
def default_decorator(func):
    print("Default Decorator !!!")
    return func


# arbitrary for sake of example
def debug_decorator(func):
    print("Debug Decorator !!!")
    return func
