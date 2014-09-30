csr-generator
=============

CSR Generator

    # python csr-generator.py
    help: parameters required are --domain, --state, --city, --organization
    # python csr-generator.py --domain example.com --state CA --city LA --organization Company
    Generating a 2048 bit RSA private key
    ...........................+++
    .................................................................................+++
    writing new private key to 'example_com.key'
    -----
    Done
    # ls
    csr-generator.py  example_com.csr  example_com.key
