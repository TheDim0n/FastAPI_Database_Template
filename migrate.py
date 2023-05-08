import os


def automigrate():
    os.system("alembic --name=postgres upgrade head")


if __name__ == "__main__":
    automigrate()
