# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import datetime

now = datetime.datetime.now()

last_week_start = now - datetime.timedelta(days=now.weekday()+7)
for i in range(1, 7):
    day=now - datetime.timedelta(days=now.weekday()+7-i)
    print(day)