# Knapsack problem
require "cli-table"

t_all_posible = Table.new(["Lista", "Peso Total", "Beneficio Total"])
t_filtered    = Table.new(["Lista", "Peso Total", "Beneficio Total"])

CAPACITY = 60
LIST     = 0       # dirty enums lool
WEIGHT   = 1       # dirty enums lool
BENEFIT  = 2       # dirty enums lool

# item [:name, weight, benefit]
items = [
  ["A", 30, 100],
  ["B", 10, 70],
  ["C", 8, 70],
  ["D", 4, 100],
  ["E", 7, 40],
  ["F", 15, 100],
  ["G", 7, 10],
  ["H", 20, 50],
  ["I", 25, 15],
]

def number_to_binary(num)
  binary = num.to_s(2).rjust(9, '0')
  binary.chars.each_slice(9).map(&:join)
end

variations = []
0.upto(2**9 -1).each do |n|
  variations.push number_to_binary(n)
end

# using a bit mask
possible = []
0.upto(variations.length() -1) do |i|
  li = variations[i].first # code would be cleaner if variations as a Array(String) instead of Array(Array(String))......
  temp = []
  j = 0
  li.each_char do |c|
    if c == "1" then temp.push(items[j]) end
    j += 1
  end
  possible << temp
end

filtered = []
possible.each do |l|
  object = l.map{|l| l[LIST]}
  sumweight = l.sum{|n| n[WEIGHT]}
  sumbenefits = l.sum{|n| n[BENEFIT]}
  row = [object, sumweight, sumbenefits]
  t_all_posible.rows << row

  if sumweight <= CAPACITY
    t_filtered.rows << row
  end
end

puts "Todas las listas possibles"
t_all_posible.show

puts "Listas que cumplen con capacidad"
t_filtered.rows.sort_by!{|l| -l[BENEFIT]}
t_filtered.show
