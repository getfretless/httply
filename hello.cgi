#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
puts cgi.header
page = 'home'
page = cgi['page'] unless cgi['page'].empty?

def render(page_name, &content)
  title = {'about' => 'About Us','home' => 'Welcome'}
  puts "<!doctype html><html><head><title>#{title[page_name]}</title></head>
  <body>#{yield}</body></html>"
end

render(page) do
  if page == 'about'
    "We are coders."
  else
    "Welcome. Have a look around."
  end
end
