def fileExists(filename):
    try:
        open(filename)
        return True
    except IOError:
        pass
    return False
