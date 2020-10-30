action_lst = ['addblock', 'printchain', 'printblock']
def parsecmd(cmd):
    lst = cmd.split(' ')
    if lst[0] != './psudobitcoin':
        print_usage()
        return
    else:
        if lst[1] == 'exit':
            return ['exit']
        else:
            if lst[1] not in action_lst:
                print_usage()
                return
            else:
                if lst[1] == 'addblock':
                    return add_block_parser(lst)
                elif lst[1] == 'printchain':
                    return ['printchain']
                elif lst[1] == 'printblock':
                    return print_block_parser(lst)
                    


def print_usage():
    print('usage: \n ./psudobitcoin exit \n ./psudobitcoin addblock -transactions <transactions> \n ./psudobitcoin printchain \n ./psudobitcoin printblock -height <height> \n')


def add_block_parser(lst):
    if not lst[2] or lst[2] != '-transactions':
        print_usage()
        return
    else:
        return ['addblock', lst[3]]


def print_block_parser(lst):
    if not lst[2] or lst[2] != '-height':
        print_usage()
        return
    else:
        if lst[3].isalnum():
            return ['printblock', lst[3]]
        else:
            print_usage()
            return
