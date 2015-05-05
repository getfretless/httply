#!/usr/bin/env ruby
require 'cgi'
require 'erb'

cgi = CGI.new
puts cgi.header
page = 'home'

pages = {'about' => 'About Us', 'home' => 'Welcome'}
if pages.keys.include?(cgi['page'])
  page = cgi['page']
end

title = pages[page]

def render(title, &content)
  layout = File.read 'layout.html.erb'
  puts ERB.new(layout).result(binding)
end

def load_content(page)
  File.read "#{page}.html"
end

render(title) do
  load_content page
end
