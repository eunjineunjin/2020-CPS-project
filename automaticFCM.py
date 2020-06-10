from pyfcm import FCMNotification

mApi_key = "AAAA5ZH8TEo:APA91bEwkLBs3nluSJXvy7ICS2NQoMKfXkdba86NrM_hP1rZdzTktRSMGQc_1cX8JeDgFpBoopOOoZCg4sEoeHzf_Qo2cwwJ-s7uX-wa4obk8OQVXgkjrHlECa_ghoJbWD_ny0xLknNY"
mToken = "985996741706"

push_service = FCMNotification(api_key=mApi_key)


mMessage = {
    "body" : "test1"
}

# result = push_service.single_device_data_message(registration_id=mToken, data_message=data_message)


message_title = "ttitle"
message_body = "bbdoy"




#result = push_service.notify_multiple_devices(registration_ids=push_tokens, message_title=message_title, message_body=message_body)

result = push_service.notify_single_device(registration_id=mToken, message_title=message_title, message_body=message_body)


print(result)
