from decimal import Decimal
from enum import StrEnum

TAX_RATE_PERCENTAGE = Decimal("20")
CURRENT_DISCOUNT = Decimal("10")


class FeatureFlags(StrEnum):
    DEBUG = "debug"
    DEFAULT = "default"
    PRINT_OUTPUT = "print_output"


FEATURE_FLAGS = {"debug": True, "print_output": True, "default": True}
