# blockchain_in_py

This is a program of psuedo bitcoin

HOW TO RUN:
------
>pip install -r requirements.txt
>python3 -m main

    
usage:
------
> ./psudobitcoin createwallet
> ./psudobitcoin createblockchain -address <address>
> ./psudobitcoin printchain
> ./psudobitcoin printblock -height <height>
> ./psudobitcoin send -from <from> -to <to> -amount <amount>
> ./psudobitcoin getbalance -address <address>

functions :
------
> block, blockchain, pow
> database, client
> Utxo
> mining reward
> merkle tree

requirements :
------
>base58
>ecdsa
