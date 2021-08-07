# Email
> 150 million emails sent every minute, 9/10 are spam lol

## Message formats
<img src="images/email_structure.png">

## How does it work?
1. Users use POP3 or IMAP to interact with their mailbox
2. Users & Message Transfer Agents use SMTP to send email from a source to a destination

## Interent Message Access Protocl (IMAP)
Sends commands to mail server to manipulate mailboxes
* LOGIN
* FETCH (fetch from folder)
* CREATE/DELETE (create or delete folder)
* EXPUNGE (remove messages marked for deletion)

## Multipurpose Interent Mail Extensions (MIME)
* Additional headers introduced (egg Content-Type) to indicate type of data in message (text, images, video, multipart)

### Base64 to encode binary to ASCII
egg. 
binary: 01101101 01100101
base64: 011011 01011 0101`00`
ascii: bVU=

How many characters does the Base64 encoding of 3,688 bytes have?
3,688/3=1229.33, so there are 1229 groups of 3 bytes and 1 byte left over.
Each of 3 bytes is encoded as 4 characters, so 4⋅1229=4916 characters.
The last byte is encoded as 2 Base64 characters, and two = signs are appended for padding.
Hence, the total number of characters is 4916+2+2=4920.