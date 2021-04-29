# Blockchain in Python

## Table of Content

- [Introduction](#introduction)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Functions](#functions)
- [Requirements](#requirements)



## Introduction
This is a program of psuedo bitcoin

##  How to Run

```bash
    pip install -r requirements.txt
    python3 -m main
```
    
## Usage:

```bash
     ./psudobitcoin createwallet
     ./psudobitcoin createblockchain -address <address>
     ./psudobitcoin printchain
     ./psudobitcoin printblock -height <height>
     ./psudobitcoin send -from <from> -to <to> -amount <amount>
     ./psudobitcoin getbalance -address <address>
```

## Functions

    - block, blockchain, pow
    - database, client
    - Utxo
    - mining reward
    - merkle tree

## Requirements
    > base58
    > ecdsa
