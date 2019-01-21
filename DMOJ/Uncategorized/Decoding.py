def bar():
    x = 1
    y = x + 1
    def magic(n):
        print(n)
    return magic

def replace_inner_function(outer, new_inner):
    new_inner = new_inner.__code__
    ocode = outer.__code__
    function, code = type(outer), type(ocode)
    iname = new_inner.co_name
    orig_inner = next(
        const for const in ocode.co_consts
        if isinstance(const, code) and const.co_name == iname)
    new_consts = tuple(
        new_inner if const is orig_inner else const
        for const in outer.__code__.co_consts)
    return function(
        code(ocode.co_argcount, ocode.co_nlocals, ocode.co_stacksize,
             ocode.co_flags, ocode.co_code, new_consts, ocode.co_names,
             ocode.co_varnames, ocode.co_filename, ocode.co_name,
             ocode.co_firstlineno, ocode.co_lnotab, ocode.co_freevars,
             ocode.co_cellvars),
        outer.__globals__, outer.__name__, outer.__defaults__,
        outer.__closure__)

replace_inner_function(foo, bar())()