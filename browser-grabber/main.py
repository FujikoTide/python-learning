import psutil

firefoxes = [
    process for process in psutil.process_iter() if process.name() == "firefox.exe"
]
for firefox in firefoxes:
    print(f"Process ID: {firefox.pid} | Name: {firefox.name()}")
print(len(firefoxes))
