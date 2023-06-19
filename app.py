import controller_view as cv

if __name__ == '__main__':
    try:
        app = cv.App()
        app.run()
    except BaseException as e:
        input(e)
