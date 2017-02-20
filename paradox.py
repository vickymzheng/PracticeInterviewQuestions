def paradox():
    try:
        raise Exception("Here")
    except Exception:
        return "There"
    finally:
        return "Or maybe there"

    return "Or here?"

print(paradox())  