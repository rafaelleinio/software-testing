def is_valid(exp: str) -> bool:
    if not isinstance(exp, str):
        return False
    l = len(exp)
    if not (l >= 1 and l <= 6):
        return False
    if not exp[0].isalpha():
        return False
    if not all((c.isalpha() or c.isdigit()) for c in exp):
        return False
    return True
