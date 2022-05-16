def dos_veces_cero(*args):
    for n in args:
        if args[n] == 0 and args[n + 1] == 0:
            return True
        else:
            return False

print(dos_veces_cero(0,1,2,0,3,5,6,7,2,1,0,8,8,0))