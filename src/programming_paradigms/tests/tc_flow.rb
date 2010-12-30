# Unit tests for flow.rb

# The Clever Algorithms Project: http://www.CleverAlgorithms.com
# (c) Copyright 2010 Jason Brownlee. Some Rights Reserved. 
# This work is licensed under a Creative Commons Attribution-Noncommercial-Share Alike 2.5 Australia License.

require "test/unit"
require File.expand_path(File.dirname(__FILE__)) + "/../flow"

class TC_GeneticAlgorithm < Test::Unit::TestCase

  # test the creation of random strings
  def test_random_bitstring
    assert_equal(10, random_bitstring(10).size)
    assert_equal(0, random_bitstring(10).delete('0').delete('1').size)
  end

  # test the approximate proportion of 1's and 0's
  def test_random_bitstring_ratio
    s = random_bitstring(1000)
    assert_in_delta(0.5, (s.delete('1').size/1000.0), 0.05)
    assert_in_delta(0.5, (s.delete('0').size/1000.0), 0.05)
  end
  
  # test uniform crossover
  def test_uniform_crossover    
    p1 = "0000000000"
    p2 = "1111111111"    
    o = nil   
    silence_stream(STDOUT){o = VariationFlowUnit.new(Queue.new,Queue.new,0.0) }
    assert_equal(p1, o.uniform_crossover(p1,p2))
    silence_stream(STDOUT){o = VariationFlowUnit.new(Queue.new,Queue.new,0.0) }
    assert_not_same(p1, o.uniform_crossover(p1,p2))
    silence_stream(STDOUT){o = VariationFlowUnit.new(Queue.new,Queue.new,1.0) }
    s = o.uniform_crossover(p1,p2)        
    s.size.times {|i| assert( (p1[i]==s[i]) || (p2[i]==s[i]) ) }
  end
  
  # test that members of the population are selected
  def test_binary_tournament
    o = nil
    silence_stream(STDOUT){o = SelectFlowUnit.new(Queue.new,Queue.new) }
    pop = Array.new(10) {|i| {:fitness=>i} }
    10.times {assert(pop.include?(o.binary_tournament(pop)))}  
  end

  # TODO write tests for all algorithms
      
  # helper for turning off STDOUT
  # File activesupport/lib/active_support/core_ext/kernel/reporting.rb, line 39
  def silence_stream(stream)
    old_stream = stream.dup
    stream.reopen('/dev/null')
    stream.sync = true
    yield
  ensure
    stream.reopen(old_stream)
  end   
  
  # test that the algorithm can solve the problem
  def test_search    
    best = nil
    silence_stream(STDOUT) do
      best = search()
    end  
    assert_not_nil(best[:fitness])
    assert_equal(64, best[:fitness])
  end
  
end
