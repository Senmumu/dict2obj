class Container: pass

def revert(obj):
    if isinstance(obj, Container): return revert_container(obj)
    elif isinstance(obj, dict): return revert_dict(obj)
    elif isinstance(obj, list): return revert_list(obj)
    elif isinstance(obj, tuple): return revert_tuple(obj)
    elif isinstance(obj, set): return revert_set(obj)
    else: return obj

def revert_container(obj_container: Container):
    return dict([key, revert(value)] for key, value in obj_container.__dict__.items())

def revert_dict(obj_dict: dict):
    return dict([key, revert(value)] for key, value in obj_dict.items())

def revert_list(obj_list: list):
    return list(revert(element) for element in obj_list)

def revert_tuple(obj_tuple: tuple):
    return tuple(revert(element) for element in obj_tuple)

def revert_set(obj_set: set):
    return set(revert(element) for element in obj_set)

def convert(obj):
    if isinstance(obj, dict): return convert_dict(obj)
    elif isinstance(obj, list): return convert_list(obj)
    elif isinstance(obj, tuple): return convert_tuple(obj)
    elif isinstance(obj, set): return convert_set(obj)
    else: return obj

def convert_dict(obj_dict: dict):
    converted = Container()

    for key, value in obj_dict.items():
        setattr(converted, key, convert(value))

    return converted

def convert_list(obj_list: list):
    return list(convert(element) for element in obj_list)

def convert_tuple(obj_tuple: tuple):
    return tuple(convert(element) for element in obj_tuple)

def convert_set(obj_set: set):
    return set(convert(element) for element in obj_set)