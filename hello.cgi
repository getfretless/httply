#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
puts cgi.header

title = {
  'about' => 'About Us',
  'home' => 'Welcome'
}

page = 'home'
page = cgi['page'] unless cgi['page'].empty?

html_head = "<!doctype html><html><head>
    <title>#{title[page]}</title></head><body>"

html_foot = "</body></html>"

if cgi['page'] == 'about'
  puts "#{html_head} We are coders. #{html_foot}"
else
  puts "#{html_head} Wecome. Have a look around. #{html_foot}"
end
