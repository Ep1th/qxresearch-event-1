import datetime

def greet(name):
    now = datetime.datetime.now()
    print(f"Привет, {name}!")
    print(f"Сейчас: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Это мой вклад в qxresearch-event-1")

if __name__ == "__main__":
    greet("Мир")