require "cli-table"


def golden_search(a, b)
    t = Table.new(["i", "a", "b", "d", "x1", "x2", "f(x1)", "f(x2)"])
    phi = (Math.sqrt(5) - 1) / 2.0
    i = 0
    while i <= 20 do
        d = phi*(b - a)
        x1 = a + d
        x2 = b - d
        fx1 = f(x1)
        fx2 = f(x2)
        t.rows << [i, a, b, d, x1, x2, fx1, fx2]
        if fx1 > fx2 then b = x1 else a = x2 end
        i += 1
    end
    t.show
end

def f(x)
    # return (x - 4.1)**2
    # return x**2 - 6*x + 15

    # because its its to find max: - (fx)
    # f(x) will apear negative but that is because you need to flip it
    return - ( (-x**2 / 3.0) + x )
end

# dont forget to update a, b
golden_search(0, 4)
