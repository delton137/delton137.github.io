import glob as glob
import os
import re
from natsort import natsorted
import bibtexparser as bt


def normalize_name_to_initials(name):
    name = name.strip()

    # If name is already in initials format (e.g., "D. C. Elton" or "D. Elton"), return as-is
    if re.fullmatch(r"([A-Z]\.\s?)+[A-Z][a-z]+", name):
        return name

    # Split name into parts
    parts = name.split()
    if len(parts) < 2:
        return name  # can't process single-word names

    *first_names, last_name = parts
    initials = " ".join(f"{fn[0]}." for fn in first_names if fn)
    return f"{initials} {last_name}"


def format_authors(author_field):
    author_field = author_field.replace('\n', '').replace('\r', '')  
    authors = author_field.split("and ")
    if len(authors) > 1:
        formatted = []
        for author in authors:
            author = author.strip()
            if ',' in author:
                # Format: Last, First
                last, first = [x.strip() for x in author.split(",", 1)]
                name = f"{first} {last}"
                name = normalize_name_to_initials(name)
                formatted.append(name)
            else:
                # Format: First Last
                formatted.append(normalize_name_to_initials(author))
        return ", ".join(formatted)
    else:
        return authors[0]

def parse_bib(f):
    bib_database = bt.bparser.BibTexParser(common_strings=True).parse_file(open(f))

    bd = bib_database.entries[0]

    s = "<span style=\"font-size:0.9em; font-family: helvetica;\"><strong>"+bd['title']+"</strong><br>" #

    if ('note' in bd.keys()):
        s += bd['note']+"<br>"

    authors_converted = format_authors(bd['author'])

    s += authors_converted.replace(" and ",", ").replace(" and", ",")+"." + "<br>"

    if 'journal' in bd.keys():
        s +=  " *"+bd['journal']+"*."

    elif 'booktitle' in bd.keys():
        s +=  " Chapter in *"+bd['booktitle']+"*."

    if 'volume' in bd.keys():
        if not(str(bd['volume']).replace(" ", "")==""):
            s += " **"+bd['volume']+"**"

    if 'number' in bd.keys():
        if not(str(bd['number']).replace(" ", "")==""):
            s +=  " ("+bd['number']+")"

    if 'pages' in bd.keys():
        if not(str(bd['pages']).replace(" ", "")==""):
            s +=  " pgs "+bd['pages']+"."

    s += " ("+bd['year']+")"

    s += "<br>"

    if not('hide' in bd.keys()):
        s += " [[.bib](../"+f.replace("/home/dan/Dropbox/delton137.github.io/", "")+")]"

    pdf_link = f.replace(".bib", ".pdf")

    if 'url' in bd.keys():
        s += "  [[link]("+bd['url']+")]"

    if 'arxiv' in bd.keys():
        s += "  [[arXiv]("+bd['arxiv']+")]"
        if not(os.path.exists(pdf_link)):
            s += "  [[pdf]("+bd['arxiv'].replace("/abs/", "/pdf/")+")]"

    if 'medrxiv' in bd.keys():
        s += "  [[medRxiv]("+bd['medrxiv']+")]"

    if os.path.exists(pdf_link):
        pdf_link = pdf_link.replace("/home/dan/Dropbox/delton137.github.io/", "")
        s += "[[pdf](../" + pdf_link + ")]"

    supp_link = f.replace(".bib", "_supplementary_info.pdf")
    if os.path.exists(supp_link):
        supp_link = supp_link.replace("/home/dan/Dropbox/delton137.github.io/", "")
        s += "[[supplementary info](../"+supp_link+")]"


    if 'press_release' in bd.keys():
        s += "  [[Press Release]("+bd['press_release']+")]"

    s += "</span>"

    return s


s = """---
id: 1917
title: Research
author: delton137
layout: page
---

See also [Google Scholar](https://scholar.google.com/citations?user=KG0pbOYAAAAJ)

"""

#"""
#<h1 id="no_toc">Table of contents</h1>
#* TOC
#{:toc}
#
#"""

folders = natsorted(glob.glob("assets/my_papers/*"))

tot = 0

