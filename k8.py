#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess 
import cgi   

z = cgi.FieldStorage()
input = z.getvalue("x")

value = input.split()
if value[0] == "1":
    i_name = value[1]
    d_name = value[2]
    cmd = "kubectl create deployment " + (d_name) + " --image=" + (i_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8ws/admin.conf")
    print(output)
elif value[0] == "2":
    i_name = value[1]
    p_name = value[2]
    cmd = "kubectl run " + (p_name) + " --image=" + (i_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8ws/admin.conf")
    print(output)
elif value[0] == "3":
    p_name = value[1]
    cmd = "kubectl delete pod " + (p_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8ws/admin.conf")
    print(output)
elif value[0] == "4":
    d_name = value[1]
    cmd = "kubectl delete deployment " + (d_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8ws/admin.conf")
    print(output)
elif value[0] == "5":
    d_name = value[1]
    port = value[2]
    cmd = "kubectl expose deployment " + (d_name) + " --port=" + (port) + " --type=NodePort"
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8ws/admin.conf")
    print(output)
elif value[0] == "6":
    d_name = value[1]
    replica = value[2]
    cmd = "kubectl scale deployment " + (d_name) + " --replicas=" + (replica)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig /root/k8ws/admin.conf")
    print(output)
elif value[0] == "7":
    cmd = "sudo kubectl get pods --kubeconfig /root/k8ws/admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)
elif value[0] == "8":
    cmd = "kubectl get deployments --kubeconfig /root/k8ws/admin.conf"
    output = subprocess.getoutput("sudo " + cmd)
    print(output)
elif value[0] == "9":
    cmd = "sudo kubectl get svc --kubeconfig /root/k8ws/admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)
elif value[0] == "10":
    cmd = "kubectl delete all --all --kubeconfig /root/k8ws/admin.conf"
    output = subprocess.getoutput("sudo " + cmd)
    print(output)
elif value[0] == "11":
    print("Sorry, No results found !!")
