# remote_handler
#
# This is a remote connection machine to execute the command script
#
# You can use this script to Execute the command remotely, and it will 
# execute the results to return 
# 
#####################################################################
# This program has two ways to use remote action
# 
# The first is the interactive mode, you can run this program, will enter the 
# interactive mode, you can enter the command to be executed, enter
# 
# The second is to read the configuration file mode, you can define a command 
# configuration file, the file as the first parameter of the #  program, enter
#
#####################################################################
#
# How to use script?
``` 
# such as:

First mode:
root@carltonxu-dev: python remote_handler.py
[command]>> hostname
localhost: "carltonxu-dev"
127.0.0.1: "carltonxu-dev"
[command]>> 

second mode:
root@carltonxu-dev:python remote_handler.py command_file.txt
localhost: "carltonxu-dev"
127.0.0.1: "carltonxu-dev"
```  
