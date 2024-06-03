#!/usr/bin/env ruby
puts ARGV[0].scan(/[^ A-Za-a-]\d{10}/).join
