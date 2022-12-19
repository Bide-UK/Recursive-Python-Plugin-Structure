from plugins import Base

if __name__ == '__main__':
    print('Running Main')
    for p in Base.plugins:
        inst = p()
        inst.start()
    print("Finish")

