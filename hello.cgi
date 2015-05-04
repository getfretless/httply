#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new

if cgi['name'].empty?
  honoriffics = ['Mr. President', 'Your Highness', 'Your Exaltedness']
  greeting = honoriffics.sample
else
  greeting = cgi['name']
end

puts cgi.header

puts "
<!doctype html>
<html>
  <head>
    <title>Mind... BLOWN</title>
  </head>
  <body>
    Hello, #{greeting}.
  </body>
</html>"
