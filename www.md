# The World Wide Web

> Webpage: one document on the web
> Website: set of webpages

## Universal Resource Locators (URL)
https://www.mamamia.org/yeet/the/path
> protocol, domain name, path

## HTTP requests
### GET
* retrieve content
### HEAD
* GET without body 
### POST
* create new shit 
### PUT
* replace 
### PATCH
* modify 
### DELETE
* yeet 

## HTTP response codes
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

## Persistent connection
* HTTP runs on top of TCP
* allow browsers to issue multiple requests over the same connection

## Pipelining vs. Multiplexing
* Pipelining (HTTP 1.1), reponses have to be in the same order as request, performance issues if one request takes longer, security was crap
* Multiplexing (HTTP 2), give each request a number & match based on it (similar to sequence numbers)


