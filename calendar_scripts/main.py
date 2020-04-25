from ics import Calendar
import requests

SOURCES_PATH = "sources.txt"
OUT_PATH = "out.ics"


def main():
    with open(SOURCES_PATH) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    new_c = Calendar()
    for source in content:
        c = Calendar(requests.get(source).text)
        new_c.events.update(c.events)

    with open("out.ics", "w") as f:
        f.write(str(c))

    print(f"Saved new calendar to `{OUT_PATH}``")


if __name__ == "__main__":
    main()
