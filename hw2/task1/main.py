import latexgen

mytable = [
        [1, 2],
        [3, 4],
        ["five", 6],
        [7, "eight"]
]

doc = latexgen.headergen("Gleb Kashkin", "test")
doc += latexgen.tablegen(mytable)
doc += latexgen.footergen()

out = open("test.tex", "w")
out.write(doc)
out.close()