for folder in folders:
    folder_name = folder.split("/")[-1]
    folder_name = folder_name.replace("A_AI_general","Artificial intelligence")
    folder_name = folder_name.replace("B_AI_medical_imaging","Machine learning for medical imaging")
    folder_name = folder_name.replace("C_AI_molecular_design","Machine learning for molecular design")
    folder_name = folder_name.replace("D_Physics_energetic_materials","Physics of detonation")
    folder_name = folder_name.replace("E_Physics_water","Physics of water")
    folder_name = folder_name.replace("F_other","Physics of turbulence")
    folder_name = folder_name.replace("G_preprints","Preprints")

    print("-------"+folder_name+"-----------")

    s += "# "+folder_name+"\n"

    files = natsorted(glob.glob(folder+"/*.bib"), reverse=True)

    for f in files:
        print(os.path.basename(f))
        tot += 1
        s += parse_bib(f).replace("{", "").replace("}", "")
        s += "\n\n"

s = s.replace("Pritam Mukherjee", "P. Mukherjee")
s = s.replace("Mannudeep K Kalra", "M. K. Kalra")
s = s.replace("Mark Walters", "M. Walters")
s = s.replace("Artem B Mamonov", "A. B. Mamonov")
s = s.replace("Emiliano G Frias", "E. G. Frias")
s = s.replace("James Y Sato", "J. S. Sato")
s = s.replace("Thomas J Schultz", "T. J. Schultz")
s = s.replace("Bernardo  C. Bizzo", "B. C. Bizzo")
s = s.replace("Keith J Dreyer", "K. J. Dreyer")
s = s.replace("Giridhar Dasegowda", "G. Dasegowda")
s = s.replace("Martynas Ziemelis", "M. Ziemelis")
s = s.replace("Daniel C Elton","D. C. Elton")
s = s.replace("Daniel C. Elton","D. C. Elton")
s = s.replace("Daniel Elton","D. C. Elton")
s = s.replace("Anastasios Nikolas Angelopoulos","A. N. Angelopoulos")
s = s.replace("Stuart R. Pomerantz","S. R. Pomerantz")
s = s.replace("Christopher P. Bridge","C. P. Bridge")
s = s.replace("Michael H. Lev","M. H. Lev")
s = s.replace("R Gilberto Gonzalez","R. G. Gonzalez")
s = s.replace("Michael I. Jordan","M. I. Jordan")       
s = s.replace("Elizabeth D. Williams","E. D. Williams")
s = s.replace("James D. Riches","J. D. Riches")
s = s.replace("Peter D. Spencer","P. D. Spencer")
s = s.replace("Peter W. Chung","P. W. Chung")
s = s.replace("Mark D. Fuge","M. D. Fuge")
s = s.replace("Gaurav Kumar","G. Kumar")
s = s.replace("Francis G. Van Gessel","F. G. Van Gessel")
s = s.replace("Zois Boukouvalas","Z. Boukouvalas")
s = s.replace("Mark S. Butrico","M. S. Butrico")
s = s.replace("Brian C. Barnes","B. C. Barnes")
s = s.replace("Seung Yeon Shin","S. Y. Shin")
s = s.replace("James L. Gulley","J. L. Gulley")
s = s.replace("Sungwon Lee","S. Lee")
s = s.replace("Ronald M. Summers","R. M. Summers")
s = s.replace("Perry J. Pickhardt","P. J. Pickhardt")
s = s.replace("Veit Sandfort","V. Sandfort")
s = s.replace("DeCarlos E. Taylor","D. E. Taylor")
s = s.replace("William D. Mattson","W. D. Mattson")
s = s.replace("Yingying Zhu","Y. Zhu")
s = s.replace("Mohammedhadi Bagheri","M. Bagheri")
s = s.replace("N. N. Mehta","P. C. Grayson")
s = s.replace("Peter A. Pinto","P. A. Pinto")
s = s.replace("Alberto A. Perez","A. A. Perez")
s = s.replace("Peter M. Graffy","P. M. Graffy")
s = s.replace("Youbao Tang","Y. Tang")
s = s.replace("Yuxing Tang","Y. Tang")
s = s.replace("Thomas Shen","T. Shen")
s = s.replace("Tejas Sudharshan", "T. S.")
s = s.replace("Michelle Fritz","M. Fritz")
s = s.replace("Jiamin Liu","J. Liu")
s = s.replace("Victoria Noe-Kim","V. Noe-Kim")
s = s.replace("John W. Garrett", "J. W. Garrett")
s = s.replace("Tejas S. Mathai", "T. S. Mathai")
s = s.replace("Shuai Wang", "S. Wang")
s = s.replace("Yifan Peng", "Y. Peng")
s = s.replace("Hima Tallam", "H. Tallam")
s = s.replace("Thomas C. Shen", "T. C. Shen")
s = s.replace("Tommy", "T. C. Shen")
s = s.replace("Thomas Shen", "T. C. Shen")
s = s.replace("Paul Wakim", "P. Wakim")
s = s.replace("Evrim B. Turkbey", "E. B. Turkbey")
s = s.replace("Andy Chen","A. Chen").replace("Qingyu Chen", "Q. Chen").replace("Zhiyong Lu", "Z. Lu").replace("Bruce Nielson", "B. Nielson")
s = s.replace("Marivi Fernández-Serra", "M.-V. Fernández-Serra")
s = s.replace("\\textquotesingle", "'")
s = s.replace("$\\alpha$", "α")
s = s.replace("'a", "á")
s = s.replace("\\", "")

