#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import json
import math
import random

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234

Torstein = "C:\\Kode\\GitHub\\KBE-welding-trajectory\\" #location
Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\" #location
yourLocation = Aashild #must be changed after whom is using it

class MyHandler(BaseHTTPRequestHandler):

    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()


    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        # Check what is the path
        path = s.path
        
        if path.find("/") != -1 and len(path) == 1:
            startPage = open("HTML/startPage.HTML", 'r')
            startPageText = startPage.read()
            s.wfile.write(bytes(startPageText, 'utf-8'))

        elif path.find("/orderWeldingLines") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            userInterface = open("HTML/uploadImage_test.html", "r") #reading the userinterface html-page
            UItext = userInterface.read()
            """
            # changing the params displayed
            for i in range(len(variablesToReplace)):
                UItext = UItext.replace(variablesToReplace[i], str(custom_parameters[i])) # the data about the pipe-env

            for i in range(len(custommerInfoToChange)):
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i])) # the data about the customer

            UItext = UItext.replace('#messageToCustomer#', messageToCustomer) # handeling error messages to the customer

            s.wfile.write(bytes(UItext, 'utf-8')) # writing to the local host
            """
        elif path.find("/yourParameters") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            userInterface = open("HTML/userInterface.html", "r") #reading the userinterface html-page
            UItext = userInterface.read()

            # changing the params displayed
            for i in range(len(variablesToReplace)):
                if custom_parameters[i].find("%2C"):
                    custom_parameters[i] = custom_parameters[i].replace("%2C", ",") #taking care of the ","
                UItext = UItext.replace(variablesToReplace[i], str(custom_parameters[i])) # the data about the pipe-env
            
            for i in range(len(custommerInfoToChange)):
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i])) # the data about the customer

            UItext = UItext.replace('#messageToCustomer#', messageToCustomer) # handeling error messages to the customer

            s.wfile.write(bytes(UItext, 'utf-8')) # writing to the local host

        elif path.find("/sendOrder") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            
            orderAcceptedMsg = open("HTML/orderAccepted.html", 'r')
            orderMsgText = orderAcceptedMsg.read()
            s.wfile.write(bytes(orderMsgText, 'utf-8'))# writing to the local host
         

    def do_POST(s):
        #allowing us to edit the custom parameters
        global custom_parameters, messageToCustomer, custommerInfo, yourLocation
        
        
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        

		# Check what is the path
        path = s.path
        if path.find("/yourParameters") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            #print("param line", param_line)

			#making a string to print
            global print_order, yourLocation
            print_order = ""

            custom_parameters = stringSplit(custom_parameters, param_line)
            
            

            
			# check if input is valid
            errorMsg = checkCustomerInput(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, num_node_ax, pipDia)

            messageToCustomer = "Something wrong has happened.<br>"
            inputError = False
            for i in errorMsg: # going through the error messages
                if "ok" not in i:
                    inputError = True
                    messageToCustomer += i + " "
                    #be brukeren skrive inn på nytt og gi tilbakemelding på hva som er feil. 
                    # send brukeren til yourParameters"
                    ...
            if not inputError:
                messageToCustomer = "Your system is accepted."


            # take picture of the drawCustomerInfo 
                # calling drawGivenInfo.py
                # tegne noe i nx av seg selv
                # picture function må lages
                # send image to web
            
            

            s.do_GET() #this is not a optimal solution

        elif path.find("/sendOrder") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            
            # string parsing av customer info ( name, number..)
            custommerInfo = stringSplit(custommerInfo, param_line)
            name= custommerInfo[0]
            pNumber= custommerInfo[1]
            eMail= custommerInfo[2]
            compName= custommerInfo[3]

            systemPathObject = pathInterpreter.pipeSystem(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, num_node_ax, pipDia)
            systemPath = systemPathObject.makePath()
            

            # give new path to dfa template:
                # input params: new path list, env_size, eq_size_list, eq_pos, pipDia, company_name, custommer name.
            # save a file with new 
            filename = makeDFA(num_eq, eq_size_list, eq_pos,eq_in_out, env_size, startPoint, endPoint, pipDia, custommerInfo, systemPath, yourLocation)

            print("The order from ", name, ", ", compName, " is now stored in the folder 'GeneratedSystems' as ", filename, ".")
            s.do_GET()


        elif path.find("/"):
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            s.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))

def stringSplit(paramContainer, param_line):
    if param_line.find("%2C"): # replacing "%2C" with ','
        param_line = param_line.replace("%2C", ',')
    if param_line.find("%40"):
        param_line = param_line.replace("%40", "@")
    
    #getting the parameter values
    key_val_pair = param_line.split('&')							#splitting the string at "&"
    for i in range(len(paramContainer)): 						#itterating through the custom_parameter list
        paramContainer[i] = key_val_pair[i].split('=')[1]		#spliting at "=" to only get the value
        if "+" in paramContainer[i]:
            paramContainer[i]= paramContainer[i].replace("+", " ")

    return paramContainer