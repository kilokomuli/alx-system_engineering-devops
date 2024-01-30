#!/usr/bin/env ruby
# Script that outputs [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
