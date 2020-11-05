import time
import sys, argparse
import random
import pymouse

def main():
    parser = argparse.ArgumentParser(description="Make sure screen stays undimmed by moving mouse")
    parser.add_argument('-t',"--time",type=float,default = 10.0,help="Enter the time in seconds(default 10s)")
    args = vars(parser.parse_args())

    t = args['time']
    stop = False
    while not stop:
        mouse = pymouse.PyMouse()
        (x,y) = mouse.position()
        mouse.move(x,y)
        print(f"Sleeping for {t} secs",end='\r',flush=True)
        time.sleep(t)

        rand = random.randint(-2,2)
        mouse.move(x+rand,y+rand)

if __name__=='__main__':
    main()
