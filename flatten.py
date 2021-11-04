def flatten(obj):
    try:
        for item in obj:
            yield from flatten(item)
    except:
        yield obj
        
def flatten(obj):
    try:
        return [e for item in obj for e in flatten(item)]
    except:
        return [obj]
