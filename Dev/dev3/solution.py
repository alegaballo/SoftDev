import gdb


class MEMORY_OFFSET(object):
    WORD = 4;
    DWORD = 8;


def print_out(output, last_line=True):
    out = output.split()
    print('-------------')
    for i in range(1, len(out), 2):
        print('> '+out[i])
    if last_line:
        print('-------------')


def print_list(address, format_, recursive=False):
    x=''
    for c in format_:
        if c == 'i':
            x+=gdb.execute('x/1dw' + hex(address), False, True)
            address+=MEMORY_OFFSET.WORD
        elif c == 'f':
            x +=gdb.execute('x/1fw' + hex(address), False, True)
            address += MEMORY_OFFSET.WORD
        elif c == 'p':
            x +=gdb.execute('x/1ag' + hex(address), False, True)
            address += MEMORY_OFFSET.DWORD
        elif c == 's':
            y = gdb.execute('x/1ag ' + hex(address), False, True)
            x += gdb.execute('x/1sb' + y.split()[1], False, True)
            address += MEMORY_OFFSET.DWORD
        elif c == 'l':
            x +=gdb.execute('x/1dg' + hex(address), False, True)
            address += MEMORY_OFFSET.DWORD
        elif c == '.':
            address += MEMORY_OFFSET.WORD
        elif c == 'n':
            out = gdb.execute('x/1ag' + hex(address), False, True)
            address += MEMORY_OFFSET.DWORD
    if recursive:
        print_out(x, False)
        next = int(out.split()[1],0)
        if next != 0:
            print_list(next, format_, recursive)
        else:
            print('-------------')
    else:
        print_out(x)

class pstruct(gdb.Command):
    def __init__(self):
        super(pstruct, self).__init__("pstruct", gdb.COMMAND_OBSCURE)

    def invoke (self, args, from_tty):
        params = args.split()
        address = int(params[0],0)#converting from hex string to int
        if 'n' in  params[1]:
            print_list(address, params[1], True)
        else:
            print_list(address, params[1])
pstruct()
