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
    python3 -m pip install -r requirements.txt
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

- Block, Blockchain, Pow
- Database, Client
- Utxo
- Mining Reward
- Merkle Tree
- Sign and Verify(TBD)
## Requirements
- Python >= 3.6
- base58
- ecdsa
