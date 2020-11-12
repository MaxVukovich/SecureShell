
#links Andrew, Tanmay, Ahmad Journal
def journal1():
    greeting = "What's Good!"
    name = "Google Doc"
    doa = "November 6"
    job = "Journal Record Group 1"
    embed = "https://docs.google.com/document/d/1-UAGwPRwrVyJvLPtaW597b4U8GfcQATbWQZXWXvoxgo/edit#"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

#links Max, Luca, Cody Journal
def journal2():
    greeting = "Yurrrr!"
    name = "Google Doc"
    doa = "November 6"
    job = "Journal Record Group 2"
    embed = "https://docs.google.com/document/d/1f-aT5hgvu_h0xv1gSOvz8Ls-oXVEXlLowsxZdkN6YZw/edit"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def alldata():
    return [journal1(), journal2()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Nighthawk Coding"
    github = "https://github.com/MaxVukovich/SecureShell"
    source = {"name": name, "github": github}
    #Project Data
    project1 =  "Hello Series"
    projlinks1 = [
        Link("Project Plan", "https://docs.google.com/document/d/1oDSYDH4TLnrq1seO0PEO6nYHXbi3XMscEtPeNIbfMIk/edit"),
        Link("Repl", "https://repl.it/@TMarwah/Team3-SSH-Login#main.py"),
        Link("Resources", "https://padlet.com/jmortensen7/csp2021")
    ]
    project2 =  "Flask Project"
    projlinks2 = [
        Link("Project Plan", "https://docs.google.com/document/d/1oDSYDH4TLnrq1seO0PEO6nYHXbi3XMscEtPeNIbfMIk/edit"),
        Link("Repl", "https://repl.it/@TMarwah/p2-TanmayA#main.py"),
        Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
    ]
    #Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects
