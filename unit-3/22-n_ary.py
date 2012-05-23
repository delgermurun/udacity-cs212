# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        if args:
            args = (x,) + args
            r = f(args[-2], args[-1])
            args = list(args[:-2])
            args.reverse()
            for i in args:
                r = f(i, r)
            return r
        else:
            return x
    return n_ary_f

def l(x,y):
    return x,y

a = n_ary(l)
