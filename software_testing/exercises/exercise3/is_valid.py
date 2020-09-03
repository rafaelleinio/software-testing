"""is_valid module."""


def is_valid(exp: str) -> bool:
    """Validate if expression is a valid identifier.

    Args:
        exp: string to be validated

    Returns:
        True: if is a valid identifier.
        False: if is not a valid identifier.

    """
    if not isinstance(exp, str):
        return False
    length = len(exp)
    if not (length >= 1 and length <= 6):
        return False
    if not exp[0].isalpha():
        return False
    if not all((c.isalpha() or c.isdigit()) for c in exp):
        return False
    return True
