def ErrorM():
    try:
        import natch
    except ModuleNotFoundError:
        print("ModuleNotFoundError")

ErrorM()