s = s.replace("D. C. Elton","**D. C. Elton**")

s += """
# Selected Abstracts
<span style=\"font-size:0.9em; font-family: helvetica;\">
<strong>Automated Deep Learning Diagnosis of Hepatic Steatosis on CT Scans Reveals Underreporting by Radiologists</strong><br>
D. Yardeni, T. C. Shen, D. C. Elton, S. Lee, R. M. Summers, Y. Rotman. *The Liver Meeting*, 2022. <br> [[link](https://aasldpubs.onlinelibrary.wiley.com/doi/10.1002/hep.32697)][[pdf](../assets/my_papers/B_AI_medical_imaging/2022_Yardeni_Hepatology_abstract.pdf)]
</span>

<img class="alignright" src="https://www.moreisdifferent.com/wp-content/uploads/2015/09/waterbinding2-300x204.png" alt="atom in a clathrate-like cage" width="100" height="70" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/09/waterbinding2-300x204.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2015/09/waterbinding2-768x523.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2015/09/waterbinding2-1024x698.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2015/09/waterbinding2-1200x818.png 1200w, http://www.moreisdifferent.com/wp-content/uploads/2015/09/waterbinding2.png 1573w" sizes="(max-width: 199px) 100vw, 199px" />
# Ph.D. Thesis
<span style=\"font-size:0.9em; font-family: helvetica;\">
* [Understanding the Dielectric Properties of Water](http://www.moreisdifferent.com/wp-content/uploads/2014/11/Daniel_Elton_Thesis_Final_Copy.pdf) (11 Mb PDF)
</span>

# ChatGPT Deep Research Outputs
<span style=\"font-size:0.9em; font-family: helvetica;\">
* [Graded Exercise Therapy for Chronic Fatigue Syndrome]({{ site.baseurl }}/GET_for_CFS.htm)
</span>

# Old science notes
<span style=\"font-size:0.9em; font-family: helvetica;\">
* [Notes on GAN objective functions](http://www.moreisdifferent.com/assets/science_notes/notes_on_GAN_objective_functions.pdf) (2018)
* [Relation of crystal shape & structure to LO-TO splitting](http://www.moreisdifferent.com/wp-content/uploads/2015/08/loto1.pdf) (2015)
* [Elementary theory of solvation](http://www.moreisdifferent.com/wp-content/uploads/2015/08/solvation4.pdf) (2015)
* [Energy Barriers and Rates &#8211; Transition State Theory for Physicists](http://www.moreisdifferent.com/wp-content/uploads/2015/07/transition_state_theory_dan_elton1.pdf) (2013)
* [Stretched Exponential Relaxation](http://www.moreisdifferent.com/wp-content/uploads/2015/07/stretched.pdf) (2013)
* [Foundations of Quantum Mechanics & Quantum Computing](http://www.moreisdifferent.com/wp-content/uploads/2015/07/foundations-of-qm_dan-elton.pdf) (2012)
* [Hydrogen bond network analysis for TIP4P water](http://www.moreisdifferent.com/wp-content/uploads/2015/07/hydrogen_bond_network_analysis_dan_elton.pdf) (2012)
* [Maxwell&#8217;s equations in different conventions](http://www.moreisdifferent.com/wp-content/uploads/2015/07/maxwells-equations-dan-elton.pdf) (2011)
* [Some errata for _Geometry, Topology, & Physics_ by M. Nakahara](http://www.moreisdifferent.com/wp-content/uploads/2015/08/Nakahara_Errata.pdf) (2011)
* [Equations for the Physics GRE](http://www.moreisdifferent.com/assets/science_notes/physics_GRE_equations.pdf) (2010)
</span>
"""

with open("science.md", 'w') as f:
    f.writelines(s)

print("total papers = ", tot)
