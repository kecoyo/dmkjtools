from inflection import *


def camel_case(str):
    return camelize(snake_case(str), False)


def pascal_case(str):
    return camelize(snake_case(str))


def snake_case(str):
    str = re.sub(r"[\.\/ ]+", "_", str)
    return underscore(str)


def constant_case(str):
    return snake_case(str).upper()


def kebab_case(str):
    return snake_case(str).replace("_", "-")


def param_case(str):
    return snake_case(str).replace("_", "-")


def dot_case(str):
    return snake_case(str).replace("_", ".")


def path_case(str):
    return snake_case(str).replace("_", "/")


def title_case(str):
    str = re.sub(r"[\.\/]+", " ", str)
    return titleize(str)
