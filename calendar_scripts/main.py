from ics import Calendar
import requests

SOURCES_PATH = "calendar_sources.txt"
OUT_PATH = "virtual-econ-calendar.ics"


def main():
    with open(SOURCES_PATH) as f:
        content = list(filter(lambda z: len(z) > 0, map(lambda x: x.split('#')[0].strip(), f.readlines())))

    new_c = Calendar()
    for source in content:
        cal_text = requests.get(source).text
        c = Calendar(cal_text)
        new_c.events.update(c.events)

    with open(OUT_PATH, "w") as f:
        f.write(str(new_c))

    print(f"Saved new calendar to `{OUT_PATH}``")


if __name__ == "__main__":
    main()
