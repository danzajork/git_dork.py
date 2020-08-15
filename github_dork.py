#!/usr/bin/python3
import os
from argparse import ArgumentParser
from jinja2 import Template

RESULTS_DIRECTORY = './git_results'

def create_working_folder(domain):

    path = os.getcwd()

    if not os.path.exists(f"{path}/{RESULTS_DIRECTORY}/"):
        os.mkdir(f"{path}/{RESULTS_DIRECTORY}/")

    folder = f"{path}/{RESULTS_DIRECTORY}/{domain}"

    try:
        os.mkdir(folder)
    except OSError:
        print("Creation of the directory %s failed" % path)

    return folder

def read_template(uri):

    with open(uri, "r") as file:
        return Template(file.read())


def write_report(working_folder, domain,
                 filename="git_search.html") -> None:
    
    template = read_template("templates/simple.html")

    links = { 
        "Password":         f"https://github.com/search?q=%22{domain}%22+password&type=Code", 
        "npmrc _auth":      f"https://github.com/search?q=%22{domain}%22+npmrc%20_auth&type=Code", 
        "dockercfg":        f"https://github.com/search?q=%22{domain}%22+dockercfg&type=Code", 
        "pem private":      f"https://github.com/search?q=%22{domain}%22+pem%20private&type=Code", 
        "id_rsa":           f"https://github.com/search?q=%22{domain}%22+id_rsa&type=Code", 
        "aws_access_key_id": f"https://github.com/search?q=%22{domain}%22+aws_access_key_id&type=Code", 
        "s3cfg":            f"https://github.com/search?q=%22{domain}%22+s3cfg&type=Code", 
        "htpasswd":         f"https://github.com/search?q=%22{domain}%22+htpasswd&type=Code", 
        "git-credentials":  f"https://github.com/search?q=%22{domain}%22+git-credentials&type=Code",
        "bashrc password":  f"https://github.com/search?q=%22{domain}%22+bashrc%20password&type=Code", 
        "sshd_config":      f"https://github.com/search?q=%22{domain}%22+sshd_config&type=Code",
        "xoxp OR xoxb OR xoxa": f"https://github.com/search?q=%22{domain}%22+xoxp%20OR%20xoxb%20OR%20xoxa&type=Code",
        "SECRET_KEY":       f"https://github.com/search?q=%22{domain}%22+SECRET_KEY&type=Code",
        "client_secret":    f"https://github.com/search?q=%22{domain}%22+client_secret&type=Code",
        "sshd_config":      f"https://github.com/search?q=%22{domain}%22+sshd_config&type=Code",
        "github_token":     f"https://github.com/search?q=%22{domain}%22+github_token&type=Code",
        "api_key":          f"https://github.com/search?q=%22{domain}%22+api_key&type=Code",
        "FTP":              f"https://github.com/search?q=%22{domain}%22+FTP&type=Code",
        "app_secret":       f"https://github.com/search?q=%22{domain}%22+app_secret&type=Code",
        "passwd":           f"https://github.com/search?q=%22{domain}%22+passwd&type=Code",
        "s3.yml":           f"https://github.com/search?q=%22{domain}%22+.env&type=Code",
        ".exs":             f"https://github.com/search?q=%22{domain}%22+.exs&type=Code",
        "beanstalkd.yml":   f"https://github.com/search?q=%22{domain}%22+beanstalkd.yml&type=Code",
        "deploy.rake":      f"https://github.com/search?q=%22{domain}%22+deploy.rake&type=Code",
        "mysql":            f"https://github.com/search?q=%22{domain}%22+mysql&type=Code",
        "credentials":      f"https://github.com/search?q=%22{domain}%22+credentials&type=Code",
        "PWD":              f"https://github.com/search?q=%22{domain}%22+PWD&type=Code",
        ".bash_history":    f"https://github.com/search?q=%22{domain}%22+.bash_history&type=Code",
        ".sls":             f"https://github.com/search?q=%22{domain}%22+.sls&type=Code",
        "secrets":          f"https://github.com/search?q=%22{domain}%22+secrets&type=Code",
        "composer.json":    f"https://github.com/search?q=%22{domain}%22+composer.json&type=Code"
        }

    output = template.render(domain=domain,links=links)

    with open(f"{working_folder}/{filename}", "w") as file:
        file.write(output)    


def main():
    parser = ArgumentParser()
    parser.add_argument("-d", "--domain", dest="domain", help="Domain to target")
    args = parser.parse_args()

    write_report(create_working_folder(args.domain), args.domain)

if __name__ == "__main__": main()