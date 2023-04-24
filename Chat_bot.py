import requests

print('want to sell waste?')
res1 = input()


if (res1 == "yes"):
    print("what type of waste do you want to sell?")
    print(" A) E-waste")
    print(" B) paper waste")
    print(" C) plastic waste")
    print(" D) other")

    r = input("write correct option:")

    message = f"type of waste: {r}\n"
    bot_token = "5706459736:AAGp7t_ifrwWRQK--Z9NU5c44OK3j66Cn-k"
    chat_id = "5166919718"
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    post_fields = {"chat_id": chat_id, "text": message}

    # Send the message using the Telegram API
    response = requests.post(api_url, data=post_fields)
    if response.status_code != 200:
        print(f"Failed to send message to Telegram chat: {response.text}")


    if(r=="A"):
        s= input("write your type of e-waste , e.g refrigerator, washing machine, fan ,ac, etc. ")
        t= input ("weight of product ")
        u =input("location of user ")
        v= input ("user contact number ")
        w=input( "would you like to contact our consumer care services? ")

        message = f"responses for e-waste: {s}\n{t}\n{u}\n{v}\n{w}\n"
        bot_token = "5706459736:AAGp7t_ifrwWRQK--Z9NU5c44OK3j66Cn-k"
        chat_id = "5166919718"
        api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        post_fields = {"chat_id": chat_id, "text": message}

        # Send the message using the Telegram API
        response = requests.post(api_url, data=post_fields)
        if response.status_code != 200:
            print(f"Failed to send message to Telegram chat: {response.text}")


        if (w=="yes"):
            print("Please wait. We are trying to contact the client as soon as possible ")
        else:
            print("we wil be reaching out to you soon. thank you for choosing 3R ZeroWaste pvt ltd.")
    elif (r=="B"):
        x=input("weight of product ")
        y=input("location of user ")
        z=input("user contact number ")

        message = f"responses for paper waste: {x}\n{y}\n{z}\n"
        bot_token = "5706459736:AAGp7t_ifrwWRQK--Z9NU5c44OK3j66Cn-k"
        chat_id = "5166919718"
        api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        post_fields = {"chat_id": chat_id, "text": message}

        # Send the message using the Telegram API
        response = requests.post(api_url, data=post_fields)
        if response.status_code != 200:
            print(f"Failed to send message to Telegram chat: {response.text}")
    elif(r=="C"):
        a=input("what is the material of the plastic ")
        b=input("weight of product ")
        c=input("location of user ")
        d=input("user contact number ")

        message = f"responses for plastic waste: {a}\n{b}\n{c}\n{d}\n"
        bot_token = "5706459736:AAGp7t_ifrwWRQK--Z9NU5c44OK3j66Cn-k"
        chat_id = "5166919718"
        api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        post_fields = {"chat_id": chat_id, "text": message}

        # Send the message using the Telegram API
        response = requests.post(api_url, data=post_fields)
        if response.status_code != 200:
            print(f"Failed to send message to Telegram chat: {response.text}")
    elif(r=="D"):
        e=input("please specify other type of waste: ")
        print ("we will look into how we cacan process it and get back to you for the same")

        message = f"responses for other type of waste: {e}\n"
        bot_token = "5706459736:AAGp7t_ifrwWRQK--Z9NU5c44OK3j66Cn-k"
        chat_id = "5166919718"
        api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        post_fields = {"chat_id": chat_id, "text": message}

        # Send the message using the Telegram API
        response = requests.post(api_url, data=post_fields)
        if response.status_code != 200:
            print(f"Failed to send message to Telegram chat: {response.text}")