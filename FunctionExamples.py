def standard_arg(arg):
   print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
     print(pos_only, standard, kwd_only)

standard_arg(10)
pos_only_arg(20)
kwd_only_arg(arg=30)
combined_example(40,50,kwd_only=60)