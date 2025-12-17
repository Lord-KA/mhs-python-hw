_header = """
\\documentclass{article}

% Language setting
% Replace `english' with e.g. `spanish' to change the document language
\\usepackage[english]{babel}

% Set page size and margins
% Replace `letterpaper' with `a4paper' for UK/EU standard size
\\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}

% Useful packages
\\usepackage{amsmath}
\\usepackage{graphicx}
\\usepackage[colorlinks=true, allcolors=blue]{hyperref}

"""

def headergen(title, author):
    result = _header
    result += f"\\title{{{title}}}\n"
    result += f"\\author{{{author}}}\n"

    result += "\\begin{document}\n"
    result += "\\maketitle\n"

    return result

def footergen():
    return "\\end{document}\n"

def tablegen(table):
    result = "\\begin{tabular}{|l|l|}\n"
    result += "\\hline\n"
    for [a, b] in table:
        result += str(a) + " & " + str(b) + " \\\\\n"
        result += "\\hline\n"
    result += "\\end{tabular}\n"

    return result
