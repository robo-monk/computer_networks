# Cryptography
> The research area concerned with creating cryptosystems

### Cryptosystem
* Set of algorithms with guaranteed security properties


### Kerckhoff's principle
* Security of the system should not depend on the screcy of the algorithms, but only the keys should remain secret

### Cryptoanalysis
* research on breaking cryptosystems


## Cipher
They make us of:
* KeyGen
* Enc
* Dec

**Encryption assumes a passive adversary who aims to break confidentiality. If they manage to obtain any infromation about the content of any message that they didnt have before the cryptosystem is broken. They are allowed only to learn the length of the message**


## Symetric-key encryption
> aka secret-key encryption
* uses one key K
* Alice & Bob agree on K and keep it secret

### Stream ciphers & Block ciphers
* Stream ciphers act on each character of the plain text individually
* Block chiphers divide the plaintext in blocks of equal length & act on each block

### Substitution ciphers & Transposition ciphers
* Substitution ciphers replaces a block with another one
* Transposition changes the order of them

> Transposition ciphers nowdays are only used as an after or before step to the substitution to increase security


## Stream Ciphers

### One-Time Pad (OTP)
* Alice wants to send Bob `M`
* Alice computes `C = M xor K` and sends `C`
* Bob can get M by `C xor K = M`

## Block Ciphers

