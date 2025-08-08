class Logging:
    @staticmethod
    def log_info(message):
        return f"INFO: {message}"

    @staticmethod
    def log_warning(message):
        return f"WARNING: {message}"

    @staticmethod
    def log_error(message):
        return f"ERROR: {message}"


print(Logging.log_error("hello"))
print(Logging.log_warning("tomato"))
print(Logging.log_info("cupboard"))
