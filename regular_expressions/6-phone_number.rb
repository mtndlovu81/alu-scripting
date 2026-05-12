#!/usr/bin/env ruby
puts ARGV[0].scan(/(?:\d\D*){10,10}/).join
