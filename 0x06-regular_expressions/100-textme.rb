#!/usr/bin/env ruby

puts ARGV[0].scan(/\[from:\+?\d+\] \[to:\+?\d+\] \[flag:.*\]).join
