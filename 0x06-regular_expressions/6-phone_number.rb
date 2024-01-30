#!/usr/bin/env ruby
# Regx matching 10 digits number
puts ARGV[0].scan(/^[0-9]{10}$/).join
