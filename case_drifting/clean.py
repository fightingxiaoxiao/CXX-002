import shutil
for i in range(16):
    try:
        shutil.rmtree('processor'+str(i))
    except FileNotFoundError:
        pass