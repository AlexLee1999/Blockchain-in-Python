action_lst = ['addblock', 'printchain', 'printblock', 'createblockchain']
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
                elif lst[1] == 'createblockchain':
                    return create_block_chain_parser(lst)
                    


def print_usage():
    print('usage: \n ./psudobitcoin exit \n ./psudobitcoin addblock -transactions <transactions> \n ./psudobitcoin printchain \n ./psudobitcoin printblock -height <height> \n')


def add_block_parser(lst):
    if len(lst) != 4:
        print_usage()
        return
    elif not lst[2] or lst[2] != '-transactions':
        print_usage()
        return
    else:
        if lst[3] != '':
            return ['addblock', lst[3]]
        else:
            print_usage()
            return


def print_block_parser(lst):
    if len(lst) != 4:
        print_usage()
        return
    elif not lst[2] or lst[2] != '-height':
        print_usage()
        return
    else:
        if lst[3].isalnum():
            return ['printblock', lst[3]]
        else:
            print_usage()
            return


def create_block_chain_parser(lst):
    if len(lst) != 4:
        print_usage()
        return
    elif lst[2] != '-address':
        print_usage()
        return
    else:
        if lst[3] != '':
            return['createblockchain', lst[3]]
        else:
            print_usage()
            return