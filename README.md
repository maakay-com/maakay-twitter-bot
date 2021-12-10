# Twitter Tip Bot | Maakay

## Introduction
The bot will allow the users to tip any other users on twitter using TNBC.

## How’ll it work?
The users can deposit TNBC into their twitter account and then use those TNBC to send tips to any twitter user.

### Depositing TNBC
They will send a direct message to the bot account using `@deposit` command. The bot will then reply with the account number, memo and QR code. Once TNBC is sent, the users can check their twitter balance with the `@balance` command.

### Withdrawing TNBC
They can use the command `@withdraw account_number: ACCOUNT_NUMBER amount_of_tnbc: AMOUNT` in the private message of the bot to withdraw TNBC into their wallet.

### Check Balance
The users can check their twitter balance using `@balance` command.

### How’ll they tip?
They’ll need to create a tweet mentioning @maakay using the format `@maakay tip #TNBC 200 @user_they_want_to_tip`

The bot will then scan for the mentions and reply to the tweet with `@user tipped @user_who_got_tipped AMOUNT #TNBC`
