class CustomEnumerable

  def map(&block)
    result = []
    each do |element|
      result << block.call(element)
    end #each
    result
  end 
  
end

class ArrayWrapper

  include CustomEnumerable

  def initialize(*items)
    @items = items.flatten
  end #initialize

  def each(&block)
    @items.each(&block)
    self
  end 

  def ==(other)
    @items == other
  end

end 