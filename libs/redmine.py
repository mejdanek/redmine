def get_all_issues(redmineobj, project):
    for issue in project.issues:
        #print(list(issue))
        print("#{}\t{}\t{}\t{}".format(issue.id, issue.subject, issue.created_on, issue.author))

#def new_issue(title,version,description,author):
#   with redmine.session(return_response=False):
#       issue = redmine.issue.create(project_id = project.id, subject = title, fixed_version_id = version)
#    return project.issues[0].id

def new_issue(redmineobj, item):
    project, title, version = redmineobj.project.get(item[0]), item[1], item[2]
    with redmineobj.session(return_response=False):
        redmineobj.issue.create(
            project_id = project.id,
            subject = "{} {}".format(version, title),
            fixed_version_id = version
            )
    return project.issues[0].id

def get_issue(redmineobj, nr_issue):
    return redmineobj.issue.get(nr_issue)

def update_issue(redmineobj, nr_issue,author):
    redmineobj.issue.update(nr_issue,assigned_to_id=author)

if __name__ == "__main__":
    print("Not directly executable")