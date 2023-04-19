__all__ = [
    "DTProjectError",
    "RecipeProjectNotFound",
    "DTProjectNotFound",
    "MalformedDTProject",
    "UnsupportedDTProjectVersion",
]


class DTProjectError(RuntimeError):
    pass


class RecipeProjectNotFound(DTProjectError):
    pass


class DTProjectNotFound(DTProjectError):
    pass


class MalformedDTProject(DTProjectError):
    pass


class UnsupportedDTProjectVersion(DTProjectError):
    pass