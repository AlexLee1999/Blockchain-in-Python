action_lst = ['printchain', 'printblock', 'createblockchain', 'createwallet', 'getbalance', 'send']
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
                if lst[1] == 'printchain':
                    return ['printchain']
                elif lst[1] == 'printblock':
                    return print_block_parser(lst)
                elif lst[1] == 'createblockchain':
                    return create_block_chain_parser(lst)
                elif lst[1] == 'createwallet':
                    return ['createwallet']
                elif lst[1] == 'getbalance':
                    return get_balance_parser(lst)
                elif lst[1] =='send':
                    return send_parser(lst)


                    


def print_usage():
    print('usage: \n ./psudobitcoin exit \n ./psudobitcoin printchain \n ./psudobitcoin printblock -height <height> \n ./psudobitcoin createblockchain -address <address> \n ./psudobitcoin send -from <from> -to <to> -amount <amount> \n')




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

def get_balance_parser(lst):
    if len(lst) != 4:
        print_usage()
        return
    elif lst[2] != '-address':
        print_usage()
        return
    else:
        if lst[3] != '':
            return['getbalance', lst[3]]
        else:
            print_usage()
            return

def send_parser(lst):
    if len(lst) != 8:
        print_usage()
        return
    elif lst[2] != '-from':
        print_usage()
        return
    elif lst[4] != '-to':
        print_usage()
        return
    elif lst[6] != '-amount':
        print_usage()
        return
    else:
        if lst[7] != '':
            return['send', lst[3], lst[5], int(lst[7])]
        else:
            print_usage()
            return