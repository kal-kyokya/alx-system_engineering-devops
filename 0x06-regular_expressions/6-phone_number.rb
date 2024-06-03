#!/usr/bin/env ruby
puts ARGV[0].scan(/[^\s][0-9]{10}/).join
